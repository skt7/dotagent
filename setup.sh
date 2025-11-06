#!/bin/bash

# Dotagent Setup Script
# Run this after cloning dotagent into your project's .dotagent directory
# Usage: cd .dotagent && ./setup.sh

set -e

echo "🔧 Setting up dotagent in your project..."
echo ""

# Determine project root (parent of .dotagent)
if [[ "$(basename "$PWD")" == ".dotagent" ]]; then
    PROJECT_ROOT=".."
    DOTAGENT_ROOT="."
else
    echo "❌ Error: Please run this script from within the .dotagent directory"
    echo ""
    echo "Expected: cd .dotagent && ./setup.sh"
    exit 1
fi

# Step 1: Create .cursor directory if needed
echo "1. Setting up .cursor directory..."
if [ ! -d "$PROJECT_ROOT/.cursor" ]; then
    mkdir -p "$PROJECT_ROOT/.cursor/rules"
    mkdir -p "$PROJECT_ROOT/.cursor/commands"
    echo "   ✓ Created .cursor/ structure"
else
    mkdir -p "$PROJECT_ROOT/.cursor/rules"
    mkdir -p "$PROJECT_ROOT/.cursor/commands"
    echo "   ✓ .cursor/ directory exists"
fi

# Step 2: Copy agent_prompt.md as Cursor rule
echo ""
echo "2. Installing dotagent rule..."
if [ -f "agent_prompt.md" ]; then
    cp agent_prompt.md "$PROJECT_ROOT/.cursor/rules/dotagent.mdc"
    echo "   ✓ Copied agent_prompt.md → .cursor/rules/dotagent.mdc"
else
    echo "   ❌ agent_prompt.md not found!"
    exit 1
fi

# Step 3: Copy all commands to .cursor/commands/
echo ""
echo "3. Installing dotagent commands..."
if [ -d "commands" ]; then
    # Count commands
    COMMAND_COUNT=$(find commands -maxdepth 1 -name "*.md" | wc -l | tr -d ' ')
    
    # Copy all command files
    cp commands/*.md "$PROJECT_ROOT/.cursor/commands/"
    echo "   ✓ Copied $COMMAND_COUNT commands to .cursor/commands/"
else
    echo "   ❌ commands/ directory not found!"
    exit 1
fi

# Step 4: Verify installation
echo ""
echo "4. Verifying installation..."

# Check rule
if [ -f "$PROJECT_ROOT/.cursor/rules/dotagent.mdc" ]; then
    echo "   ✓ Dotagent rule installed"
else
    echo "   ❌ Rule not installed"
    exit 1
fi

# Check commands
INSTALLED_COUNT=$(find "$PROJECT_ROOT/.cursor/commands" -name "*.md" | wc -l | tr -d ' ')
if [ "$INSTALLED_COUNT" -ge 20 ]; then
    echo "   ✓ Commands installed ($INSTALLED_COUNT files)"
else
    echo "   ⚠️  Only $INSTALLED_COUNT command files found (expected 20+)"
fi

# Success message
echo ""
echo "════════════════════════════════════════"
echo "✅ DOTAGENT SETUP COMPLETE"
echo "════════════════════════════════════════"
echo ""
echo "📁 Installed:"
echo "   $PROJECT_ROOT/.cursor/rules/dotagent.mdc"
echo "   $PROJECT_ROOT/.cursor/commands/*.md ($COMMAND_COUNT commands)"
echo ""
echo "🎯 Next steps:"
echo "   1. Restart Cursor (to load the new rule)"
echo "   2. Try a command: /help"
echo "   3. Or ask naturally: 'Check git status'"
echo ""
echo "💡 Available commands:"
echo "   /help              - List all commands"
echo "   /git_status        - Check repository status"
echo "   /tasks_add         - Add a development task"
echo "   /issues_report     - Report a bug"
echo "   /ideas_brainstorm  - Structure an idea"
echo "   ...and 15 more!"
echo ""
echo "📖 Documentation:"
echo "   - README.md for usage guide"
echo "   - agent_prompt.md for system behavior"
echo "   - commands/ for all available commands"
echo ""


