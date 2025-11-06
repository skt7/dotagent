# Test 8: Multiple Bugs (Incremental IDs)

## Objective
Verify that bug IDs increment correctly when multiple bugs are reported.

## Prerequisites
Test 3 must have passed (BUG-001 exists)

## Execute
```
/issues_report
Title: "GPT-4 tokenizer uses wrong encoding"
Steps: 
  1. Create TokenCounter with model="gpt-4"
  2. Count tokens in text
Expected: "Uses cl100k_base encoding"
Actual: "Uses gpt2 encoding, giving incorrect counts"
Labels: "bug, tokenizer"
```

## Expected Behavior
- Assigns ID BUG-002 (incrementing from BUG-001)
- Creates separate file .dotagent/work/issues/BUG-002.md
- Both files coexist

## Verification
- [ ] Both BUG-001.md and BUG-002.md exist
- [ ] IDs are sequential
- [ ] Files are independent
- [ ] No overwriting of previous bug

## Pass Criteria
✅ Second bug report created with incremented ID (BUG-002)

## Result
[ PASS / FAIL ] - [notes]

