# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "boto3>=1.35.0",
# ]
# ///
"""Optimize a prompt file using AWS Bedrock OptimizePrompt API.

Usage: uv run .kiro/skills/prompt-optimizer/scripts/optimize.py [OPTIONS]

Options:
  --file <path>       File to optimize (required)
  --model <id>        Target model ID or alias (default: nova-2-lite)
  --output <format>   Output format: json, diff, text (default: json)
  --write <path>      Write optimized content to file
  --list-models       List supported models and exit
  --help              Show help and exit

Exit codes: 0=success, 1=file not found, 2=API error, 3=invalid args
"""
import argparse
import json
import os
import sys

MODEL_ALIASES = {
    "claude-opus-4.7": "anthropic.claude-opus-4-7",
    "claude-opus-4.6": "anthropic.claude-opus-4-6-v1",
    "claude-sonnet-4.6": "anthropic.claude-sonnet-4-6",
    "claude-opus-4.5": "anthropic.claude-opus-4-5-20251101-v1:0",
    "claude-sonnet-4.5": "anthropic.claude-sonnet-4-5-20250929-v1:0",
    "claude-sonnet-4": "anthropic.claude-sonnet-4-20250514-v1:0",
    "claude-haiku-4.5": "anthropic.claude-haiku-4-5-20251001-v1:0",
    "nova-2-lite": "amazon.nova-2-lite-v1:0",
    "nova-pro": "amazon.nova-pro-v1:0",
}

# Region availability per model (single-region support from docs)
MODEL_REGIONS: dict[str, list[str]] = {
    "anthropic.claude-opus-4-7": [],
    "anthropic.claude-opus-4-6-v1": [],
    "anthropic.claude-sonnet-4-6": [],
    "anthropic.claude-opus-4-5-20251101-v1:0": [],
    "anthropic.claude-sonnet-4-5-20250929-v1:0": [],
    "anthropic.claude-sonnet-4-20250514-v1:0": [],
    "anthropic.claude-haiku-4-5-20251001-v1:0": [],
    "amazon.nova-2-lite-v1:0": [],
    "amazon.nova-pro-v1:0": ["ap-southeast-2", "eu-west-2", "us-east-1"],
}


def resolve_model(name: str) -> str:
    return MODEL_ALIASES.get(name, name)


def unified_diff(original: str, optimized: str, filename: str) -> str:
    orig_lines = original.splitlines()
    opt_lines = optimized.splitlines()
    lines = [f"--- a/{filename}", f"+++ b/{filename}"]
    max_len = max(len(orig_lines), len(opt_lines))
    lines.append(f"@@ -1,{len(orig_lines)} +1,{len(opt_lines)} @@")
    for i in range(max_len):
        if i < len(orig_lines) and i < len(opt_lines):
            if orig_lines[i] == opt_lines[i]:
                lines.append(f" {orig_lines[i]}")
            else:
                lines.append(f"-{orig_lines[i]}")
                lines.append(f"+{opt_lines[i]}")
        elif i >= len(orig_lines):
            lines.append(f"+{opt_lines[i]}")
        else:
            lines.append(f"-{orig_lines[i]}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Optimize a prompt file using AWS Bedrock OptimizePrompt API."
    )
    parser.add_argument("--file", help="File to optimize (required unless --list-models)")
    parser.add_argument("--model", default="nova-2-lite", help="Target model ID or alias (default: nova-2-lite)")
    parser.add_argument("--output", choices=["json", "diff", "text"], default="json", help="Output format (default: json)")
    parser.add_argument("--write", help="Write optimized content to file")
    parser.add_argument("--list-models", action="store_true", help="List supported models and exit")
    args = parser.parse_args()

    if args.list_models:
        models = [{"alias": k, "id": v} for k, v in MODEL_ALIASES.items()]
        print(json.dumps(models, indent=2))
        sys.exit(0)

    if not args.file:
        print("Error: --file is required.", file=sys.stderr)
        parser.print_usage(sys.stderr)
        sys.exit(3)

    file_path = os.path.abspath(args.file)
    if not os.path.isfile(file_path):
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    with open(file_path, "r") as f:
        original = f.read()

    tokens_est = len(original) // 4
    if tokens_est > 1000:
        print(
            f"Warning: input is ~{tokens_est} tokens ({len(original)} chars). "
            "OptimizePrompt works best under ~1000 tokens.",
            file=sys.stderr,
        )

    model_id = resolve_model(args.model)
    print(f"Optimizing {args.file} for {model_id}...", file=sys.stderr)

    import boto3

    region = os.environ.get("AWS_REGION", "eu-central-1")

    supported_regions = MODEL_REGIONS.get(model_id)
    if supported_regions and region not in supported_regions:
        print(
            f"Warning: {model_id} may not be available in {region}. "
            f"Supported regions: {', '.join(supported_regions)}",
            file=sys.stderr,
        )

    client = boto3.client("bedrock-agent-runtime", region_name=region)

    analysis = ""
    optimized = ""

    try:
        response = client.optimize_prompt(
            input={"textPrompt": {"text": original}},
            targetModelId=model_id,
        )
        for event in response["optimizedPrompt"]:
            if "optimizedPromptEvent" in event:
                opt_prompt = event["optimizedPromptEvent"].get("optimizedPrompt", {})
                if "textPrompt" in opt_prompt:
                    optimized = opt_prompt["textPrompt"].get("text", "")
            elif "analyzePromptEvent" in event:
                analysis = event["analyzePromptEvent"].get("message", "")
    except Exception as e:
        print(f"Error: Bedrock API call failed: {e}", file=sys.stderr)
        sys.exit(2)

    if not optimized:
        print("Error: no optimized prompt returned from API.", file=sys.stderr)
        sys.exit(2)

    if args.write:
        write_path = os.path.abspath(args.write)
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        with open(write_path, "w") as f:
            f.write(optimized)
        print(f"Written to {args.write}", file=sys.stderr)

    filename = os.path.basename(args.file)

    if args.output == "diff":
        print(unified_diff(original, optimized, filename))
    elif args.output == "text":
        print(optimized)
    else:
        print(json.dumps({
            "file": args.file,
            "model": model_id,
            "analysis": analysis,
            "original": original,
            "optimized": optimized,
            "charDiff": len(optimized) - len(original),
        }, indent=2))


if __name__ == "__main__":
    main()
