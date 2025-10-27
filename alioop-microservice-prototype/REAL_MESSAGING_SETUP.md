# Real Email & SMS Setup Guide

This guide will help you configure the app to send real emails and text messages.

## Overview

The app supports:
- **Email**: SendGrid API
- **SMS**: Twilio API

Without API keys, messages are logged to the console (DRYRUN mode).
With API keys configured, messages are sent to real recipients.

---

## 📧 SendGrid Setup (Email)

### 1. Create SendGrid Account
1. Go to https://signup.sendgrid.com/
2. Sign up for a free account (100 emails/day free tier)
3. Verify your email address

### 2. Get API Key
1. Log into SendGrid dashboard
2. Go to **Settings** → **API Keys**
3. Click **Create API Key**
4. Name it (e.g., "Alioop Local Dev")
5. Choose **Full Access** or **Restricted Access** (with Mail Send permission)
6. Copy the API key (you'll only see it once!)

### 3. Verify Sender Email
1. Go to **Settings** → **Sender Authentication**
2. Choose **Single Sender Verification**
3. Add your email address that you'll send FROM
4. Verify the email they send you

### 4. Set Environment Variables

```bash
export SENDGRID_API_KEY="SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export SENDGRID_FROM_EMAIL="your-verified-email@example.com"
```

Or create a `.env` file:
```bash
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SENDGRID_FROM_EMAIL=your-verified-email@example.com
```

### 5. Test It
Restart the server and try sending an email through the app!

---

## 📱 Twilio Setup (SMS)

### 1. Create Twilio Account
1. Go to https://www.twilio.com/try-twilio
2. Sign up for a free trial account
3. Verify your phone number

### 2. Get Credentials
1. Log into Twilio Console: https://console.twilio.com/
2. Find your **Account SID** and **Auth Token** on the dashboard
3. Copy both values

### 3. Get a Phone Number
1. In Twilio Console, go to **Phone Numbers** → **Manage** → **Buy a number**
2. Choose a phone number (free on trial)
3. Make sure it has **SMS** capability
4. Copy your Twilio phone number (e.g., +1-555-123-4567)

**Trial Limitations:**
- Can only send to verified phone numbers
- Messages include "Sent from your Twilio trial account"

### 4. Add Verified Phone Numbers (Trial Mode)
If on trial, you need to verify recipient numbers:
1. Go to **Phone Numbers** → **Manage** → **Verified Caller IDs**
2. Click **Add a new Caller ID**
3. Enter the phone number you want to send SMS to
4. Verify via SMS code

### 5. Set Environment Variables

```bash
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_auth_token_here"
export TWILIO_FROM_NUMBER="+15551234567"
```

Or add to `.env` file:
```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_FROM_NUMBER=+15551234567
```

### 6. Phone Number Format
Make sure phone numbers in the app use E.164 format:
- ✅ Correct: `+15551234567`
- ❌ Wrong: `555-123-4567` or `(555) 123-4567`

---

## 🚀 Quick Start with Environment Variables

### Option 1: Export in Terminal
```bash
# SendGrid
export SENDGRID_API_KEY="SG.your_key_here"
export SENDGRID_FROM_EMAIL="you@example.com"

# Twilio
export TWILIO_ACCOUNT_SID="ACyour_sid_here"
export TWILIO_AUTH_TOKEN="your_token_here"
export TWILIO_FROM_NUMBER="+15551234567"

# Restart server
./start_server.sh
```

### Option 2: Create .env File
Create `/workspaces/audomte/alioop-microservice-prototype/.env`:

```bash
# SendGrid Configuration
SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SENDGRID_FROM_EMAIL=noreply@yourdomain.com

# Twilio Configuration
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_FROM_NUMBER=+15551234567

# Phone Masking (optional)
PHONE_MASKING_ENABLED=true
PHONE_MASKING_PROVIDER=twilio
```

Then install and use python-dotenv:
```bash
pip install python-dotenv
```

Update `app/main.py` to load .env:
```python
from dotenv import load_dotenv
load_dotenv()  # Add this at the top
```

---

## 🧪 Testing

### Test Email
```bash
curl -X POST http://localhost:8000/send \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 1,
    "channel": "email",
    "body": "Test email from Alioop!"
  }'
```

### Test SMS
```bash
curl -X POST http://localhost:8000/send \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": 1,
    "channel": "sms",
    "body": "Test SMS from Alioop!"
  }'
```

---

## 📊 Cost Estimates

### SendGrid
- **Free Tier**: 100 emails/day forever
- **Essentials**: $19.95/month for 50,000 emails
- **Pro**: $89.95/month for 100,000 emails

### Twilio
- **Trial**: Free with limitations (verified numbers only)
- **Pay-as-you-go**: 
  - SMS: $0.0079 per message (US)
  - Phone number: $1.15/month

---

## 🔍 Troubleshooting

### Email Not Sending
1. Check API key is correct and has Mail Send permission
2. Verify sender email is authenticated in SendGrid
3. Check server logs for error messages
4. Ensure no firewall blocking outbound HTTPS

### SMS Not Sending
1. Verify Account SID and Auth Token are correct
2. Check phone number format (+1XXXXXXXXXX)
3. On trial: Ensure recipient number is verified
4. Check Twilio console for error logs
5. Ensure phone number has SMS capability

### Environment Variables Not Loading
```bash
# Check if variables are set
echo $SENDGRID_API_KEY
echo $TWILIO_ACCOUNT_SID

# If empty, they're not set. Re-export them.
```

---

## 🎯 Next Steps

1. **Start with SendGrid** (easier, no phone verification needed)
2. **Test with your own email** first
3. **Add Twilio** for SMS capability
4. **Upgrade accounts** when ready for production
5. **Monitor usage** in respective dashboards

For production, consider:
- Domain authentication for better email deliverability
- Dedicated IP address for high-volume sending
- Webhook handlers for delivery tracking
- Rate limiting to avoid spam triggers
