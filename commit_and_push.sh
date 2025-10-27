#!/bin/bash
# Commit and push all changes to GitHub

cd /workspaces/audomte

echo "📝 Staging all changes..."
git add -A

echo ""
echo "📊 Changes to be committed:"
git status --short

echo ""
echo "💾 Creating commit..."
git commit -m "Add phone masking service, real SMS/email integration, and automatic phone formatting

Features:
- Phone masking service for privacy protection
- Real Twilio SMS integration with auto phone formatting
- SendGrid email integration
- Automatic E.164 phone number formatting
- Environment variable management (.env support)
- Comprehensive documentation and helper scripts

Bug fixes:
- Fixed UI issues with project creation
- Added proper phone validation and formatting
- Database schema updates for phone masking"

echo ""
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Check your repository at:"
echo "   https://github.com/trentbecknell/audomte"
