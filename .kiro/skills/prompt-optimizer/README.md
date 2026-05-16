# Prompt Optimizer Skill

Optimize prompt files using AWS Bedrock's OptimizePrompt API. Works on `.kiro/prompts/`, Lambda system prompts, or any text/markdown file.

## Installation

Copy the skill folder into any project:

```bash
cp -r .kiro/skills/prompt-optimizer <your-project>/.kiro/skills/
```

No npm dependencies or config changes needed.

## Prerequisites

- **`uv`** — Python package runner (`brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- **AWS credentials** — configured via `~/.aws/credentials`, env vars, or SSO with Bedrock access
- **Region** — defaults to `eu-central-1`, override with `AWS_REGION=us-east-1`

## Usage via Kiro (LLM invocation)

Ask naturally in a Kiro chat session:

```
> optimize my commit-message prompt
> improve .kiro/prompts/debug-helper.md for claude-sonnet-4
> can you optimize this prompt file?
```

Kiro will detect the skill, run the script, show you a diff, and ask whether to replace, save separately, or keep the original.

## Usage via script (direct invocation)

```bash
# Basic — optimize with default model (nova-2-lite)
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file .kiro/prompts/commit-message.md

# Choose a model
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file .kiro/prompts/debug-helper.md --model claude-opus-4.6

# See the diff
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file .kiro/prompts/brainstorm.md --output diff

# Write optimized version to a separate folder
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file .kiro/prompts/commit-message.md --write .kiro/prompts-optimized/commit-message.md

# Replace in place
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file .kiro/prompts/commit-message.md --write .kiro/prompts/commit-message.md

# List available models
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --list-models
```

## Supported Models

| Alias | Model ID |
|-------|----------|
| `nova-2-lite` (default) | amazon.nova-2-lite-v1:0 |
| `nova-pro` | amazon.nova-pro-v1:0 |
| `claude-opus-4.7` | anthropic.claude-opus-4-7 |
| `claude-opus-4.6` | anthropic.claude-opus-4-6-v1 |
| `claude-sonnet-4.6` | anthropic.claude-sonnet-4-6 |
| `claude-opus-4.5` | anthropic.claude-opus-4-5-20251101-v1:0 |
| `claude-sonnet-4.5` | anthropic.claude-sonnet-4-5-20250929-v1:0 |
| `claude-sonnet-4` | anthropic.claude-sonnet-4-20250514-v1:0 |
| `claude-haiku-4.5` | anthropic.claude-haiku-4-5-20251001-v1:0 |

## Notes

- OptimizePrompt works best on prompts under ~1000 tokens (~4000 chars)
- The script warns if input exceeds this but still proceeds
- For Lambda system prompts embedded in code: extract to a temp file, optimize, paste back
