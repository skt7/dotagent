# Test 5: File Update Without Template (/tasks_update)

## Objective
Verify that /tasks_update can modify existing task files without breaking format.

## Prerequisites
Test 2 must have passed (todo.md exists)

## Execute
```
/tasks_update
Input: "Complete: Add PDF parsing support"
```

## Expected Behavior
1. Reads existing .dotagent/work/tasks/todo.md
2. Finds matching task (fuzzy match on "PDF parsing")
3. Changes [ ] to [x]
4. Shows preview
5. On confirm, updates file

## Verification
- [ ] Task checkbox changed: `- [x] Add PDF parsing support`
- [ ] Other tasks unchanged
- [ ] Format preserved (tags, rationale intact)
- [ ] No corruption of session headers

## Pass Criteria
✅ Task marked complete without breaking file structure

## Result
[ PASS / FAIL ] - [notes]

