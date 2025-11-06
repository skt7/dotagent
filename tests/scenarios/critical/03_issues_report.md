# Test 3: Template Usage - Bug Reports (/issues_report)

## Objective
Verify that /issues_report uses template to create properly structured bug reports.

## Execute
```
/issues_report
Title: "Chunking breaks on code blocks"
Steps: 
  1. Create DocumentChunker with SENTENCE strategy
  2. Pass text containing markdown code blocks
  3. Call chunk_text()
Expected: "Code blocks preserved as complete units"
Actual: "Code blocks split mid-function, destroying formatting"
Labels: "bug, critical, chunking"
```

## Expected Behavior
1. Reads .dotagent/work/issues/templates/bug.md
2. Assigns next bug ID (BUG-001 if first)
3. Fills template with provided information
4. Shows preview
5. On confirm, creates .dotagent/work/issues/BUG-001.md

## Verification
- [ ] File created: `.dotagent/work/issues/BUG-001.md`
- [ ] Contains YAML frontmatter with: id, title, status, severity, labels
- [ ] Has all sections: Description, Steps to Reproduce, Expected Behavior, Actual Behavior
- [ ] Proper markdown structure with headers

## Pass Criteria
✅ Bug report created with proper YAML frontmatter and all template sections

## Result
[ PASS / FAIL ] - [notes]

