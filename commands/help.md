# Help - List All Commands

## Goal
Show user all available dotagent commands grouped by category.

## Inputs
- None

## Behavior

Display all commands organized by category:

```
📋 DOTAGENT COMMANDS

═══ Git Operations ═══
/git_add          - Stage files for commit
/git_commit       - Create conventional commits
/git_create_branch - Create and switch to new branch
/git_diff         - Show detailed file changes
/git_status       - Check repository status
/git_sync         - Pull and push changes

═══ Task Management ═══
/tasks_add        - Add new development task
/tasks_update     - Update task status
/tasks_next       - Suggest next task to work on

═══ Issue Tracking ═══
/issues_report    - Report a bug with details
/issues_close     - Mark bug as resolved
/issues_describe  - Get detailed bug information
/issues_solve     - Mark issue as solved
/issues_log_gap   - Log a feature gap

═══ Idea Management ═══
/ideas_brainstorm - Structure raw idea into spec
/ideas_capture    - Quick idea capture

═══ Session Tracking ═══
/sessions_summarize - Generate session summary from git changes

═══ Project Context ═══
/project_check    - Review project context
/project_readme   - Generate/update README

═══ Help ═══
/help             - Show this help message

💡 Usage: Type any command (e.g., /git_status) to execute it.
```

## Output
Reply with the command list above.

## Examples

User: `/help`  
Assistant: [Shows full command list]
