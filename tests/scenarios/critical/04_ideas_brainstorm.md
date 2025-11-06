# Test 4: Template Usage - Ideas (/ideas_brainstorm)

## Objective
Verify that /ideas_brainstorm uses template to structure raw ideas into specs.

## Execute
```
/ideas_brainstorm
Input: "Add async batch processing to handle thousands of documents in parallel with rate limiting"
```

## Expected Behavior
1. Reads .dotagent/work/ideas/templates/idea.md
2. Structures the raw idea into spec format
3. Creates preview at .dotagent/work/idea_preview.md
4. Shows preview inline
5. Asks for confirm
6. On confirm, writes to .dotagent/work/ideas/idea.md

## Verification
- [ ] Preview file created: `.dotagent/work/idea_preview.md`
- [ ] Contains structured sections (Title, Elevator, Problem, Features, etc.)
- [ ] Follows template format from .dotagent/work/ideas/templates/idea.md
- [ ] After confirm, .dotagent/work/ideas/idea.md matches structure

## Pass Criteria
✅ Idea spec created with all template sections (Elevator, Problem, Features, Milestones, etc.)

## Result
[ PASS / FAIL ] - [notes]

