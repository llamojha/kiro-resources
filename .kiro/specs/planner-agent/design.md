# Planner Agent — Design

## Architecture

```
.kiro/
├── agents/
│   └── planner.json          # Agent config (tools, resources, prompt ref)
└── specs/
    └── planner-agent/
        ├── requirements.md    # Requirements spec
        ├── design.md          # This file
        └── prompt.md          # Externalized system prompt
```

## Agent Configuration

| Field | Value | Rationale |
|-------|-------|-----------|
| `tools` | `fs_read`, `grep`, `glob`, `thinking`, `web_search`, `web_fetch`, `todo_list`, `use_subagent` | Read tools for planning + todo/subagent for execution |
| `allowedTools` | `fs_read`, `grep`, `glob`, `thinking`, `todo_list` | Auto-approve read-only + todo; web/subagent tools prompt |
| `resources` | `file://.kiro/steering/*.md` | Load project conventions into context |
| `prompt` | `file://.kiro/specs/planner-agent/prompt.md` | Externalized for maintainability |
| `keyboardShortcut` | `ctrl+shift+p` | Quick toggle ("plan" mnemonic) |

## Workflow Phases

```
Phase 1: Requirements    Phase 2: Gap Analysis    Phase 3: Plan Output    Phase 4: Execution
─────────────────────    ────────────────────     ──────────────────      ─────────────────
Ask questions     ──►    Explore codebase   ──►   Present full plan ──►  Create todo list
Clarify scope            Identify gaps            Assign agents          Spawn subagents
Iterate                  Flag risks               Map dependencies       Track progress
                         Resolve ambiguities      Get approval           Report results
```

## Execution Model

Phase 4 uses `use_subagent` to delegate implementation:

1. `ListAgents` — discover available custom agents
2. Group tasks by dependency level (independent tasks at same level)
3. For each level, spawn up to 4 parallel subagents with:
   - `agent_name` — the assigned custom agent
   - `query` — the task objective
   - `relevant_context` — file paths, constraints, conventions
4. Mark completed tasks in todo list
5. Proceed to next dependency level

The planner itself never writes files or runs commands — all implementation flows through subagents which have their own tool access.

## Key Decisions

- **No `fs_write`/`execute_bash` on planner**: Implementation is fully delegated to subagents. This keeps the planner focused on orchestration.
- **`use_subagent` not auto-approved**: User confirms before each subagent spawn, maintaining control over execution.
- **`todo_list` auto-approved**: Creating/updating the task list is low-risk and frequent during execution.
- **Steering docs as resources**: Ensures plans respect project conventions (minimal scope, YAGNI, agent assignment) without searching.
- **`thinking` tool included**: Complex gap analysis and dependency mapping benefit from structured reasoning.

## Differences from Built-in `kiro_planner`

| Aspect | Built-in | Custom |
|--------|----------|--------|
| Prompt | Hardcoded | Externalized, editable |
| Gap analysis | Implicit | Explicit phase with risk flagging |
| Plan output | Informal | Structured with agents + dependencies |
| Execution | Hands off to user | Creates todo list + spawns subagents |
| Agent assignment | Not built-in | Maps tasks to custom agents |
| Conventions | Generic | Loads project steering docs |
| Customizable | No (cannot edit built-ins) | Version-controlled |
