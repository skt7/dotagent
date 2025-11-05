# Dotagent Directory Structure

Complete architecture documentation for the dotagent repository.

## Overview

When users install dotagent, this repository becomes their `.dotagent/` directory:

```
user-project/
├── .dotagent/          # ← This repo
│   ├── commands/       # Command definitions (flat)
│   ├── work/           # User's workspace
│   ├── agent_prompt.md # System prompt
│   ├── context.json    # Project context
│   └── setup.sh        # Installation script
├── .cursor/            # Created by setup.sh
│   ├── rules/
│   │   └── dotagent.mdc  # Agent prompt (copy)
│   └── commands/         # All commands (copies)
├── src/
├── README.md
└── ...
```

---

## Directory Structure

### `commands/` - Command Definitions (Flat Structure)

All commands are flat `.md` files. Cursor requires this structure for command discovery.

```
commands/
├── git_status.md         # → /git_status
├── git_diff.md           # → /git_diff
├── git_add.md            # → /git_add
├── git_commit.md         # → /git_commit
├── git_create_branch.md  # → /git_create_branch
├── git_sync.md           # → /git_sync
├── tasks_add.md          # → /tasks_add
├── tasks_update.md       # → /tasks_update
├── tasks_next.md         # → /tasks_next
├── issues_report.md      # → /issues_report
├── issues_log_gap.md     # → /issues_log_gap
├── issues_describe.md    # → /issues_describe
├── issues_solve.md       # → /issues_solve
├── issues_close.md       # → /issues_close
├── ideas_brainstorm.md   # → /ideas_brainstorm
├── ideas_capture.md      # → /ideas_capture
├── sessions_summarize.md # → /sessions_summarize
├── project_check.md      # → /project_check
├── project_readme.md     # → /project_readme
└── help.md               # → /help
```

**Total: 20 commands**

**Command Naming Convention:**
- Pattern: `{category}_{name}.md` → `/{category}_{name}`
- Root commands: `{name}.md` → `/{name}`
- Examples:
  - `git_status.md` → `/git_status`
  - `tasks_add.md` → `/tasks_add`
  - `help.md` → `/help`

**Why Flat?**
- Cursor only discovers commands in flat structure
- Subdirectories (`commands/git/status.md`) don't work
- Prefixes provide categorization (`git_`, `tasks_`, etc.)

---

### `work/` - User's Workspace

Where dotagent stores and manages all user content. Each subdirectory contains a `templates/` folder with clean starter files.

```
work/
├── tasks/                # Development todos & task lists
│   ├── templates/
│   │   └── todo.md       # Task list template (singular)
│   └── todo.md           # User's actual task file (created by commands)
│
├── issues/               # Bug reports & gap tracking
│   ├── templates/
│   │   ├── bug.md        # Bug template (singular)
│   │   └── gap.md        # Gap log template (singular)
│   ├── BUG-001.md        # Individual bug files
│   ├── BUG-002.md
│   └── gap.md            # Gap log (created by commands)
│
├── ideas/                # Project ideas & feature specs
│   ├── templates/
│   │   └── idea.md       # Idea template (singular)
│   └── idea.md           # User's idea file (created by commands)
│
├── notes/                # General notes & documentation
│   ├── templates/
│   │   └── note.md       # Note template (singular)
│   └── *.md              # User's note files
│
├── sessions/             # Session logs & tracking
│   ├── templates/
│   │   └── session.md    # Session template (singular)
│   └── session.md        # User's session log (created by commands)
│
└── docs/                 # Project specifications
    ├── templates/
    │   └── specification.md  # Spec template (singular)
    └── *.md              # User's spec files
```

**Template System:**
- Templates are **always singular** (`todo.md`, not `todos.md`)
- Commands **must read templates** before creating files
- Templates contain only placeholders and structure
- See `agent_prompt.md` section D.1 for template usage rules

---

### Root Files

```
.dotagent/
├── agent_prompt.md       # System prompt for Cursor (defines AI behavior)
├── context.json          # Project-wide context tracking
├── setup.sh              # User installation script
├── README.md             # Usage documentation
├── STRUCTURE.md          # This file
└── .gitignore            # Git ignore patterns
```

**`agent_prompt.md`** - Core system instructions:
- Defines how AI interprets commands
- Maps slash commands to files
- Enforces template usage
- Safety rules (no auto-commit, approval required)

**`context.json`** - Project metadata:
```json
{
  "project_name": "example",
  "description": "...",
  "tech_stack": [],
  "key_files": [],
  "current_focus": ""
}
```

**`setup.sh`** - Installation automation:
- Copies `agent_prompt.md` → `.cursor/rules/dotagent.mdc`
- Copies `commands/*.md` → `.cursor/commands/`
- Creates necessary directories

---

## Installation Flow

### For Users

```bash
# 1. Clone into project
git clone <repo-url> .dotagent

# 2. Run setup
cd .dotagent
./setup.sh

# 3. Restart Cursor
# Commands are now available!

# 4. Try it
/help
```

### What Setup Does

```
Before:                      After:
user-project/               user-project/
└── .dotagent/              ├── .dotagent/          (untouched)
    ├── commands/           └── .cursor/
    ├── work/                   ├── rules/
    ├── agent_prompt.md             └── dotagent.mdc  ✓ copied
    └── setup.sh                └── commands/
                                     ├── git_status.md  ✓ copied
                                     ├── tasks_add.md   ✓ copied
                                     └── ... (20 files)
```

---

## Command Categories

### 🔄 Git Operations (6 commands)
- `git_status` - Check repository status
- `git_diff` - Show detailed changes
- `git_add` - Stage files
- `git_commit` - Create conventional commits
- `git_create_branch` - Create and switch branch
- `git_sync` - Pull and push changes

**Safety:** Never auto-executes git commands, always shows what to run

### 📋 Task Management (3 commands)
- `tasks_add` - Add new development task
- `tasks_update` - Update or complete tasks
- `tasks_next` - Suggest next prioritized task

**Files:** `work/tasks/todo.md`

### 🐛 Issue Tracking (5 commands)
- `issues_report` - Report bug (creates BUG-XXX.md)
- `issues_log_gap` - Log feature gap or limitation
- `issues_describe` - Summarize bug details
- `issues_solve` - Generate fix plan
- `issues_close` - Mark bug as resolved

**Files:** `work/issues/BUG-*.md`, `work/issues/gap.md`

### 💡 Idea Management (2 commands)
- `ideas_brainstorm` - Structure raw idea into spec
- `ideas_capture` - Quick idea log with hotness tracking

**Files:** `work/ideas/idea.md`

### 📝 Session Tracking (1 command)
- `sessions_summarize` - Generate session summary from git changes

**Files:** `work/sessions/session.md`

### 📄 Project Context (2 commands)
- `project_check` - Review and update context.json
- `project_readme` - Generate/update README

**Files:** `context.json`, `README.md`

### ℹ️ Help (1 command)
- `help` - List all available commands

---

## Command-to-Template Mapping

| Command | Template Used | Output File(s) |
|---------|---------------|----------------|
| `/tasks_add` | `work/tasks/templates/todo.md` | `work/tasks/todo.md` |
| `/tasks_update` | (reads existing) | `work/tasks/todo.md` |
| `/tasks_next` | (reads existing) | (preview only) |
| `/issues_report` | `work/issues/templates/bug.md` | `work/issues/BUG-NNN.md` |
| `/issues_log_gap` | `work/issues/templates/gap.md` | `work/issues/gap.md` |
| `/issues_close` | (reads existing) | `work/issues/BUG-NNN.md` |
| `/ideas_brainstorm` | `work/ideas/templates/idea.md` | `work/ideas/idea.md` |
| `/ideas_capture` | `work/ideas/templates/idea.md` | `work/ideas/idea.md` |
| `/sessions_summarize` | `work/sessions/templates/session.md` | `work/sessions/session.md` |
| `/project_readme` | `work/docs/templates/specification.md` | `README.md` |

---

## Design Principles

1. **Flat Command Structure** - Cursor compatibility requires flat `commands/` directory
2. **Template-Driven** - All file creation uses templates for consistency
3. **User Workspace** - All managed content in `work/` subdirectories
4. **Safety First** - No auto-commits, no auto-execution, always preview
5. **Singular Naming** - Templates use singular names (`todo.md`, not `todos.md`)
6. **Category Prefixes** - Commands use `category_name` pattern for organization
7. **Copy, Don't Link** - Setup copies files to avoid bidirectional issues

---

## Adding New Commands

To add a new command:

1. **Create command file**: `commands/{category}_{name}.md`
2. **Update help.md**: Add to appropriate category
3. **Create template** (if needed): `work/{category}/templates/{name}.md`
4. **Update STRUCTURE.md**: Document the command
5. **Test**: Ensure command works in Cursor

Example:
```bash
# Add new research command
touch commands/research_add.md
# Edit file with Goal, Inputs, Behavior, Output
# Add to help.md under "Research" category
```

---

## Development vs Production

**In this repo (development):**
- Commands are in `commands/` (flat)
- Work templates in `work/*/templates/`
- Clean, no user data

**In user's project (production):**
- `.dotagent/` contains this repo
- `.cursor/` contains copies (setup.sh creates)
- `work/` contains actual user data

**Separation is key:** User can modify `.cursor/` commands without affecting `.dotagent/` repo.

---

## Testing

See `tests/README.md` for comprehensive testing documentation.

**Quick test:**
```bash
cd tests/
./setup_test_env.sh
cd dummy_project/
cursor test_plan.md
```

---

## Migration Guide

**From nested to flat structure:**

Old:
```
commands/git/status.md → /git_status
commands/tasks/add.md → /tasks_add
```

New:
```
commands/git_status.md → /git_status
commands/tasks_add.md → /tasks_add
```

No user-facing changes! Slash commands remain the same.

---

**For questions or contributions, see README.md**
