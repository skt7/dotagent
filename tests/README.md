# Dotagent Testing Framework

This directory contains comprehensive testing infrastructure for dotagent.

## Overview

Dotagent includes a functional testing framework that validates all commands work correctly in a realistic development environment.

## Test Infrastructure

```
tests/
├── README.md                    # This file
├── test.md                      # Test orchestrator (registered as /test command)
├── setup_test_env.sh            # Setup script (copies files)
├── scenarios/                   # Modular test scenarios
│   ├── critical/                # Tests 1-4 (must pass)
│   ├── important/               # Tests 5-7 (should pass)
│   ├── edge_cases/              # Tests 8-10 (nice to have)
│   └── extended/                # Tests 11-14 (comprehensive)
└── dummy_project/               # Realistic test project
    ├── .cursor/                 # Cursor configuration (created by setup)
    │   ├── rules/dotagent.mdc   # Dotagent system prompt
    │   └── commands/*.md        # 22 commands (21 dotagent + test.md)
    ├── .dotagent/               # Copied from main repo (isolated)
    ├── docprep/                 # Python library source (785 LOC)
    ├── tests/                   # Unit tests
    ├── examples/                # Usage examples
    └── .dotagent/work/          # Created by dotagent commands during testing
```

**Important:**
- `.dotagent/` is a **copy** (not symlink) - changes won't affect main repo
- `test.md` is registered as `/test` command in `.cursor/commands/`
- Run tests from `dummy_project/` by typing `/test` in Cursor chat

## Dummy Project: DocPrep

A realistic Python library for document preprocessing in RAG systems.

**Purpose:** Provides a production-quality codebase for testing dotagent commands

**Features:**
- Document chunking (multiple strategies)
- Token counting for LLMs
- Metadata extraction
- Embedding cache
- OpenAI integration

**Intentional Issues (for testing):**
1. **Code block bug** (`chunker.py:45`) - Chunking destroys code formatting
2. **Wrong tokenizer** (`tokens.py:28`) - GPT-4 uses incorrect encoding
3. **Memory leak** (`cache.py:56`) - Cache never evicts old entries
4. **Missing headers** (`parser.py:89`) - Parser misses H2/H3 headers

**TODOs (for testing):**
- PDF parsing support
- Semantic chunking with embeddings
- Async batch processing
- Custom tokenizers
- Chunk deduplication
- Sliding window overlap
- Structured data support

## Understanding the Test Plan

Before running tests, understand what `test.md` does:

1. **Asks you** which tests to run (interactive)
2. **Sets up** the test environment automatically
3. **Loads** dotagent configuration
4. **Executes** test scenarios based on your choice
5. **Documents** results in `TEST_RESULTS.md`

### Test Options You'll Be Asked

| Option | Tests | Time | Best For |
|--------|-------|------|----------|
| `"critical"` | 1-4 | ~5 min | Quick validation |
| `"critical, important"` | 1-7 | ~15 min | **Pre-merge** ⭐ |
| `"all"` | 1-14 | ~25 min | Full regression |
| Specific files | As chosen | Variable | Targeted testing |

---

## Running Tests

### Step 1: Setup Test Environment

**First time, or when dotagent commands/templates change:**

```bash
# From your project root (where .dotagent/ is)
.dotagent/tests/setup_test_env.sh
```

This script:
- ✅ Copies dotagent files to `.dotagent/tests/dummy_project/.dotagent/`
- ✅ Installs dotagent to `.dotagent/tests/dummy_project/.cursor/`
- ✅ Registers `/test` command in `.cursor/commands/`
- ✅ Cleans previous test artifacts
- ✅ Verifies all templates are present

---

### Step 2: Run Tests (Interactive)

**Simply invoke the `/test` command:**

1. **Navigate to dummy_project and open Cursor**
   ```bash
   cd .dotagent/tests/dummy_project
   cursor .
   ```

2. **Run the test command**
   - Open Cursor chat
   - Type: `/test`
   - AI will ask: *"What tests would you like to run?"*
   - Respond with your choice (e.g., `"critical, important"`)

3. **AI Handles Everything**
   - ✅ Loads `.dotagent/agent_prompt.md`
   - ✅ Executes chosen test scenarios
   - ✅ Documents results in `../TEST_RESULTS.md`

4. **Review Results**
   - Check `tests/TEST_RESULTS.md` for pass/fail
   - Review generated files in `.dotagent/work/`

**That's it!** Just type `/test` from within dummy_project and the AI orchestrates everything.

---

### Test Coverage (14 Scenarios)

The testing framework is **modular** - you can run different test suites:

**🔴 Critical Path (Tests 1-4) - MUST PASS**
1. `/help` - Command discovery
2. `/tasks_add` - Template usage for tasks
3. `/issues_report` - Template usage for bugs
4. `/ideas_brainstorm` - Template usage for ideas

**🟡 Important Tests (5-7) - SHOULD PASS**
5. `/tasks_update` - Update existing file
6. `/git_status` - Git safety (no auto-execution)
7. `/sessions_summarize` - Session tracking with template

**🟢 Edge Cases (8-10) - NICE TO HAVE**
8. Multiple bugs - Incremental ID assignment
9. Cross-command compatibility - Format consistency
10. `/issues_log_gap` - Gap logging with template

**🔵 Extended Tests (11-14) - COMPREHENSIVE**
11. `/git_commit` - Conventional commit messages
12. `/issues_close` - Bug resolution workflow
13. `/ideas_capture` - Quick idea capture
14. `/project_readme` - Documentation generation

### How Test Configuration Works

The test orchestrator will **ask you interactively** which tests to run. You don't need to edit any files!

**Response examples:**
- `"critical"` - Quick validation (4 tests)
- `"critical, important"` - Pre-merge recommended (7 tests)
- `"all"` - Full regression (14 tests)
- `"01_help.md, 05_tasks_update.md"` - Specific tests only

## What Tests Verify

### Template Usage
- Commands read from `.dotagent/work/*/templates/*.md`
- New files use template structure
- Placeholders are filled with actual data
- Format is consistent across commands

### File Management
- Correct paths (`.dotagent/work/` directory structure)
- Proper file naming (singular: `todo.md`, `bug.md`, etc.)
- No overwrites unless intended
- Append operations work correctly

### Command Behavior
- All 20 commands are discoverable
- Commands follow their specifications
- Previews shown before mutations
- Confirmation requested for changes

### Git Safety
- No automatic git execution
- Commands only suggest git operations
- User maintains full control

### Data Integrity
- Multiple commands can work with same files
- Format remains consistent
- No data corruption or conflicts

## Test Philosophy

**Agentic & Modular Testing:**

- **Agentic:** Tests are markdown prompts that instruct an AI to execute, verify, and document
- **Modular:** Each test is a separate file for easy maintenance and selective execution
- **Configurable:** Choose which test suites to run (critical, standard, comprehensive, custom)
- **Markdown-driven:** Aligns with dotagent's philosophy

This allows:
- ✅ Quick validation (critical tests in ~5 minutes)
- ✅ Comprehensive testing (all 14 tests when needed)
- ✅ Custom test runs (pick specific scenarios)
- ✅ Easy expansion (add new test files to scenarios/)

## Troubleshooting

### `.dotagent` symlink broken
**Solution:** Re-run `./setup_test_env.sh`

### Commands not found
**Check:**
- Symlink exists: `ls -la dummy_project/.dotagent`
- Commands accessible: `ls dummy_project/.dotagent/commands/`

### Templates not used
**Check:**
- Templates exist: `ls dummy_project/.dotagent/work/*/templates/`
- `agent_prompt.md` loaded in Cursor (section D.1)

### Tests fail
1. Review test output in `TEST_RESULTS.md`
2. Check command files in `commands/` for issues
3. Verify `agent_prompt.md` has template usage instructions
4. Compare actual output with expected format in scenario files

## Adding New Tests

To add new test scenarios:

1. **Create new test file**
   - Add to appropriate `scenarios/` subdirectory
   - Follow naming: `NN_description.md` (e.g., `15_new_test.md`)
   - Use existing test files as templates
   
2. **Update `test.md`**
   - Add test to overview table
   - Update run mode definitions if needed
   
3. **Update dummy_project** (if needed)
   - Add new bugs, TODOs, or code patterns to test against

4. **Update scenario verification**
   - Define expected format/structure inline in scenario file

5. **Document in this README**
   - Update test count and categories

## Success Criteria

**Ready to merge when:**
- ✅ All Critical Path tests pass (Tests 1-4)
- ✅ At least 80% of Important tests pass (Tests 5-7)
- ✅ No data corruption or git safety violations
- ✅ Template usage verified for all creation commands

**Fix before merge if:**
- ❌ Any Critical Path test fails
- ❌ Commands don't use templates
- ❌ Git commands execute automatically
- ❌ File format inconsistencies detected

## Continuous Testing

After changes to dotagent:

1. Clean test environment: `rm -rf .dotagent/tests/dummy_project/.dotagent/work/`
2. Re-run setup: `.dotagent/tests/setup_test_env.sh`
3. Execute test plan
4. Compare results with previous runs
5. Update scenario files if expected behavior changes

## Maintenance

- **dummy_project/.dotagent/work/** is gitignored (generated during tests)
- **Reset test environment:** `rm -rf .dotagent/tests/dummy_project/.dotagent/work`
- **Update scenarios:** Modify verification criteria in scenario files as needed

---

```
