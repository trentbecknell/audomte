#!/bin/bash
# Simple script to commit and push changes

cd /workspaces/audomte

echo "Step 1: Staging all changes..."
git add -A

echo ""
echo "Step 2: Creating commit..."
git commit -m "Add phone masking, SMS/email integration, and phone formatting

- Phone masking service for privacy
- Twilio SMS and SendGrid email integration  
- Automatic E.164 phone number formatting
- Bug fixes for UI and phone validation"

echo ""
echo "Step 3: Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Your code is now on GitHub"
echo "View at: https://github.com/trentbecknell/audomte"
