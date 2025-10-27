# Verify Phone Numbers for Twilio Trial Account

## The Problem
Twilio trial accounts can only send SMS to **verified phone numbers**. You'll get error 21211 if you try to send to unverified numbers.

## Solution: Verify Your Test Numbers

### Step 1: Go to Twilio Console
Open: https://console.twilio.com/us1/develop/phone-numbers/manage/verified

### Step 2: Click "Add a new Caller ID" or "Verify a Phone Number"

### Step 3: Enter the Phone Number
- Enter the phone number you want to test with (e.g., +15133092841)
- Use E.164 format: +1XXXXXXXXXX

### Step 4: Verify via SMS or Call
- Twilio will send you a verification code
- Enter the code to verify the number

### Step 5: Test Again
Once verified, you can send SMS to that number from your app!

## Alternative: Upgrade to Paid Account
If you need to send to any number without verification:
1. Go to https://console.twilio.com/us1/billing/manage-billing/upgrade
2. Add payment method
3. Purchase a phone number (if needed)
4. You can now send to any valid phone number

## Testing Without Verification
For testing purposes without real SMS:
1. Check the Twilio console logs to see if messages were queued: https://console.twilio.com/us1/monitor/logs/sms
2. The message will show as "queued" but won't deliver to unverified numbers

## Quick Links
- Verify Numbers: https://console.twilio.com/us1/develop/phone-numbers/manage/verified
- SMS Logs: https://console.twilio.com/us1/monitor/logs/sms
- Upgrade Account: https://console.twilio.com/us1/billing/manage-billing/upgrade
