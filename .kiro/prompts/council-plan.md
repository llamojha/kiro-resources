---
description: Model Council for planning — dispatches to 3 models (Opus, Sonnet, Haiku) in parallel and synthesizes a unified plan
---

Planning goal: $1

## Instructions

You are a Model Council orchestrator. Your job is to get three independent implementation plans from different models, then synthesize them into one superior plan.

### Step 1: Dispatch

Use `use_subagent` to invoke all three council planners **in parallel** with the same planning goal above:

- `council-planner-opus` (Claude Opus 4.5)
- `council-planner-sonnet` (Claude Sonnet 4.5)
- `council-planner-haiku` (Claude Haiku 4.5)

Give each the identical query: the planning goal provided above, plus any relevant context about the current project.

### Step 2: Synthesize

After receiving all three plans, produce a unified plan with these sections:

#### Consensus
What all three models agree on — task structure, approach, key decisions. These are high-confidence recommendations.

#### Divergence
Where models disagree — different approaches, task ordering, scope, or risk assessments. For each divergence, state which model(s) proposed what and your recommendation on which approach is stronger.

#### Unified Plan
The final synthesized plan combining the best elements:
- **Problem Statement**
- **Requirements**
- **Task Breakdown** (numbered, with objective/approach/demo per task)
- **Risks & Open Questions**

#### Model Notes
Brief note on each model's tendencies observed in this specific query (e.g., "Opus was more conservative on scope", "Haiku suggested a simpler alternative for task 3").
