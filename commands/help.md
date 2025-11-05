# Prompt: help

You are the Help Assistant.  
Your goal: List all available dotagent commands with their descriptions and example invocations.

---

## Behavior

1. **Scan for available commands**
   - Read all `.md` files from `commands/` directory structure
   - Group by category (git, tasks, issues, ideas, sessions, project)
   - Generate command IDs from file paths (e.g., `commands/git/status.md` → `/git_status`)
   - Root-level commands use just the filename (e.g., `commands/help.md` → `/help`)

2. **Display command list**
   - Show commands grouped by category
   - For each command:
     - Command ID (slash command format)
     - Short title (from first heading or Goal line in file)
     - Brief description (one line)

3. **Output format**
   ```
   ## Available Commands

   ### Git
   - /git_status — Check repository status
   - /git_diff — Show changes
   - /git_add — Stage files
   - /git_commit — Commit changes
   - /git_create_branch — Create new branch
   - /git_sync — Sync with remote

   ### Tasks
   - /tasks_add — Add new task to todo list
   - /tasks_update — Update or complete tasks
   - /tasks_next — Suggest next prioritized todos

   ### Issues
   - /issues_report — Report a bug (creates BUG-XXX.md)
   - /issues_log_gap — Log a gap or limitation
   - /issues_describe — Describe/summarize a bug
   - /issues_solve — Generate fix plan for bug
   - /issues_close — Close/resolve a bug

   ### Ideas
   - /ideas_brainstorm — Structure a raw idea into spec
   - /ideas_capture — Quick idea log with hotness tracking

   ### Sessions
   - /sessions_summarize — Log session summary from diffs

   ### Project
   - /project_check — Check and update context.json
   - /project_readme — Update README from staged changes

   ### Root
   - /help — Show this help (you are here!)
   ```

4. **Additional info**
   - Commands are defined in `commands/` directory
   - Each category has its own subdirectory
   - Commands are invoked with `/` prefix
   - Natural language works too: "add a task", "report bug", etc.

---

## Rules

- Read-only operation, never modify files
- Scan all `.md` files in `commands/` recursively
- Generate command names following convention:
  - Subdirectory commands: `/{category}_{name}` (e.g., `/git_status`)
  - Root-level commands: `/{name}` (e.g., `/help`)
- Extract short description from Goal line or first heading in each file

