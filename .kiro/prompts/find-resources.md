# Find Resources

This prompt helps you discover and install Kiro resources from KiroHub — the community hub for Steering files, Hooks, Powers, Prompts, Agents, and Skills.

## When to Use This Prompt

Use this prompt when the user:
* Asks "how do I do X" where X might be a common task with an existing resource
* Says "find a resource for X" or "is there a steering file for X"
* Asks "can you do X" where X is a specialized capability
* Wants to search for Kiro resources, tools, or automation patterns
* Mentions they wish they had help with a specific domain (AWS, testing, deployment, etc.)
* Asks about extending Kiro's capabilities with Powers or MCP servers

## What is the KiroHub CLI?

The KiroHub CLI (`npx kirohub`) is the package manager for Kiro resources. Resources are modular packages that extend Kiro's capabilities with specialized knowledge, workflows, and tools.

**Key commands:**
* `npx kirohub search [query]` - Search for resources by keyword
* `npx kirohub search [query] --type <type>` - Filter by type (Steering, Hook, Power, Prompt, Agent, Skill)
* `npx kirohub add <slug>` - Install a resource by its slug

**Browse resources at:** [https://kirohub.dev](https://kirohub.dev)

## How to Help Users Find Resources

### Step 1: Understand What They Need

When a user asks for help with something, identify:
1. The domain (e.g., AWS CDK, React, testing, security)
2. The specific task (e.g., writing infrastructure, code review, deployment)
3. The resource type that best fits (Steering for guidance, Hook for automation, Power for tools)

### Step 2: Search for Resources

Run the search command with a relevant query:

```
npx kirohub search [query]
```

For example:
* User asks "how do I structure my CDK project?" → `npx kirohub search "aws cdk" --type Steering`
* User asks "can you help with code reviews?" → `npx kirohub search "code review"`
* User asks "I need an MCP server for GitHub" → `npx kirohub search "github" --type Power`

### Step 3: Present Options to the User

When you find relevant resources, present them with:
1. The resource name and what it does
2. The type (Steering, Hook, Power, Prompt, Agent, Skill)
3. The install command
4. A link to learn more on kirohub.dev

Example response:

```
I found a resource that might help! The "aws-cdk-best-practices" steering file
provides comprehensive CDK development patterns and conventions.

To install it:
npx kirohub add aws/aws-cdk-best-practices

Learn more: https://kirohub.dev/r/aws/aws-cdk-best-practices
```

### Step 4: Offer to Install

If the user wants to proceed, install the resource for them:

```
npx kirohub add <slug>
```

## Resource Types

When searching, consider which type best fits the user's need:

| Type | Description | Best For |
|------|-------------|----------|
| Steering | Markdown files providing context and instructions to Kiro | Coding standards, architecture guidance, best practices |
| Hook | Agent hooks triggered by IDE events | Automating repetitive tasks on file save, message send |
| Power | Bundled MCP servers + steering files | Adding tool capabilities (GitHub, AWS, databases) |
| Prompt | Reusable CLI prompts for Kiro CLI | Common workflows like code review, debugging, planning |
| Agent | Specialized agent configurations | Domain-specific expertise (security, architecture) |
| Skill | Composable skill packages | Multi-step workflows and specialized knowledge |

## Common Search Categories

| Category | Example Queries |
|----------|----------------|
| Cloud & Infrastructure | aws, cdk, terraform, serverless, lambda |
| Web Development | react, nextjs, typescript, tailwind, vite |
| Testing | testing, jest, playwright, e2e, unit-test |
| DevOps | deploy, docker, ci-cd, github-actions |
| Code Quality | review, lint, refactor, best-practices |
| Security | security, owasp, auth, iam |
| Documentation | docs, readme, api-docs, changelog |
| AI & Agents | mcp, agent, llm, prompt-engineering |

## Tips for Effective Searches

1. **Use specific keywords**: "aws cdk patterns" is better than just "aws"
2. **Filter by type**: Add `--type Steering` to narrow results
3. **Try alternative terms**: If "deploy" doesn't work, try "deployment" or "ci-cd"
4. **Check popular resources**: Sort by downloads on kirohub.dev to find community favorites

## When No Resources Are Found

If no relevant resources exist:
1. Acknowledge that no existing resource was found
2. Offer to help with the task directly using your general capabilities
3. Suggest the user could submit their own resource at kirohub.dev

Example:

```
I searched for resources related to "xyz" but didn't find any matches.
I can still help you with this task directly! Would you like me to proceed?

If this is something you do often, you could create and share your own resource
at https://kirohub.dev — click "Submit Resource" to contribute.
```
