# Kiro Prompt Pack

A collection of 12 reusable prompts and 247 agents for the [Kiro CLI](https://kiro.dev/cli/).

## Installation

### Option 1: Clone for a single project (local prompts)

```bash
# In your project root
git clone https://github.com/llamojha/kiro-prompts.git .kiro-prompts-temp
cp -r .kiro-prompts-temp/.kiro/prompts .kiro/prompts
rm -rf .kiro-prompts-temp
```

### Option 2: Install globally (available in all projects)

```bash
git clone https://github.com/llamojha/kiro-prompts.git
cp -r kiro-prompts/.kiro/prompts ~/.kiro/prompts
rm -rf kiro-prompts
```

### Option 3: Cherry-pick individual prompts

```bash
# Copy just the prompts you want
curl -o ~/.kiro/prompts/code-review.md https://raw.githubusercontent.com/llamojha/kiro-prompts/main/.kiro/prompts/code-review.md
```

## Usage

In Kiro CLI chat, invoke any prompt with `@prompt-name`:

```bash
@code-review
@security-checklist
@debug-helper
```

## Prompts

### commit-message

Generate a commit message for staged changes.

- **Input:** Auto-scans git staged changes
- **Format:** Conventional Commits (feat/fix/docs/style/refactor/test/chore)
- **Output:** One-line summary (max 72 chars), optional body for complex changes

---

### code-review

Review staged changes for correctness, security, reliability, readability, and test coverage.

- **Input:** Auto-scans git staged changes
- **Output:** Issues with severity, location, problem description, and fix suggestions

---

### mock-testing

Generate a test plan with mocks/stubs strategy and sample tests.

- **Input:** Paste code or reference with @filename
- **Framework:** Auto-detects from project config (package.json, pyproject.toml). Asks if not found.
- **Output:** Test plan, mocking strategy, and working test implementations

---

### daily-next-step

Summarize current status and output next actions for today.

- **Input:** Auto-scans `.kiro/specs/` and `TODO.md`
- **Output:** Status summary (done/blocked/in-progress) and 1-3 concrete next actions

---

### security-checklist

Security-focused review of staged changes.

- **Input:** Auto-scans git staged changes
- **Reviews:** Secrets, auth/authz, input validation, least privilege, sensitive data logging, dependency risks
- **Output:** Findings with risk level and mitigation recommendations

---

### debug-helper

Debug helper for errors, stack traces, and logs.

- **Input:** Paste error, or auto-scans terminal output and log files (`*.log`, `logs/`, `.kiro/logs/`, `tmp/`)
- **Output:** Likely root causes, clarifying questions, debugging actions, safe fix with rollback notes

---

### prompt-builder

Turn a rough goal into a polished, reusable prompt.

- **Input:** Describe your rough goal or idea
- **Output:** Clarifying questions, then a polished prompt with clear objective, constraints, and output format

---

### refactor-code

Refactor staged changes for clarity, structure, and performance.

- **Input:** Auto-scans git staged changes
- **Output:** List of changes with rationale, before/after diff, verification steps

---

### generate-documentation

Generate documentation for code.

- **Input:** Reference file/folder with @filename, paste code, or say "staged changes"
- **Doc style:** Auto-detects (JSDoc, docstrings, etc.) or specify preferred format
- **Output:** Overview, API docs, examples, edge cases and gotchas

---

### codebase-search

Find or change code in the codebase.

- **Input:** Describe what you want to find or change
- **Output:** Search targets (symbols, patterns, regex), likely locations, step-by-step execution plan

---

### seo-meta-sitemap-robots

Generate or improve SEO and crawler assets.

- **Input:** Auto-scans existing SEO files. Asks for URL if not found.
- **Output:** Social tags (Open Graph/Twitter), sitemap.xml, robots.txt, llms.txt with exact file edits

---

### refresh-foundational-steering-and-docs

Refresh foundational steering documents and docs.

- **Input:** Auto-scans `.kiro/steering/`, `docs/`, and `README.md`
- **Output:** Audit of outdated guidance, revised structure, updated conventions, PR checklist

## Quick Reference

| Prompt | Input | Description |
|--------|-------|-------------|
| `commit-message` | Auto: staged changes | Generate conventional commit message |
| `code-review` | Auto: staged changes | Review for correctness, security, reliability, readability |
| `mock-testing` | Code input | Generate test plan with mocks/stubs |
| `daily-next-step` | Auto: specs + TODO.md | Status summary and next actions |
| `security-checklist` | Auto: staged changes | Security review |
| `debug-helper` | Paste or auto: logs | Root cause analysis and fix suggestions |
| `prompt-builder` | Describe goal | Turn rough goals into polished prompts |
| `refactor-code` | Auto: staged changes | Refactor with before/after diff |
| `generate-documentation` | File, paste, or staged | Generate docs |
| `codebase-search` | Describe target | Search targets and execution plan |
| `seo-meta-sitemap-robots` | Auto or URL input | SEO and crawler assets |
| `refresh-foundational-steering-and-docs` | Auto: steering + docs | Refresh steering docs |

## Agents

247 agents converted to Kiro format. Switch agents with `/agent <name>`.

### Sources

| Source | Count | Description |
|--------|-------|-------------|
| [wshobson/agents](https://github.com/wshobson/agents) | 109 | Architecture, languages, DevOps, security, AI/ML, docs |
| [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) | 137 | Framework and technology experts |
| Custom | 1 | rubberduck |

### Agent List

<details>
<summary>Architecture & Design (15)</summary>

- `architect-review` - Architectural consistency review
- `backend-architect` - API design, microservices, database schemas
- `c4-code` - C4 code-level diagrams
- `c4-component` - C4 component diagrams
- `c4-container` - C4 container diagrams
- `c4-context` - C4 context diagrams
- `cloud-architect` - AWS/Azure/GCP infrastructure
- `database-architect` - Schema design, technology selection
- `design-system-architect` - Design system architecture
- `dotnet-architect` - .NET architecture
- `event-sourcing-architect` - Event sourcing patterns
- `graphql-architect` - GraphQL API design
- `hybrid-cloud-architect` - Multi-cloud architecture
- `kubernetes-architect` - Kubernetes architecture
- `monorepo-architect` - Monorepo structure

</details>

<details>
<summary>Languages (47)</summary>

- `bash-expert`, `bash-pro` - Bash scripting
- `c-expert`, `c-pro` - C programming
- `clojure-expert` - Clojure
- `cpp-expert`, `cpp-pro` - C++
- `csharp-expert`, `csharp-pro` - C#
- `dart-expert` - Dart
- `elixir-expert`, `elixir-pro` - Elixir
- `erlang-expert` - Erlang
- `go-expert`, `golang-pro` - Go
- `haskell-expert`, `haskell-pro` - Haskell
- `java-expert`, `java-pro` - Java
- `javascript-expert`, `javascript-pro` - JavaScript
- `julia-pro` - Julia
- `kotlin-expert` - Kotlin
- `lua-expert` - Lua
- `ocaml-expert` - OCaml
- `perl-expert` - Perl
- `php-expert`, `php-pro` - PHP
- `posix-shell-pro` - POSIX shell
- `python-expert`, `python-pro` - Python
- `ruby-expert`, `ruby-pro` - Ruby
- `rust-expert`, `rust-pro` - Rust
- `scala-expert`, `scala-pro` - Scala
- `sql-expert`, `sql-pro` - SQL
- `swift-expert` - Swift
- `typescript-expert`, `typescript-pro` - TypeScript

</details>

<details>
<summary>Web Frameworks (32)</summary>

- `actix-expert` - Actix (Rust)
- `angular-expert`, `angularjs-expert` - Angular
- `aspnet-core-expert` - ASP.NET Core
- `astro-expert` - Astro
- `django-expert`, `django-pro` - Django
- `express-expert` - Express.js
- `fastapi-expert`, `fastapi-pro` - FastAPI
- `fastify-expert` - Fastify
- `fiber-expert` - Fiber (Go)
- `flask-expert` - Flask
- `gin-expert` - Gin (Go)
- `laravel-expert` - Laravel
- `nestjs-expert` - NestJS
- `nextjs-expert` - Next.js
- `phoenix-expert` - Phoenix (Elixir)
- `rails-expert` - Ruby on Rails
- `react-expert` - React
- `remix-expert` - Remix
- `solidjs-expert` - SolidJS
- `spring-boot-expert` - Spring Boot
- `svelte-expert` - Svelte
- `vue-expert` - Vue.js

</details>

<details>
<summary>Mobile & Desktop (13)</summary>

- `android-expert` - Android
- `electron-expert` - Electron
- `expo-expert` - Expo
- `flutter-expert` - Flutter
- `ios-developer`, `ios-expert` - iOS
- `mobile-developer` - Mobile development
- `mobile-security-coder` - Mobile security
- `react-native-expert` - React Native
- `swiftui-expert` - SwiftUI
- `tauri-expert` - Tauri
- `unity-developer` - Unity

</details>

<details>
<summary>Databases (22)</summary>

- `cassandra-expert` - Cassandra
- `cockroachdb-expert` - CockroachDB
- `database-admin` - Database administration
- `database-optimizer` - Query optimization
- `dynamodb-expert` - DynamoDB
- `elasticsearch-expert` - Elasticsearch
- `knex-expert` - Knex.js
- `mariadb-expert` - MariaDB
- `mongodb-expert` - MongoDB
- `mongoose-expert` - Mongoose
- `mssql-expert` - MS SQL Server
- `mysql-expert` - MySQL
- `neo4j-expert` - Neo4j
- `opensearch-expert` - OpenSearch
- `postgres-expert` - PostgreSQL
- `prisma-expert` - Prisma
- `redis-expert` - Redis
- `sequelize-expert` - Sequelize
- `sqlite-expert` - SQLite
- `typeorm-expert` - TypeORM
- `vector-database-engineer`, `vector-db-expert` - Vector databases

</details>

<details>
<summary>DevOps & Infrastructure (24)</summary>

- `ansible-expert` - Ansible
- `circleci-expert` - CircleCI
- `deployment-engineer` - Deployment
- `devops-troubleshooter` - DevOps troubleshooting
- `docker-expert` - Docker
- `flyway-expert` - Flyway migrations
- `github-actions-expert` - GitHub Actions
- `gitlab-ci-expert` - GitLab CI
- `jenkins-expert` - Jenkins
- `kubernetes-expert` - Kubernetes
- `liquibase-expert` - Liquibase
- `pulumi-expert` - Pulumi
- `service-mesh-expert` - Service mesh
- `terraform-expert`, `terraform-specialist` - Terraform

</details>

<details>
<summary>Observability (8)</summary>

- `elk-expert` - ELK Stack
- `grafana-expert` - Grafana
- `loki-expert` - Loki
- `observability-engineer` - Observability
- `opentelemetry-expert` - OpenTelemetry
- `prometheus-expert` - Prometheus

</details>

<details>
<summary>Messaging & Queues (10)</summary>

- `bullmq-expert` - BullMQ
- `celery-expert` - Celery
- `kafka-expert` - Kafka
- `mqtt-expert` - MQTT
- `nats-expert` - NATS
- `rabbitmq-expert` - RabbitMQ
- `sidekiq-expert` - Sidekiq
- `sns-expert` - AWS SNS
- `sqs-expert` - AWS SQS

</details>

<details>
<summary>APIs & Protocols (10)</summary>

- `graphql-expert` - GraphQL
- `grpc-expert` - gRPC
- `openapi-expert` - OpenAPI
- `rest-expert` - REST APIs
- `trpc-expert` - tRPC
- `websocket-expert` - WebSocket

</details>

<details>
<summary>Auth & Security (12)</summary>

- `auth0-expert` - Auth0
- `backend-security-coder` - Backend security
- `frontend-security-coder` - Frontend security
- `jwt-expert` - JWT
- `keycloak-expert` - Keycloak
- `oauth-oidc-expert` - OAuth/OIDC
- `owasp-top10-expert` - OWASP Top 10
- `security-auditor` - Security auditing
- `threat-modeling-expert` - Threat modeling

</details>

<details>
<summary>AI & ML (10)</summary>

- `ai-engineer` - AI engineering
- `data-scientist` - Data science
- `langchain-expert` - LangChain
- `ml-engineer` - ML engineering
- `mlops-engineer` - MLOps
- `numpy-expert` - NumPy
- `openai-api-expert` - OpenAI API
- `pandas-expert` - Pandas
- `pytorch-expert` - PyTorch
- `scikit-learn-expert` - scikit-learn
- `tensorflow-expert` - TensorFlow

</details>

<details>
<summary>Testing (14)</summary>

- `ava-expert` - AVA
- `cypress-expert` - Cypress
- `jasmine-expert` - Jasmine
- `jest-expert` - Jest
- `mocha-expert` - Mocha
- `playwright-expert` - Playwright
- `puppeteer-expert` - Puppeteer
- `selenium-expert` - Selenium
- `tdd-orchestrator` - TDD orchestration
- `test-automator` - Test automation
- `testcafe-expert` - TestCafe
- `vitest-expert` - Vitest

</details>

<details>
<summary>Payments (3)</summary>

- `braintree-expert` - Braintree
- `payment-integration` - Payment integration
- `stripe-expert` - Stripe

</details>

<details>
<summary>Frontend & UI (10)</summary>

- `accessibility-expert` - Accessibility
- `css-expert` - CSS
- `frontend-developer` - Frontend development
- `html-expert` - HTML
- `jquery-expert` - jQuery
- `tailwind-expert` - Tailwind CSS
- `ui-designer` - UI design
- `ui-ux-designer` - UI/UX design
- `ui-visual-validator` - Visual validation
- `webpack-expert`, `rollup-expert` - Bundlers

</details>

<details>
<summary>Build Tools & Runtimes (4)</summary>

- `bun-expert` - Bun
- `deno-expert` - Deno
- `nodejs-expert` - Node.js

</details>

<details>
<summary>Documentation (5)</summary>

- `api-documenter` - API documentation
- `docs-architect` - Documentation architecture
- `mermaid-expert` - Mermaid diagrams
- `reference-builder` - Reference docs
- `tutorial-engineer` - Tutorials

</details>

<details>
<summary>Code Quality & Review (7)</summary>

- `code-reviewer` - Code review
- `conductor-validator` - Validation
- `context-manager` - Context management
- `debugger` - Debugging
- `error-detective` - Error analysis
- `legacy-modernizer` - Legacy code modernization
- `performance-engineer` - Performance optimization

</details>

<details>
<summary>SEO (10)</summary>

- `seo-authority-builder` - Authority building
- `seo-cannibalization-detector` - Cannibalization detection
- `seo-content-auditor` - Content auditing
- `seo-content-planner` - Content planning
- `seo-content-refresher` - Content refresh
- `seo-content-writer` - SEO writing
- `seo-keyword-strategist` - Keyword strategy
- `seo-meta-optimizer` - Meta optimization
- `seo-snippet-hunter` - Featured snippets
- `seo-structure-architect` - Site structure

</details>

<details>
<summary>Business & Other (15)</summary>

- `business-analyst` - Business analysis
- `content-marketer` - Content marketing
- `customer-support` - Customer support
- `dx-optimizer` - Developer experience
- `firmware-analyst` - Firmware analysis
- `hr-pro` - HR
- `incident-responder` - Incident response
- `legal-advisor` - Legal advice
- `malware-analyst` - Malware analysis
- `network-engineer` - Network engineering
- `prompt-engineer`, `prompter` - Prompt engineering
- `quant-analyst` - Quantitative analysis
- `reverse-engineer` - Reverse engineering
- `risk-manager` - Risk management
- `rubberduck` - Rubber duck debugging
- `sales-automator` - Sales automation
- `search-specialist` - Search
- `startup-analyst` - Startup analysis

</details>

## Contributing

Contributions welcome! Feel free to:
- Submit new prompts via PR
- Improve existing prompts
- Report issues

## License

MIT License - see [LICENSE](LICENSE) for details.
