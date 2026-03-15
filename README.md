<h1 align="center">Marc Mantei</h1>

<p align="center">
  <strong>Senior Software Developer</strong><br>
  <sub>Systems architect · AI agent infrastructure · Code intelligence</sub>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/marcmantei/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://www.marcmantei.com"><img src="https://img.shields.io/badge/marcmantei.com-111?style=flat-square&logo=safari&logoColor=white" alt="Website" /></a>
  <a href="mailto:mail@marcmantei.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://www.imdb.com/name/nm15608082/"><img src="https://img.shields.io/badge/IMDb-F5C518?style=flat-square&logo=imdb&logoColor=000" alt="IMDb" /></a>
</p>

---

I design and build software infrastructure behind large-scale production — pipeline systems, workflow automation, and the developer tools that keep teams shipping. 10+ years across fullstack development, pipeline engineering, and ML/AI. Started as a Digital Artist, evolved through Pipeline TD into software architecture.

> Built key production tools for [Eyeline Studios'](https://eyelinestudios.com/en/studios/stages) virtual production stages — LED volumes, volumetric capture, and the Light Dome.

---

### What I'm building

<table>
<tr>
<td width="50%" valign="top">

#### <img src="https://img.shields.io/badge/🤖-111?style=flat-square" /> Spacebot Agent Network

A production autonomous agent system built on [Spacebot](https://github.com/AgenDev/spacebot) (Rust) that operates as a one-person software team.

```
  GitHub App (org-wide)
       │  webhooks
       ▼
  Tailscale Funnel (zero open ports)
       │
       ▼
  Agent ──▸ PRD ──▸ Plan ──▸ Implement ──▸ PR
    │                                       │
    │        ◂── fully autonomous ──▸       │
    │                                       │
    └── CI fix ◂── Review ◂── Merge ◂──────┘
```

**How it works:**
- GitHub App delivers webhooks via Tailscale Funnel (zero open ports)
- Dynamic Project Registry auto-discovers and auto-clones repos
- Agent writes structured PRD with acceptance criteria
- Complexity assessment routes to single or multi-worker flow
- Each worker gets an isolated git worktree for parallel execution
- CI failures auto-spawn fix workers, reviews trigger revisions

**Capabilities:**
- Org-wide GitHub App with secure Tailscale Funnel delivery
- Dynamic Project Registry: auto-discovers, auto-clones, tracks all repos
- Complexity-based routing: simple → direct, complex → plan + implement
- Image generation via Gemini with project-aware style extraction
- Cross-channel coordination: GitHub + Telegram + worker management
- Hot-reloadable config with daily automated backups

<sub>

`Spacebot (Rust)` · `Claude Opus / Haiku` · `Gemini Flash` · `Tailscale Funnel` · `GitHub App` · `SQLite` · `systemd`

</sub>

</td>
<td width="50%" valign="top">

#### <img src="https://img.shields.io/badge/🧬-111?style=flat-square" /> Mycelium

A code knowledge graph engine that transforms source code into a queryable, intelligent graph — built to give AI agents deep codebase understanding.

```
  Source Code
       │
  tree-sitter ──▸ Symbols + Relationships
       │
  LanceDB ──▸ Vector Embeddings (384-dim)
       │
  graphrs ──▸ Communities (Leiden algorithm)
       │
  DFS ──▸ Process Traces (execution flows)
       │
  ┌────┴────┐
  MCP    CLI    Cypher
```

**Core concepts:**
- **Symbols** — functions, classes, types extracted via tree-sitter
- **Communities** — cohesive modules detected via Leiden clustering
- **Processes** — execution flows traced from entry points via DFS
- **Impact analysis** — BFS through call graph from git diff changes

**Search modes:**
- BM25 keyword search · Vector semantic search · Hybrid RRF fusion

**6-crate workspace:**
`mycelium-core` · `mycelium-storage` · `mycelium-mcp` · `mycelium-cypher` · `mycelium-benchmarks` · `myc` CLI

<sub>

`Rust` · `tree-sitter` · `LanceDB` · `fastembed` · `graphrs` · `rmcp` · `Cypher dialect`

</sub>

</td>
</tr>
</table>

---

### Stack

<p>
  <img src="https://img.shields.io/badge/-Rust-B7410E?style=flat-square&logo=rust&logoColor=fff" />
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=fff" />
  <img src="https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=fff" />
  <img src="https://img.shields.io/badge/-Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=fff" />
  <img src="https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=000" />
  <img src="https://img.shields.io/badge/-Next.js-000?style=flat-square&logo=nextdotjs&logoColor=fff" />
  <img src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=fff" />
  <img src="https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=000" />
  <img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=fff" />
</p>

---

### Current focus

| Area | What I'm doing |
|------|---------------|
| **AI Agent Infra** | Autonomous dev agents handling the full lifecycle from issue to merged PR |
| **Code Intelligence** | Knowledge graph systems that give agents deep architectural understanding |
| **Developer Tooling** | Self-healing systems, workflow orchestration, reducing friction at scale |
| **LLM Engineering** | RAG architectures, model routing, structured output patterns |

---

### GitHub Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=github-dark-blue&hide_border=true&v=3" />
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=3" />
    <img alt="GitHub Streak" src="https://streak-stats.demolab.com?user=marcmantei&theme=default&hide_border=true&v=3" />
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-dark&hide_border=true&area=true&v=3" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=3" />
  <img alt="Contribution Graph" src="https://github-readme-activity-graph.vercel.app/graph?username=marcmantei&theme=github-light&hide_border=true&area=true&v=3" width="100%" />
</picture>
