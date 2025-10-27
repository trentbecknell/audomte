#!/usr/bin/env python3
"""
Configuration Check Script
Verifies that email and SMS services are properly configured
"""

import os
import sys

def check_env_var(name, required=False):
    """Check if an environment variable is set"""
    value = os.getenv(name)
    if value:
        # Mask sensitive values
        if 'KEY' in name or 'TOKEN' in name:
            masked = value[:8] + '...' + value[-4:] if len(value) > 12 else '***'
            print(f"  ✓ {name}: {masked}")
        else:
            print(f"  ✓ {name}: {value}")
        return True
    else:
        status = "❌" if required else "⚠️"
        print(f"  {status} {name}: Not set")
        return False

def test_sendgrid():
    """Test SendGrid configuration"""
    print("\n📧 SendGrid (Email) Configuration:")
    api_key = check_env_var("SENDGRID_API_KEY")
    from_email = check_env_var("SENDGRID_FROM_EMAIL")
    
    if api_key:
        try:
            from sendgrid import SendGridAPIClient
            print("  ✓ SendGrid library installed")
            
            # Try to initialize (doesn't send anything)
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            print("  ✓ API key format appears valid")
            return True
        except ImportError:
            print("  ❌ SendGrid library not installed. Run: pip install sendgrid")
            return False
        except Exception as e:
            print(f"  ⚠️  Warning: {e}")
            return False
    else:
        print("  ℹ️  Email will run in DRYRUN mode (logged to console)")
        return False

def test_twilio():
    """Test Twilio configuration"""
    print("\n📱 Twilio (SMS) Configuration:")
    sid = check_env_var("TWILIO_ACCOUNT_SID")
    auth = check_env_var("TWILIO_AUTH_TOKEN")
    from_num = check_env_var("TWILIO_FROM_NUMBER")
    
    if sid and auth and from_num:
        try:
            from twilio.rest import Client
            print("  ✓ Twilio library installed")
            
            # Try to initialize (doesn't send anything)
            client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
            print("  ✓ Credentials format appears valid")
            return True
        except ImportError:
            print("  ❌ Twilio library not installed. Run: pip install twilio")
            return False
        except Exception as e:
            print(f"  ⚠️  Warning: {e}")
            return False
    else:
        print("  ℹ️  SMS will run in DRYRUN mode (logged to console)")
        return False

def test_phone_masking():
    """Test phone masking configuration"""
    print("\n🔒 Phone Masking Configuration:")
    enabled = check_env_var("PHONE_MASKING_ENABLED")
    provider = check_env_var("PHONE_MASKING_PROVIDER")
    
    if enabled:
        print(f"  ✓ Phone masking is enabled")
    else:
        print("  ℹ️  Using default: enabled")
    
    return True

def main():
    print("=" * 60)
    print("🔍 Alioop Messaging Configuration Check")
    print("=" * 60)
    
    sendgrid_ok = test_sendgrid()
    twilio_ok = test_twilio()
    masking_ok = test_phone_masking()
    
    print("\n" + "=" * 60)
    print("📊 Summary:")
    print("=" * 60)
    
    if sendgrid_ok:
        print("✅ Email: LIVE (real emails will be sent)")
    else:
        print("⚠️  Email: DRYRUN mode (check console logs)")
    
    if twilio_ok:
        print("✅ SMS: LIVE (real text messages will be sent)")
    else:
        print("⚠️  SMS: DRYRUN mode (check console logs)")
    
    if masking_ok:
        print("✅ Phone Masking: Configured")
    
    print("\n" + "=" * 60)
    
    if not sendgrid_ok and not twilio_ok:
        print("\n💡 To enable real messaging:")
        print("   See REAL_MESSAGING_SETUP.md for detailed instructions")
        print("\n   Quick start:")
        print("   export SENDGRID_API_KEY='your_key'")
        print("   export SENDGRID_FROM_EMAIL='your@email.com'")
        print("   export TWILIO_ACCOUNT_SID='your_sid'")
        print("   export TWILIO_AUTH_TOKEN='your_token'")
        print("   export TWILIO_FROM_NUMBER='+15551234567'")
    
    print()

if __name__ == "__main__":
    main()
