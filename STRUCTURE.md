# Dotagent Directory Structure

Complete architecture documentation for the dotagent repository.

## Overview

When users install dotagent, this repository becomes their `.dotagent/` directory:

```
user-project/
├── .dotagent/          # ← This repo
│   ├── commands/       # Command definitions  
│   ├── work/           # User's workspace
│   ├── agent_prompt.md
│   └── context.json
├── src/
├── README.md
└── ...
```

---

## Directory Structure

### `commands/` - Command Definitions

Commands are organized by category. Each `.md` file defines a slash command.

```
commands/
├── git/                  # Git workflow (6 commands)
│   ├── status.md         # → /git_status
│   ├── diff.md           # → /git_diff
│   ├── add.md            # → /git_add
│   ├── commit.md         # → /git_commit
│   ├── create_branch.md  # → /git_create_branch
│   └── sync.md           # → /git_sync
│
├── tasks/                # Task management (3 commands)
│   ├── add.md            # → /tasks_add
│   ├── update.md         # → /tasks_update
│   └── next.md           # → /tasks_next
│
├── issues/               # Bug/gap tracking (5 commands)
│   ├── report.md         # → /issues_report
│   ├── log_gap.md        # → /issues_log_gap
│   ├── describe.md       # → /issues_describe
│   ├── solve.md          # → /issues_solve
│   └── close.md          # → /issues_close
│
├── ideas/                # Idea management (2 commands)
│   ├── brainstorm.md     # → /ideas_brainstorm
│   └── capture.md        # → /ideas_capture
│
├── sessions/             # Session logging (1 command)
│   └── summarize.md      # → /sessions_summarize
│
├── project/              # Project-wide (2 commands)
│   ├── check.md          # → /project_check
│   └── readme.md         # → /project_readme
│
└── help.md               # → /help (root-level command)
```

**Command Naming Convention:**
- Subdirectory: `commands/{category}/{name}.md` → `/{category}_{name}`
- Root level: `commands/{name}.md` → `/{name}`

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
└── sessions/             # Session logs & tracking
    ├── templates/
    │   └── session.md    # Session log template (singular)
    └── session.md        # User's session log (created by commands)
```

**Key Principles:**
- **Templates are singular:** `todo.md`, `bug.md`, `idea.md` (not plural)
- **Working files match templates:** Commands create files using template names
- **Templates/** Only contain placeholders, never actual data
- **Templates are customizable:** Users can edit without changing commands

---

### Root Files

| File | Purpose |
|------|---------|
| `agent_prompt.md` | System prompt for Cursor IDE (configure as Cursor Rule) |
| `context.json` | Project-wide context and tracking stats |
| `README.md` | Getting started guide and feature overview |
| `STRUCTURE.md` | This file—architecture documentation |
| `LICENSE` | License information |
| `.gitignore` | Files to ignore in version control |

---

## Command → Template → File Mapping

Complete mapping of which commands use which templates and create which files:

| Command | Reads Template | Creates/Updates File |
|---------|---------------|---------------------|
| **Tasks** |||
| `/tasks_add` | `work/tasks/templates/todo.md` | `work/tasks/todo.md` |
| `/tasks_update` | `work/tasks/templates/todo.md` | `work/tasks/todo.md` |
| `/tasks_next` | `work/tasks/templates/todo.md` | Suggests tasks (reads existing) |
| **Issues** |||
| `/issues_report` | `work/issues/templates/bug.md` | `work/issues/BUG-XXX.md` (new file each time) |
| `/issues_log_gap` | `work/issues/templates/gap.md` | `work/issues/gap.md` |
| `/issues_describe` | - | Reads `work/issues/BUG-XXX.md` (read-only) |
| `/issues_solve` | - | Reads `work/issues/BUG-XXX.md` (read-only) |
| `/issues_close` | - | Updates `work/issues/BUG-XXX.md` |
| **Ideas** |||
| `/ideas_brainstorm` | `work/ideas/templates/idea.md` | `work/ideas/idea.md` |
| `/ideas_capture` | `work/ideas/templates/idea.md` | `work/ideas/idea.md` |
| **Sessions** |||
| `/sessions_summarize` | `work/sessions/templates/session.md` | `work/sessions/session.md` |
| **Project** |||
| `/project_check` | - | Updates `context.json` (root level) |
| `/project_readme` | - | Updates `README.md` (root level) |
| **Git** |||
| All git commands | - | Read-only or suggest commands (never auto-execute) |
| **Help** |||
| `/help` | - | Scans `commands/` and displays list |

---

## File Lifecycle

### Initial Setup
1. User installs dotagent as `.dotagent/` in their project
2. `work/` subdirectories are empty (only `templates/` exist)
3. First command invocation reads template and creates initial file

### Development Workflow
1. User runs command (e.g., `/tasks_add`)
2. Command checks if `work/tasks/todo.md` exists
3. If not, command reads `work/tasks/templates/todo.md` and uses its structure
4. Command generates content based on template + user input
5. Command shows preview and asks for `confirm`
6. On confirm, command writes file to `work/tasks/todo.md`

### Template Customization
1. User edits `work/tasks/templates/todo.md` with custom format
2. Future `/tasks_add` commands automatically use custom format
3. No need to modify command files—templates are the source of truth for structure

---

## Naming Conventions

### Consistent Singular Naming
All templates and default working files use **singular** names:

| Category | Template | Working File | Why Singular? |
|----------|----------|--------------|---------------|
| Tasks | `todo.md` | `todo.md` | Matches common usage "todo list" |
| Issues | `bug.md` | `BUG-XXX.md` | Individual bug files |
| Issues | `gap.md` | `gap.md` | Gap log is singular document |
| Ideas | `idea.md` | `idea.md` | Idea log is singular document |
| Notes | `note.md` | `*.md` | Template for creating notes |
| Sessions | `session.md` | `session.md` | Session log is singular document |

**Exception:** Bug files use `BUG-001.md`, `BUG-002.md` pattern (each bug is separate file)

---

## Version Control Strategy

### What to Track in Git

**Option 1: Track Everything (Recommended for Teams)**
```gitignore
# In project root .gitignore
# (nothing - track all of .dotagent/)
```
✅ Whole team uses same commands  
✅ Share tasks/bugs/ideas across team  
✅ Version control your workflow

**Option 2: Commands Only**
```gitignore
# In project root .gitignore
.dotagent/work/
```
✅ Share commands but not your personal todos  
❌ Can't collaborate on tasks/bugs

**Option 3: Local Only**
```gitignore
# In project root .gitignore
.dotagent/
```
✅ Keep workflow completely local  
❌ Team doesn't benefit from commands

### dotagent's .gitignore

The `.dotagent/.gitignore` itself ignores:
```
.cursor/              # Cursor IDE config
.DS_Store             # macOS files
```

---

## Extensibility

### Adding New Commands

1. Create `.md` file in appropriate category:
   ```bash
   touch commands/tasks/archive.md
   ```

2. Command becomes available as:
   ```
   /tasks_archive
   ```

3. Follow existing command structure:
   - Prompt definition
   - Behavior (step-by-step)
   - Output format
   - Rules

### Adding New Work Categories

1. Create directory under `work/`:
   ```bash
   mkdir -p work/research/templates
   ```

2. Add template:
   ```bash
   touch work/research/templates/paper.md
   ```

3. Create commands that reference it:
   ```bash
   touch commands/research/add.md
   ```

### Adding New Templates

1. Add template to appropriate directory:
   ```bash
   touch work/tasks/templates/sprint.md
   ```

2. Update commands to reference new template (or create new command)

---

## Design Principles

### 1. Separation of Concerns
- `commands/` = What dotagent **can do** (capabilities)
- `work/` = What dotagent **manages** (user's data)
- `agent_prompt.md` = How dotagent **behaves** (orchestration rules)
- `context.json` = What dotagent **knows** (project metadata)

### 2. Template-Driven Structure
- Commands never hardcode file structures
- Templates are the single source of truth for formats
- Users can customize templates without touching commands
- Enables consistency across all generated files

### 3. Safety & Transparency
- Preview before write (all mutation commands)
- Explicit confirm required
- Git commands suggest, never execute
- Read-only by default

### 4. Discoverability
- `/help` dynamically scans and lists all commands
- Category-based organization mirrors `work/` structure
- Command names follow predictable pattern

### 5. Simplicity
- Just markdown files and directories
- No build step, no dependencies
- Works with any text editor
- Version controllable

---

## Technical Details

### Command Discovery
`/help` works by:
1. Scanning `commands/` directory recursively
2. Finding all `.md` files
3. Extracting Goal line or first heading
4. Generating command ID from path
5. Grouping by category (directory name)

### Template Usage (Section D.1 in agent_prompt.md)
When creating new files, commands **MUST**:
1. Check if target file exists
2. If not, read appropriate template from `work/{category}/templates/`
3. Use template structure as base
4. Replace placeholders with user data
5. Write new file

This is enforced by agent_prompt.md Section D.1.

### File Naming
- Templates: Always singular (`todo.md`, not `todos.md`)
- Working files: Match template names (`todo.md`)
- Bug files: Exception using `BUG-XXX.md` pattern
- Preview files: Singular (`idea_preview.md`, `next_todo_preview.md`)

---

## Migration Notes

If upgrading from an older version of dotagent:

### Old → New Structure
| Old | New | Notes |
|-----|-----|-------|
| `tasks.json` | Deleted | Commands now in `commands/` directory |
| `prompts/` | `commands/` | Renamed for clarity |
| `artifacts/` | `work/` | Renamed to better reflect purpose |
| `context/` | `work/` + `context.json` | Split into workspace + metadata |
| `/check_context` | `/project_check` | Renamed for clarity |
| `/update_readme` | `/project_readme` | Renamed to match category |
| `/brainstorm` | `/ideas_brainstorm` | Added category prefix |

### Template Names Changed
| Old | New |
|-----|-----|
| `todos.md` | `todo.md` |
| `ideas.md` | `idea.md` |
| `gaps.md` | `gap.md` |
| `BUG-template.md` | `bug.md` |
| `session_log.md` | `session.md` |

---

## Troubleshooting

**Q: Commands not showing up in `/help`?**  
A: Make sure `.md` files are in `commands/` subdirectories with correct naming.

**Q: Template not being used?**  
A: Check file exists at `work/{category}/templates/{name}.md` (singular name).

**Q: Command using wrong paths?**  
A: Commands should reference `work/` not `artifacts/` or `context/`.

**Q: Git commands not working?**  
A: Git commands **suggest** commands for you to run—they never auto-execute.

---

**Last Updated:** 2024-11-06  
**Version:** 2.0 (Post-refactor)
