# Hey, I'm Marc

**Senior Software Developer**

I design and build the software infrastructure behind large-scale production:<br>
pipeline systems, workflow automation, and the developer tools that keep creative teams shipping.

10+ years across fullstack development, pipeline engineering, and ML/AI.<br>
Started as a Digital Artist, evolved through Pipeline TD into software architecture.

> Developed key production tools for [Eyeline Studios'](https://eyelinestudios.com/en/studios/stages) virtual production stages,<br>
> including LED volumes, volumetric capture, and the Light Dome.

---

### What I work with

![Python](https://img.shields.io/badge/-Python-555?style=flat-square&logo=python&logoColor=fff)
![TypeScript](https://img.shields.io/badge/-TypeScript-555?style=flat-square&logo=typescript&logoColor=fff)
![Bash](https://img.shields.io/badge/-Bash-555?style=flat-square&logo=gnubash&logoColor=fff)
![React](https://img.shields.io/badge/-React-555?style=flat-square&logo=react&logoColor=fff)
![Next.js](https://img.shields.io/badge/-Next.js-555?style=flat-square&logo=nextdotjs&logoColor=fff)
![Docker](https://img.shields.io/badge/-Docker-555?style=flat-square&logo=docker&logoColor=fff)
![Linux](https://img.shields.io/badge/-Linux-555?style=flat-square&logo=linux&logoColor=fff)
![Git](https://img.shields.io/badge/-Git-555?style=flat-square&logo=git&logoColor=fff)

---

### Let's connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcmantei/)
[![Website](https://img.shields.io/badge/marcmantei.com-555?style=flat&logo=safari&logoColor=white)](https://www.marcmantei.com)
[![Email](https://img.shields.io/badge/mail@marcmantei.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:mail@marcmantei.com)
[![IMDb](https://img.shields.io/badge/IMDb-F5C518?style=flat&logo=imdb&logoColor=000)](https://www.imdb.com/name/nm15608082/)

---

### GitHub Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=github-dark-blue&hide_border=true&v=2" />
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=2" />
    <img alt="GitHub Streak" src="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=2" />
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-dark&hide_border=true&area=true&v=2" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=2" />
  <img alt="Contribution Graph" src="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=2" width="100%" />
</picture>

---

### Current focus

- **AI / ML:** LLM application patterns, RAG architectures, intelligent production automation
- **Developer Tooling:** self-healing systems, workflow orchestration, reducing friction at scale
- **AI Agent Infrastructure:** building autonomous dev agents that handle the full lifecycle from issue to PR

---

### AI Agent Infrastructure

I built and operate an autonomous agent network that functions as a one-person software team.

**The journey:** I first built a custom Agent Orchestrator that could react to GitHub events, manage Telegram communication, and coordinate coding tasks across multiple repositories. After proving the concept, I migrated to [Spacebot](https://github.com/AgenDev/spacebot), a Rust-based agentic system, and built a heavily customized layer on top — including a dynamic project registry, GitHub App integration, and Tailscale Funnel for secure webhook delivery.

**What it does today:**

```mermaid
graph TD
    GH["<b>GitHub App</b> (org-wide)<br/>issues · PRs · CI · reviews · push"]
    TS["<b>Tailscale Funnel</b><br/>HTTPS · zero open ports"]
    GH -- webhooks --> TS

    subgraph SERVER ["Dedicated Server"]
        direction TB

        subgraph INTAKE [" "]
            direction LR
            REG["<b>Project Registry</b><br/>auto-discover<br/>auto-clone<br/>track repos<br/>notify Telegram"]
            AGENT["<b>AI Agent</b><br/>read issue + codebase<br/>write structured PRD<br/>assess complexity<br/>create git worktree"]
            REG -- "new event" --> AGENT
        end

        subgraph WORK ["Workers (isolated git worktrees)"]
            direction LR
            SIMPLE["simple task → 1 worker"]
            COMPLEX["complex task → planner + implementer"]
        end

        subgraph LIFECYCLE ["PR Lifecycle"]
            direction LR
            PR["PR"] --> CI["CI"] --> REVIEW["Review"] --> MERGE["Merge"]
            CI -. "fail" .-> FIX["fix worker"]
            REVIEW -. "feedback" .-> REV["revision worker"]
            MERGE -. "merged" .-> CLEAN["cleanup"]
        end

        INTAKE --> WORK --> LIFECYCLE
    end

    TS --> SERVER
```

**Key capabilities:**
- GitHub App with org-wide webhook delivery via Tailscale Funnel (zero open ports)
- Dynamic Project Registry: auto-discovers, auto-clones, and tracks all repos
- Enriches issues with auto-generated PRDs before implementation
- Isolated git worktrees enable parallel workers on the same project
- Complexity-based orchestration (sequential planning + implementation for complex tasks)
- Image generation via Gemini API with on-the-fly style extraction from project code
- Cross-channel coordination: GitHub webhooks, Telegram notifications, worker management
- Hot-reloadable config with daily automated backups

**Stack:** Spacebot (Rust) · Claude Opus/Haiku · Gemini Flash · Tailscale Funnel · GitHub App · SQLite · systemd

This setup lets me operate like a small software company: I create issues, and the agent network handles PRD writing, implementation, CI fixes, and review responses autonomously.

---

### Code Knowledge Graph

I built a code intelligence engine in Rust that parses source code into a queryable knowledge graph — giving AI agents deep architectural understanding of any codebase before they write a single line.

**The idea:** AI agents waste tokens and make poor decisions when they don't understand how a codebase fits together. Instead of letting them grep around blindly, I built a system that pre-analyzes code structure — extracting symbols, mapping call relationships, detecting functional modules, and tracing execution flows — then exposes it all through MCP, a CLI, and a custom Cypher query engine.

**How it works:**

```mermaid
graph TD
    SRC["<b>Source Code</b><br/>TypeScript · JavaScript · Python"]
    SRC -- "tree-sitter" --> EXTRACT

    subgraph EXTRACT ["Symbol Extraction"]
        direction TB
        P1["Pass 1: parse all files → extract symbols<br/>functions · classes · methods · types · interfaces"]
        P2["Pass 2: resolve calls → map relationships"]
        P1 --> P2
    end

    EXTRACT --> VEC & COM & PROC

    subgraph ANALYSIS [" "]
        direction LR
        VEC["<b>Vector Embeddings</b><br/>384-dim via fastembed<br/>stored in LanceDB<br/>semantic similarity"]
        COM["<b>Community Detection</b><br/>Leiden algorithm<br/>clusters coupled symbols<br/>into functional modules"]
        PROC["<b>Process Tracing</b><br/>detect entry points<br/>DFS through call graph<br/>trace execution flows"]
    end

    ANALYSIS --> QUERY

    subgraph QUERY ["Query Layer"]
        direction LR
        MCP["<b>MCP Server</b><br/>11 tools · 8 resources<br/>stdio transport"]
        CLI["<b>CLI</b><br/>analyze · search<br/>impact · communities"]
        CYP["<b>Cypher Engine</b><br/>MATCH patterns<br/>WHERE filters<br/>graph traversal"]
    end
```

**Key capabilities:**
- Parses TypeScript, JavaScript, and Python via tree-sitter with two-pass symbol resolution
- Hybrid search: BM25 keyword + vector semantic + Reciprocal Rank Fusion
- Community detection via Leiden algorithm — surfaces functional modules automatically
- Impact analysis: parses git diffs, then BFS through the call graph to find blast radius
- Symbol rename with full cross-reference resolution and preview before applying
- MCP server with 11 tools and 8 resources for direct AI agent integration
- Custom Cypher dialect for graph traversal queries (read-only, no write operations)

**Stack:** Rust · tree-sitter · LanceDB · fastembed · graphrs · rmcp · Cypher dialect

The engine is structured as a 6-crate Rust workspace — core analysis, storage, MCP server, Cypher engine, benchmarks, and a CLI — designed to be embedded into AI developer tools or run standalone.
