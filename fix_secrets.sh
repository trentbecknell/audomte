#!/bin/bash
# Fix the secret leak and push again

cd /workspaces/audomte

echo "🔒 Removing secrets from git history..."

# Remove the .env file from git
git rm --cached alioop-microservice-prototype/.env

# Remove the fetch_twilio_number.py file (has hardcoded credentials)
git rm alioop-microservice-prototype/fetch_twilio_number.py

# Remove ENV_VARIABLES_GUIDE.md (has example credentials)
git rm alioop-microservice-prototype/ENV_VARIABLES_GUIDE.md

echo "✅ Secrets removed from git"
echo ""
echo "📝 Creating new commit..."
git commit -m "Remove sensitive credentials from repository"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Check your repo at:"
echo "   https://github.com/trentbecknell/audomte"
