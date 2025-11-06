# Dotagent Test Orchestration Plan

You are the **Test Orchestrator** for dotagent. Your job is to:
1. **Setup the test environment** (if not already done)
2. **Configure dotagent** (load agent_prompt.md)
3. **Execute test scenarios** based on configuration below
4. **Document results** in TEST_RESULTS.md

---

## 🎯 Interactive Test Configuration

**You will be asked which tests to run. Here are your options:**

### Test Categories

| Category | Tests | Time | When to Use |
|----------|-------|------|-------------|
| **`critical`** | 1-4 | ~5 min | Quick validation (command discovery, template usage) |
| **`important`** | 5-7 | ~10 min | File operations, git safety |
| **`edge_cases`** | 8-10 | ~10 min | Multi-file scenarios, cross-command |
| **`extended`** | 11-14 | ~10 min | Advanced features (commit msgs, README gen) |

### Combined Options

| Option | Tests | Time | Recommended For |
|--------|-------|------|-----------------|
| **`critical, important`** | 1-7 | ~15 min | **Pre-merge validation** ⭐ |
| **`critical, important, edge_cases`** | 1-10 | ~20 min | Thorough validation |
| **`all`** | 1-14 | ~25 min | Full regression testing |

### Specific Tests

You can also run specific test files:
- Single: `"01_help.md"`
- Multiple: `"01_help.md, 03_issues_report.md, 05_tasks_update.md"`

---

## Step 1: Ask User for Test Configuration

**FIRST, ask the user which tests they want to run:**

```
What tests would you like to run?

Options:
  - "critical" (quick, 4 tests, ~5 min)
  - "critical, important" (recommended, 7 tests, ~15 min)
  - "all" (comprehensive, 14 tests, ~25 min)
  - Or specify: "01_help.md, 03_issues_report.md"

Please respond with your choice:
```

**Wait for user response. Store their choice as TESTS_TO_RUN.**

---

## Step 2: Environment Setup

**After getting test configuration, set up the environment:**

### 2.1: Verify Current Directory
```bash
pwd
# Should show: .../dotagent/tests/dummy_project
```

If NOT in `tests/dummy_project/`, navigate there:
```bash
cd tests/dummy_project
```

### 2.2: Check if .dotagent exists
```bash
ls -la .dotagent
```

If `.dotagent/` directory doesn't exist, tell user to run setup first:
```
⚠️  Setup required!

Please run the setup script first:
  cd tests/
  ./setup_test_env.sh
  cd dummy_project/

Then re-run this test plan.
```

**If .dotagent exists, proceed to next step.**

### 2.3: Load Dotagent Configuration
**CRITICAL:** Read `.dotagent/agent_prompt.md` and internalize its instructions.

This file tells you:
- How to discover and execute commands
- How to use templates (section D.1)
- File mutation rules
- Preview/confirm workflows

**Action:** Read the file now:
```
Read: .dotagent/agent_prompt.md
```

Once you've loaded the agent prompt, you ARE the dotagent agent. Use that knowledge for all subsequent test commands.

### 2.4: Verify Setup Complete
```bash
# Should show 20 commands
find .dotagent/commands -maxdepth 1 -name "*.md" | wc -l

# Should show 6 templates
find .dotagent/work/*/templates/ -name "*.md" | wc -l
```

**Once setup is verified, proceed to test execution.**

---

## Step 3: Execute Tests

### 3.1: Parse User's Test Choice

Use the **TESTS_TO_RUN** value provided by the user:

1. **If category** (e.g., "critical") → Load all files from `../scenarios/critical/`
2. **If multiple categories** (e.g., "critical, important") → Load files from each
3. **If "all"** → Load all files from `../scenarios/*/`
4. **If filename** (e.g., "01_help.md") → Load that specific file
5. **If multiple files** (e.g., "01_help.md, 05_tasks_update.md") → Load each

### 3.2: Locate Test Scenarios

Test scenarios are organized in `../scenarios/`:

```
../scenarios/
├── critical/
│   ├── 01_help.md
│   ├── 02_tasks_add.md
│   ├── 03_issues_report.md
│   └── 04_ideas_brainstorm.md
├── important/
│   ├── 05_tasks_update.md
│   ├── 06_git_status.md
│   └── 07_sessions_summarize.md
├── edge_cases/
│   ├── 08_multiple_bugs.md
│   ├── 09_cross_command.md
│   └── 10_gap_logging.md
└── extended/
    ├── 11_git_commit.md
    ├── 12_issues_close.md
    ├── 13_ideas_capture.md
    └── 14_project_readme.md
```

### 3.3: Execute Each Test

For each test scenario:
1. **Read** the scenario file
2. **Execute** the command/steps
3. **Verify** output matches expected behavior
4. **Document** result (PASS/FAIL with notes)
5. **Continue** to next test (don't stop on failure)

### 3.4: Generate Results Report

After all tests complete, create `../TEST_RESULTS.md` with:

```markdown
# Test Results - [DATE]

## Configuration
- User Choice: "[value user provided]"
- Files Executed: [list of test files run]

## Summary
- Total Tests: X
- Passed: Y
- Failed: Z
- Success Rate: N%

## Detailed Results

[For each test executed, include:]
- Test Name
- Result: PASS/FAIL
- Notes
- Issues (if any)

## Issues Found
[List any issues discovered]

## Recommendation
- [ ] All Tests Pass → READY
- [ ] Critical Failures → FIX BEFORE MERGE
- [ ] Other Failures → DOCUMENT FOR LATER
```

---

## Test Scenarios Overview

### 🔴 Critical Path (Tests 1-4) - MUST PASS

| # | Test | Command | Validates |
|---|------|---------|-----------|
| 1 | Command Discovery | `/help` | All 20 commands listed |
| 2 | Task Creation | `/tasks_add` | Template usage for tasks |
| 3 | Bug Reporting | `/issues_report` | Template usage for bugs |
| 4 | Idea Brainstorming | `/ideas_brainstorm` | Template usage for ideas |

### 🟡 Important Tests (5-7) - SHOULD PASS

| # | Test | Command | Validates |
|---|------|---------|-----------|
| 5 | Task Updates | `/tasks_update` | File modification |
| 6 | Git Safety | `/git_status` | No auto-execution |
| 7 | Session Tracking | `/sessions_summarize` | Session logging |

### 🟢 Edge Cases (8-10) - NICE TO HAVE

| # | Test | Command | Validates |
|---|------|---------|-----------|
| 8 | Multiple Bugs | `/issues_report` | ID incrementation |
| 9 | Cross-Command | `tasks/*` | Format consistency |
| 10 | Gap Logging | `/issues_log_gap` | Gap tracking |

### 🔵 Extended Tests (11-14) - COMPREHENSIVE

| # | Test | Command | Validates |
|---|------|---------|-----------|
| 11 | Commit Messages | `/git_commit` | Conventional commits |
| 12 | Close Issues | `/issues_close` | Bug resolution |
| 13 | Quick Ideas | `/ideas_capture` | Rapid capture |
| 14 | README Generation | `/project_readme` | Documentation |

---

## Execution Instructions

**Execution Summary:**

As the test orchestrator, you will:
1. ✅ **Ask user** which tests to run (Step 1)
2. ✅ **Setup environment** - run setup script (Step 2)
3. ✅ **Load configuration** - read agent_prompt.md (Step 2.3)
4. ✅ **Execute tests** - based on user choice (Step 3)
5. ✅ **Document results** - create TEST_RESULTS.md (Step 3.4)
6. ✅ **Report to user** - share findings

**After testing:**
- Review TEST_RESULTS.md with the user
- Note any failures for fixing
- Suggest re-running failed tests after fixes

---

**Ready to begin? Start with Step 1: Ask the user which tests to run!**

