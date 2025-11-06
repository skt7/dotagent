#!/bin/bash

# Setup Test Environment for Dotagent
# This script sets up dotagent in dummy_project for testing

set -e

echo "🔧 Setting up dotagent test environment..."
echo ""

# Navigate to tests directory
cd "$(dirname "$0")"
REPO_ROOT="$(cd .. && pwd)"

# Step 1: Copy dotagent to dummy_project/.dotagent
echo "1. Copying dotagent to dummy_project/.dotagent/..."
cd dummy_project

if [ -L ".dotagent" ]; then
    echo "   ⚠️  Found symlink (removing...)"
    rm .dotagent
fi

if [ -d ".dotagent" ]; then
    echo "   ⚠️  Cleaning existing .dotagent/..."
    rm -rf .dotagent
fi

# Copy entire dotagent directory (except tests/)
echo "   📦 Copying dotagent files..."
mkdir -p .dotagent
cp -r $REPO_ROOT/{commands,work,agent_prompt.md,context.json,setup.sh} .dotagent/ 2>/dev/null || true
chmod +x .dotagent/setup.sh
echo "   ✓ Copied dotagent to .dotagent/"

# Step 2: Run the main setup.sh script
echo ""
echo "2. Running dotagent setup..."
cd .dotagent
./setup.sh
cd ..

# Step 3: Register /test command
echo ""
echo "3. Registering /test command..."
if [ -f "../test.md" ]; then
    cp "../test.md" ".cursor/commands/"
    echo "   ✓ Registered /test command in .cursor/commands/"
else
    echo "   ⚠️  test.md not found"
fi

# Step 4: Clean previous test artifacts
echo ""
echo "4. Cleaning previous test artifacts..."
if [ -d ".dotagent/work" ]; then
    # Keep templates, remove user files
    find .dotagent/work -mindepth 2 -maxdepth 2 -type f ! -path "*/templates/*" -delete 2>/dev/null
    echo "   ✓ Cleaned .dotagent/work/ (kept templates)"
else
    echo "   ✓ No artifacts to clean"
fi

# Step 5: Verify test setup
echo ""
echo "5. Verifying test environment..."

# Check Cursor setup
if [ -f ".cursor/rules/dotagent.mdc" ]; then
    echo "   ✓ Cursor rule installed"
else
    echo "   ⚠️  Cursor rule not found"
fi

if [ -d ".cursor/commands" ]; then
    COMMAND_COUNT=$(find .cursor/commands -name "*.md" | wc -l | tr -d ' ')
    echo "   ✓ Found $COMMAND_COUNT commands in .cursor/"
fi

# Check dotagent structure
TEMPLATE_COUNT=$(find .dotagent/work/*/templates -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
echo "   ✓ Found $TEMPLATE_COUNT templates in .dotagent/work/"

# Display structure
echo ""
echo "════════════════════════════════════════"
echo "✅ TEST ENVIRONMENT READY"
echo "════════════════════════════════════════"
echo ""
echo "📁 Structure:"
echo "   tests/dummy_project/"
echo "   ├── .dotagent/      → isolated copy"
echo "   ├── test.md    → test orchestrator"
echo "   ├── docprep/        → test Python library"
echo "   └── .dotagent/work/ → templates + test artifacts"
echo ""
echo "   tests/.cursor/      → Cursor integration"
echo "   ├── rules/dotagent.mdc"
echo "   └── commands/*.md"
echo ""
echo "💡 Important:"
echo "   - .dotagent/ is isolated (changes won't affect main repo)"
echo "   - Cursor is configured in tests/ directory"
echo "   - test.md ready to run"
echo ""
echo "🎯 Next Steps:"
echo "   1. cd tests/dummy_project/"
echo "   2. cursor test.md"
echo "   3. Send test.md to Cursor chat"
echo "   4. Answer which tests to run"
echo "   5. Let the AI orchestrate!"
echo ""
