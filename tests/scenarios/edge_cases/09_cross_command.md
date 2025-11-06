# Test 9: Cross-Command Compatibility (tasks)

## Objective
Verify that multiple task commands work with the same todo.md file without conflicts.

## Execute
```
1. /tasks_add
   Input: "Implement semantic chunking with embeddings @priority:medium @effort:large — use embeddings to find natural break points"

2. /tasks_update
   Input: "Complete: Add PDF parsing support"

3. /tasks_next
   (Analyze and suggest next task)
```

## Expected Behavior
- All three commands work with same todo.md file
- Format remains consistent
- No corruption or conflicts
- Each command respects the file structure

## Verification
- [ ] File format valid after each command
- [ ] All commands can read/write successfully
- [ ] Data integrity maintained
- [ ] Session headers preserved
- [ ] Tags and rationales intact

## Pass Criteria
✅ All three task commands work with same file without corruption

## Result
[ PASS / FAIL ] - [notes]

