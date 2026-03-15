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

### Current focus

- **AI / ML:** LLM application patterns, RAG architectures, intelligent production automation
- **Developer Tooling:** self-healing systems, workflow orchestration, reducing friction at scale
- **AI Agent Infrastructure:** building autonomous dev agents that handle the full lifecycle from issue to PR

---

### AI Agent Infrastructure

I built and operate an autonomous agent network that functions as a one-person software team.

**The journey:** I first built a custom Agent Orchestrator that could react to GitHub events, manage Telegram communication, and coordinate coding tasks across multiple repositories. After proving the concept, I migrated to [Spacebot](https://github.com/AgenDev/spacebot), a Rust-based agentic system, and built a heavily customized layer on top — including a dynamic project registry, GitHub App integration, and Tailscale Funnel for secure webhook delivery.

**What it does today:**

```
 ┌─────────────────────────────────────────────────────────────┐
 │  GitHub App (org-wide webhooks)                             │
 │  issues · PRs · CI · reviews · comments · push             │
 └────────────────────────┬────────────────────────────────────┘
                          ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  Tailscale Funnel (HTTPS, zero open ports)                  │
 └────────────────────────┬────────────────────────────────────┘
                          ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  Dedicated Server                                           │
 │                                                             │
 │  ┌─────────────────┐  ┌──────────────────────────────────┐  │
 │  │ Project Registry │  │ AI Agent                         │  │
 │  │                  │  │                                  │  │
 │  │ auto-discover    │  │ explore codebase                 │  │
 │  │ auto-clone       │──▶ write PRD                        │  │
 │  │ track repos      │  │ assess complexity                │  │
 │  │ notify Telegram  │  │ create worktree                  │  │
 │  └─────────────────┘  └───────────┬──────────────────────┘  │
 │                                   ▼                         │
 │           ┌───────────────────────────────────────┐         │
 │           │ Workers (isolated git worktrees)       │         │
 │           │                                        │         │
 │           │ simple ──▶ 1 worker implements         │         │
 │           │ complex ──▶ plan → implement           │         │
 │           └───────────────────┬───────────────────┘         │
 │                               ▼                             │
 │           ┌───────────────────────────────────────┐         │
 │           │ PR ──▶ CI ──▶ Review ──▶ Merge        │         │
 │           │  │                          │         │         │
 │           │  └── fix worker ◀── fail    │         │         │
 │           │  └── revision ◀── feedback  │         │         │
 │           │  └── cleanup ◀── merged ────┘         │         │
 │           └───────────────────────────────────────┘         │
 └─────────────────────────────────────────────────────────────┘
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
