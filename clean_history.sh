#!/bin/bash
# Completely remove secrets from git history using filter-branch

cd /workspaces/audomte

echo "⚠️  WARNING: This will rewrite git history!"
echo "   This is necessary to remove leaked secrets."
echo ""
read -p "Press Enter to continue or Ctrl+C to cancel..."

echo ""
echo "🔒 Removing sensitive files from entire git history..."

# Remove .env from all commits
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch alioop-microservice-prototype/.env' \
  --prune-empty --tag-name-filter cat -- --all

# Remove fetch_twilio_number.py from all commits
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch alioop-microservice-prototype/fetch_twilio_number.py' \
  --prune-empty --tag-name-filter cat -- --all

# Remove ENV_VARIABLES_GUIDE.md from all commits
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch alioop-microservice-prototype/ENV_VARIABLES_GUIDE.md' \
  --prune-empty --tag-name-filter cat -- --all

echo ""
echo "✅ Git history cleaned!"
echo ""
echo "🚀 Force pushing to GitHub..."
git push origin main --force

echo ""
echo "✅ Success! Your code is now on GitHub without secrets."
echo "   View at: https://github.com/trentbecknell/audomte"
echo ""
echo "⚠️  IMPORTANT: You should rotate your Twilio credentials now since they were exposed:"
echo "   1. Go to https://console.twilio.com/"
echo "   2. Get a new Auth Token"
echo "   3. Update your local .env file"
