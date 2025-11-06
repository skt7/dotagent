# Test 10: Gap Logging (/issues_log_gap)

## Objective
Verify that /issues_log_gap uses template to track feature gaps.

## Execute
```
/issues_log_gap
Title: "No async support for batch processing"
Description: "Current implementation processes documents sequentially. Need async/await for better throughput."
Impact: high
```

## Expected Behavior
1. If .dotagent/work/issues/gap.md doesn't exist:
   - Reads .dotagent/work/issues/templates/gap.md
2. Assigns incremental gap ID
3. Appends to .dotagent/work/issues/gap.md
4. Shows preview
5. On confirm, writes

## Verification
- [ ] File created: `.dotagent/work/issues/gap.md`
- [ ] Contains gap entry with ID, date, title, description, impact
- [ ] Format matches template structure
- [ ] Can append multiple gaps

## Pass Criteria
✅ Gap logged with proper structure and ID

## Result
[ PASS / FAIL ] - [notes]

