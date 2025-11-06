# Test 12: Close Issue (/issues_close)

## Objective
Verify that /issues_close properly marks bugs as resolved.

## Prerequisites
Test 3 must have passed (BUG-001 exists)

## Execute
```
/issues_close
Bug ID: BUG-001
Resolution: "Fixed by implementing code block detection before sentence splitting"
```

## Expected Behavior
1. Reads .dotagent/work/issues/BUG-001.md
2. Updates status to "Closed"
3. Adds resolution notes
4. Updates history with closure timestamp
5. Shows preview
6. On confirm, updates file

## Verification
- [ ] Status changed to "Closed"
- [ ] Resolution section filled
- [ ] History updated with closure
- [ ] File still valid and readable

## Pass Criteria
✅ Bug marked as closed with resolution notes

## Result
[ PASS / FAIL ] - [notes]

