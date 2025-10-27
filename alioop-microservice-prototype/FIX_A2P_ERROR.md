# Fix Twilio Error 30034: A2P 10DLC Registration Required

## The Problem
Error 30034 means your 10-digit phone number needs to be registered for Application-to-Person (A2P) messaging. This is required by US carriers for business SMS.

## Quick Solution: Use a Toll-Free Number (Recommended for Testing)

### Option 1: Get a Toll-Free Number (Fastest - No Registration Required)
1. Go to: https://console.twilio.com/us1/develop/phone-numbers/manage/search
2. Select "Toll-Free" in the number type
3. Search and buy a toll-free number (starts with 800, 888, 877, 866, 855, 844, 833)
4. Update your .env file with the new number:
   ```
   TWILIO_FROM_NUMBER=+18881234567  # Your new toll-free number
   ```
5. Restart your server

**Toll-free numbers work immediately** - no registration needed!

## Long-term Solution: Register Your 10DLC Number

### Option 2: Register for A2P 10DLC (Takes 1-4 weeks)
If you want to keep using your regular 10-digit number (+19783387220):

1. **Register Your Business:**
   - Go to: https://console.twilio.com/us1/develop/sms/campaign-registry
   - Click "Register a Business Profile"
   - Provide business information (name, address, EIN, etc.)
   - Cost: ~$4 one-time fee

2. **Create a Campaign:**
   - After business approval, create a "Use Case Campaign"
   - Describe how you'll use SMS (e.g., "Client notifications and project updates")
   - Cost: ~$10-15/month per campaign

3. **Approval Time:**
   - Low Volume Standard: Instant approval
   - Standard: 1-2 weeks
   - Can take up to 4 weeks

4. **Once Approved:**
   - Your number will work for A2P messaging
   - Much higher throughput limits

## Recommended Next Steps

**For immediate testing:** Get a toll-free number (5 minutes setup)
**For production:** Complete A2P 10DLC registration (do in parallel)

## Update Your Configuration

After getting a toll-free number, update your .env:

```bash
# Change this line:
TWILIO_FROM_NUMBER=+19783387220

# To your new toll-free number:
TWILIO_FROM_NUMBER=+18881234567
```

Then restart the server.

## Quick Links
- Buy Toll-Free Number: https://console.twilio.com/us1/develop/phone-numbers/manage/search
- A2P 10DLC Registration: https://console.twilio.com/us1/develop/sms/campaign-registry
- Learn More: https://www.twilio.com/docs/sms/a2p-10dlc
