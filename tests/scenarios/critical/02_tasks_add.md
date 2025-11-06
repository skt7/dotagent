# Test 2: Template Usage - Tasks (/tasks_add)

## Objective
Verify that /tasks_add properly uses the template to create new task files.

## Execute
```
/tasks_add
Input: "Add PDF parsing support @priority:high @effort:large — extend document format support beyond text/markdown"
```

## Expected Behavior
1. Checks if .dotagent/work/tasks/todo.md exists
2. If not, reads .dotagent/work/tasks/templates/todo.md
3. Creates .dotagent/work/tasks/todo.md with structure from template
4. Shows preview of task to be added
5. Asks for "confirm/edit/cancel"
6. On confirm, writes file

## Verification
- [ ] File created: `.dotagent/work/tasks/todo.md`
- [ ] Contains template structure:
  - Header: `# Tasks`
  - Session: `## Session: YYYY-MM-DD`
  - Task format: `- [ ] Task description @priority:high @effort:large — rationale`
- [ ] Task includes both @priority and @effort tags

## Pass Criteria
✅ Task file created using template with correct structure and tags

## Result
[ PASS / FAIL ] - [notes]

