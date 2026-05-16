---
name: prompt-optimizer
description: Optimize prompt files using AWS Bedrock OptimizePrompt API. Use when the user wants to improve, optimize, or rewrite a prompt file for better model performance.
---

# Prompt Optimizer Skill

## Overview
You are using the **prompt-optimizer** skill to enhance prompt files via AWS Bedrock's OptimizePrompt API. This skill improves prompt effectiveness and model performance through intelligent rewriting.

**Important**: Always announce at the start: "I'm using the prompt-optimizer skill to optimize your prompt with Bedrock."

## Activation Triggers
Use this skill when the user:
- Requests prompt optimization, improvement, or rewriting
- Wants to enhance prompt effectiveness for a specific model
- Desires comparison between original and optimized prompt versions

## Execution Workflow

### Step 1: Target File Identification
Identify which file to optimize. If unspecified, ask the user to clarify.

<valid_targets>
- `.kiro/prompts/*.md` — Kiro CLI prompt files
- Lambda system prompts (extract prompt string to temporary file first)
- Any markdown or text file containing a prompt
</valid_targets>

### Step 2: Target Model Selection
**Default model**: `nova-2-lite` (Amazon Nova 2 Lite)

Ask the user if they prefer a different model from the available options:

<model_aliases>
| Alias | Full Model ID | Notes |
|-------|---------------|-------|
| `claude-opus-4.7` | anthropic.claude-opus-4-7 | Experimental, 1M context |
| `claude-opus-4.6` | anthropic.claude-opus-4-6-v1 | |
| `claude-sonnet-4.6` | anthropic.claude-sonnet-4-6 | 1M context |
| `claude-opus-4.5` | anthropic.claude-opus-4-5-20251101-v1:0 | |
| `claude-sonnet-4.5` | anthropic.claude-sonnet-4-5-20250929-v1:0 | |
| `claude-sonnet-4` | anthropic.claude-sonnet-4-20250514-v1:0 | Default Claude |
| `claude-haiku-4.5` | anthropic.claude-haiku-4-5-20251001-v1:0 | |
| `nova-2-lite` | amazon.nova-2-lite-v1:0 | Default overall |
| `nova-pro` | amazon.nova-pro-v1:0 | |
</model_aliases>

### Step 3: Execute Optimization Script
Run the optimization command:

```bash
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py --file <path> --model <alias-or-id> --output diff
```

### Step 4: Present Results
Display the optimization results to the user:
1. Show the diff between original and optimized versions
2. Include Bedrock's analysis message explaining the changes
3. Highlight key improvements made

### Step 5: Apply User Decision
Ask the user how to proceed with the optimized result:

<action_options>
- **Replace original**: Execute with `--write <original-path>` to overwrite the existing file
- **Save separately**: Execute with `--write .kiro/prompts-optimized/<filename>` to preserve original
- **Keep original only**: Take no action, discard optimized version
</action_options>

## Script Reference

### Main Script
**Location**: `scripts/optimize.py`
**Execution**: Self-contained, run with `uv run`

### Command Syntax
```bash
uv run .kiro/skills/prompt-optimizer/scripts/optimize.py [OPTIONS]
```

### Available Options
```
--file <path>       Path to file for optimization (REQUIRED)
--model <id>        Target model ID or alias (default: nova-2-lite)
--output <format>   Output format: json | diff | text (default: json)
--write <path>      Write optimized content to specified file path
--list-models       Display all supported models and exit
--help              Show help information and exit
```

## Important Constraints and Requirements

<constraints>
1. **Optimal prompt length**: Bedrock OptimizePrompt performs best on prompts under ~1000 tokens (~4000 characters)
2. **Length warning**: Script issues stderr warning if input exceeds threshold but continues processing
3. **AWS credentials**: Requires configured AWS credentials with Bedrock access in eu-central-1 region
4. **Dependencies**: Requires `uv` installed for self-contained script execution with inline dependencies
5. **Lambda prompts**: For system prompts embedded in code, extract to temporary file, optimize, then reintegrate
</constraints>

## Execution Notes
- Always verify file path exists before running optimization
- Confirm model selection with user before proceeding
- Present clear before/after comparison for user evaluation
- Preserve original files unless user explicitly requests replacement
