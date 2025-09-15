# dotagent

**dotagent** is a lightweight, plug-and-play automation layer for developers.  
It helps you use your IDE (e.g. Cursor) and CLI together in a structured way, with intelligent task orchestration and context tracking.

## Features

- **Task Orchestration** — 10 built-in tasks for git workflow, README updates, brainstorming, and context management
- **Context Tracking** — Automatic project state tracking via `context/tracker.json` and structured context files
- **Resume where you left off** — Smart context checking and next-action suggestions
- **Git Integration** — Intelligent staging, diffing, and commit message generation
- **Brainstorming** — Convert raw ideas into structured specs with milestones and risks
- **README Sync** — Automatically update documentation based on staged changes

## Structure

- `tasks.json` — registry of 10 available tasks with examples and descriptions
- `prompts/` — detailed prompt templates for each task behavior (git_status, git_diff, brainstorm, etc.)
- `artifacts/` — outputs from tasks (git reports, summaries, generated content)
- `context/` — project context tracking (ideas, todos, progress tracker)
- `agent_prompt.md` — comprehensive system prompt to configure Cursor as a task orchestrator

## Quick start

1. Copy this repo or add as a submodule to your project
2. Open `agent_prompt.md` and paste it into Cursor as the **System prompt**
3. Try a task:
   - `/help` — see all available tasks
   - `/check_context` — analyze your project's current state
   - `/git_status` — check git status with intelligent parsing
   - `/update_readme` — sync README with staged changes (like this update!)
   - `/brainstorm <your idea>` — convert raw ideas into structured specs

## Available Tasks

See `tasks.json` for the complete registry, or run `/help` in chat. Key tasks include:

- **Context Management:** `check_context`, `brainstorm`, `next_to_do`, `update_to_do`
- **Git Workflow:** `git_status`, `git_diff`, `git_add`, `git_commit`
- **Documentation:** `update_readme`

## Context System

The `context/` directory tracks project state:

- `tracker.json` — structured metadata about project clarity and completeness
- `idea.md` — structured project specifications with milestones and risks
- `to_do.md` — session-based actionable task lists with priorities
