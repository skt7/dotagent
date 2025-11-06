# Test 11: Git Commit Message (/git_commit)

## Objective
Verify that /git_commit generates conventional commit messages.

## Execute
```
/git_commit
```

## Expected Behavior
1. Asks for git diff or runs git status
2. Analyzes changes
3. Generates conventional commit message
4. Shows preview
5. **DOES NOT execute git commit**
6. Provides command for user to run

## Verification
- [ ] Commit message generated
- [ ] Follows conventional commits format (type: description)
- [ ] Includes relevant details from diff
- [ ] NO automatic git execution
- [ ] User given command to copy

## Pass Criteria
✅ Conventional commit message generated, no auto-execution

## Result
[ PASS / FAIL ] - [notes]

