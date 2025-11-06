# dotagent

**dotagent** is a lightweight, command-driven automation layer for developers using Cursor IDE.  
It provides 20+ structured commands for task management, bug tracking, idea brainstorming, git workflow, and context management—all integrated directly into your development workflow.

## Features

- **📋 Task Management** — Add, update, and prioritize development todos with effort/priority tracking
- **🐛 Issue Tracking** — Report bugs, log gaps, and manage resolutions with structured markdown files
- **💡 Idea Management** — Brainstorm and capture ideas with hotness tracking and structured specs
- **📝 Session Logging** — Automatically summarize work sessions from git diffs
- **🔄 Git Integration** — Intelligent git commands that never auto-execute (safety first!)
- **📄 Documentation Sync** — Update README and context based on your actual changes
- **🎯 Context Tracking** — Centralized project context in `context.json`

## Quick Start

### 1. Install
```bash
# Clone into your project as .dotagent/
git clone https://github.com/skt7/dotagent.git .dotagent

# Or add as submodule
git submodule add https://github.com/skt7/dotagent.git .dotagent
```

### 2. Run Setup
```bash
cd .dotagent
./setup.sh
```

This automatically:
- Copies `agent_prompt.md` → `.cursor/rules/dotagent.mdc`
- Copies all commands → `.cursor/commands/`
- Sets up your Cursor environment

### 3. Try Commands
```
/help                  → See all available commands
/tasks_add            → Add a new todo
/issues_report        → Report a bug
/ideas_brainstorm     → Structure an idea
/git_status          → Check git status
/sessions_summarize  → Log your work session
```

## Available Commands

Run `/help` in chat for the complete list. Commands are organized by category:

### 📋 Tasks (3 commands)
- `/tasks_add` — Add new task to todo list
- `/tasks_update` — Update or complete existing tasks  
- `/tasks_next` — Get prioritized next actions

### 🐛 Issues (5 commands)
- `/issues_report` — Report a bug (creates BUG-XXX.md)
- `/issues_log_gap` — Log a gap or limitation
- `/issues_describe` — Summarize a bug
- `/issues_solve` — Generate fix plan
- `/issues_close` — Close/resolve a bug

### 💡 Ideas (2 commands)
- `/ideas_brainstorm` — Structure a raw idea into spec
- `/ideas_capture` — Quick idea log with hotness tracking

### 🔄 Git (6 commands)
- `/git_status`, `/git_diff`, `/git_add`, `/git_commit`, `/git_create_branch`, `/git_sync`
- **Note:** Git commands never auto-execute—they always show you what to run

### 📝 Sessions (1 command)
- `/sessions_summarize` — Log session summary from git diffs

### 📄 Project (2 commands)
- `/project_check` — Check and update context.json
- `/project_readme` — Update README from staged changes

### ℹ️ Root (1 command)
- `/help` — Show all available commands

## Directory Structure

```
.dotagent/
├── commands/          # 20 command definitions (flat structure)
│   ├── git_status.md       # /git_status
│   ├── git_commit.md       # /git_commit
│   ├── tasks_add.md        # /tasks_add
│   ├── issues_report.md    # /issues_report
│   ├── ideas_brainstorm.md # /ideas_brainstorm
│   ├── help.md             # /help
│   └── ... (14 more)
│
├── work/              # Your workspace (what dotagent manages)
│   ├── tasks/         # Your todos and task lists
│   │   └── templates/todo.md
│   ├── issues/        # Your bugs (BUG-XXX.md) and gaps
│   │   └── templates/{bug.md, gap.md}
│   ├── ideas/         # Your ideas and specs
│   │   └── templates/idea.md
│   ├── notes/         # Your notes and documentation
│   │   └── templates/note.md
│   └── sessions/      # Your session logs
│       └── templates/session.md
│
├── agent_prompt.md    # System prompt for Cursor
├── context.json       # Project-wide context tracking
└── README.md          # This file
```

## How It Works

1. **Commands** are markdown files in `commands/` that define behavior
2. **Templates** in `work/*/templates/` provide starter structures
3. **Your data** lives in `work/` subdirectories (tasks, issues, ideas, etc.)
4. **Agent prompt** tells Cursor how to execute commands
5. **Commands always preview** before writing—you stay in control!

## Workflow Example

```bash
# Start a new feature
/tasks_add
> "Implement user authentication @priority:high @effort:medium"
> confirm

# Hit a bug
/issues_report  
> Title: "Login fails with empty password"
> Steps: "1. Go to /login  2. Submit empty form"
> confirm
# → Creates work/issues/BUG-001.md

# Brainstorm solution
/ideas_brainstorm
> "Add client-side validation before API call"
> confirm

# End of session
/sessions_summarize
> Paste git status and diff
> confirm
# → Logs to work/sessions/session.md
```

## Safety First

- ✅ **Preview/Confirm** — All write operations show preview and require explicit `confirm`
- ✅ **No Auto-Commits** — Git commands never auto-execute, they suggest commands for you to run
- ✅ **Templates** — Commands use templates (which you can customize) instead of hardcoding structures
- ✅ **Read-Only by Default** — Most commands are read-only analysis

## Customization

### Custom Templates
Edit any template in `work/*/templates/` and commands will use your version:
```bash
# Customize task format
vim .dotagent/work/tasks/templates/todo.md

# All /tasks_add commands now use your format!
```

### Version Control
You can:
- ✅ Track `.dotagent/` in git (recommended) — your whole team uses same commands
- ✅ Track `work/` in git — share tasks/bugs/ideas with team
- ❌ Gitignore `.dotagent/` — keep commands local to your machine

## Requirements

- Cursor IDE
- Git (for git commands)
- Nothing else! It's just markdown files.

## Philosophy

**dotagent** follows these principles:

1. **Transparency** — You see exactly what will happen before it happens
2. **Control** — Commands never auto-execute destructive actions
3. **Simplicity** — Just markdown files and directory structure
4. **Extensibility** — Easy to add custom commands and templates
5. **Safety** — Preview/confirm workflow for all mutations

## License

See [LICENSE](LICENSE) file.

---

**Ready to be more organized?** Run `/help` and start commanding your workflow! 🚀
