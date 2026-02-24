# Planner Agent — Requirements

## User Story

As a developer using Kiro CLI, I want a planning-to-execution agent that gathers requirements, identifies design gaps, produces a structured plan, then creates a todo list and implements tasks using specialized subagents — so I can go from idea to working code in a single conversation.

## Core Requirements

1. **Structured requirements gathering** — Present numbered, multiple-choice questions to clarify scope, platform, constraints, and priorities. Accept flexible answers (e.g. "1=a, 2=b" or freeform). Iterate until clear.
2. **Gap analysis** — Explore the codebase, identify existing patterns and constraints, call out gaps/risks/ambiguities in the design, and ask follow-up questions to resolve them before planning.
3. **Implementation plan output** — Produce a complete plan containing: problem statement, requirements list, numbered task breakdown with objectives, assigned agents, guidance, demo descriptions, and dependency graph.
4. **Parallel task identification** — Mark which tasks can run concurrently (no dependencies on each other).
5. **Agent assignment** — Assign a specialist agent to each task from the project's available custom agents.
6. **Approval gate** — Present the full plan and wait for user approval before executing.
7. **Todo list creation** — On approval, create a todo list with all tasks using the `todo_list` tool.
8. **Subagent execution** — Implement tasks by delegating to specialized subagents via `use_subagent`, running independent tasks in parallel (up to 4), respecting dependency order.
9. **Progress tracking** — Mark tasks complete as subagents finish, report progress after each batch.

## Constraints

- Must follow the official Kiro CLI agent JSON format.
- Prompt externalized via `file://` URI.
- Must load project steering docs as resources.
- Planning phases (1-3) use only read tools. Write/execute happens only through subagents in Phase 4.

## Out of Scope

- Automatic agent switching (Kiro CLI handles this natively).
- MCP server integrations.
- Multi-conversation plan continuity (one plan per conversation).
