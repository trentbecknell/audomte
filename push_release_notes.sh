#!/bin/bash
# Add release notes and push to GitHub

cd /workspaces/audomte

echo "📝 Adding release notes and changelog..."
git add alioop-microservice-prototype/RELEASE_NOTES.md
git add alioop-microservice-prototype/CHANGELOG.md

echo ""
echo "💾 Committing..."
git commit -m "Add v1.0.0 release notes and changelog

- Comprehensive release notes with all features
- Changelog following Keep a Changelog format
- Documentation of bug fixes and improvements
- Quick start guide and API documentation
- Security and known limitations sections"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Release notes published!"
echo "   View at: https://github.com/trentbecknell/audomte"
