# Test 6: Git Safety (/git_status)

## Objective
Verify that git commands never execute automatically - only suggest commands to user.

## Execute
```
/git_status
```

## Expected Behavior
- Shows git status output (or asks user to run git status)
- Parses status
- Categorizes files (staged, unstaged, untracked)
- **Never runs git commands automatically**
- Only shows suggested commands

## Verification
- [ ] No automatic git execution
- [ ] Output is informational only
- [ ] Suggests commands for user to run
- [ ] User maintains full control

## Pass Criteria
✅ Git information displayed, but NO automatic git command execution

## Result
[ PASS / FAIL ] - [notes]

