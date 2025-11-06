# Test 13: Quick Idea Capture (/ideas_capture)

## Objective
Verify that /ideas_capture quickly saves raw ideas without full spec.

## Execute
```
/ideas_capture
Input: "Add deduplication for chunks to avoid storing identical content multiple times"
```

## Expected Behavior
1. Reads .dotagent/work/ideas/templates/idea.md
2. Creates minimal idea entry
3. Appends to .dotagent/work/ideas/idea.md
4. Quick workflow (less structured than /ideas_brainstorm)

## Verification
- [ ] Idea saved to .dotagent/work/ideas/idea.md
- [ ] Can coexist with full specs
- [ ] Includes date and basic info
- [ ] Fast capture workflow

## Pass Criteria
✅ Quick idea captured without requiring full spec

## Result
[ PASS / FAIL ] - [notes]

