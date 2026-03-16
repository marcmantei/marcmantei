# Hey, I'm Marc

I started as a Digital Artist, built production pipelines for virtual production stages, and now I architect AI-powered developer infrastructure in Rust.

10+ years across the full arc — from creative tools and VFX pipelines to fullstack development, systems engineering, and AI agent orchestration. I build the systems that let small teams ship like large ones.

> Built key production tools for [Eyeline Studios'](https://eyelinestudios.com/en/studios/stages) virtual production stages — LED volumes, volumetric capture, and the Light Dome.

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

- **AI agent infrastructure** — autonomous dev agents that go from issue to merged PR
- **Code intelligence** — giving AI agents structural understanding of codebases before they write code
- **Developer tooling** — workflow orchestration, self-healing systems, reducing friction at scale

---

### AI Agent Infrastructure

I built and operate an autonomous agent network that functions as a one-person software team. I create GitHub issues, and the network handles PRD writing, implementation, CI fixes, and review responses — end to end, without intervention.

Built on a heavily customized [Spacebot](https://github.com/AgenDev/spacebot) fork (846+ commits) with a dynamic project registry, GitHub App with org-wide webhooks via Tailscale Funnel (zero open ports), and isolated git worktrees for parallel execution. The CI/CD pipeline alone has processed 7,300+ automated task commits since January 2025.

- Auto-generates structured PRDs before implementation begins
- Complexity-aware orchestration — simple tasks get one worker, complex tasks get a planner + implementer
- Full PR lifecycle management: CI failure → auto-fix, review feedback → auto-revision
- Cross-channel coordination: GitHub webhooks, Telegram notifications, worker management

**Stack:** Spacebot (Rust) · Claude Opus/Haiku · Gemini Flash · Tailscale Funnel · GitHub App · SQLite · systemd

---

### Myceliums — Code Knowledge Graph

A code intelligence engine in Rust that parses source code into a queryable knowledge graph — so AI agents understand architecture before they write a single line. Published on [crates.io](https://crates.io/crates/myc).

Instead of letting agents grep through files and guess at structure, Myceliums gives them a structured graph: symbols, call chains, functional modules, and execution flows — all queryable through MCP, a CLI, or a custom Cypher dialect. One search call instead of fifty.

- 5-crate Rust workspace (~8,600 lines) — core, storage, MCP server, Cypher engine, benchmarks
- Parses TypeScript, JavaScript, and Python via tree-sitter with two-pass symbol resolution
- Hybrid search: BM25 keyword + vector semantic + Reciprocal Rank Fusion
- Impact analysis: parses git diffs, then BFS through the call graph to find blast radius
- MCP server with 11 tools and 8 resources for direct AI agent integration

**Stack:** Rust · tree-sitter · LanceDB · fastembed · graphrs · rmcp · Cypher dialect

---

### What I work with

![Rust](https://img.shields.io/badge/-Rust-555?style=flat-square&logo=rust&logoColor=fff)
![Python](https://img.shields.io/badge/-Python-555?style=flat-square&logo=python&logoColor=fff)
![TypeScript](https://img.shields.io/badge/-TypeScript-555?style=flat-square&logo=typescript&logoColor=fff)
![Bash](https://img.shields.io/badge/-Bash-555?style=flat-square&logo=gnubash&logoColor=fff)
![React](https://img.shields.io/badge/-React-555?style=flat-square&logo=react&logoColor=fff)
![Next.js](https://img.shields.io/badge/-Next.js-555?style=flat-square&logo=nextdotjs&logoColor=fff)
![Docker](https://img.shields.io/badge/-Docker-555?style=flat-square&logo=docker&logoColor=fff)
![Linux](https://img.shields.io/badge/-Linux-555?style=flat-square&logo=linux&logoColor=fff)
![Git](https://img.shields.io/badge/-Git-555?style=flat-square&logo=git&logoColor=fff)
