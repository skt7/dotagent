# Test 7: Session Summary (/sessions_summarize)

## Objective
Verify that /sessions_summarize uses template to create session logs.

## Execute
```
/sessions_summarize
(Provide git status and diff output when requested)
```

## Expected Behavior
1. Asks for git status output
2. Asks for git diff output
3. If .dotagent/work/sessions/session.md doesn't exist:
   - Reads .dotagent/work/sessions/templates/session.md
4. Generates "Worked On" bullets from diffs
5. Shows preview
6. On confirm, creates/appends to .dotagent/work/sessions/session.md

## Verification
- [ ] File created: `.dotagent/work/sessions/session.md`
- [ ] Contains session header with date
- [ ] Has "Worked On" section with inferred items
- [ ] Format matches template structure

## Pass Criteria
✅ Session log created with proper structure and work items inferred from git changes

## Result
[ PASS / FAIL ] - [notes]

