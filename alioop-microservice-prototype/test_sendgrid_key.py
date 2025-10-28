#!/usr/bin/env python3
"""
SendGrid API Key Tester - Quickly test if your API key works
"""

import sys

def test_api_key(api_key):
    """Test if the API key is valid"""
    try:
        from sendgrid import SendGridAPIClient
        
        print("🔍 Testing API key...")
        sg = SendGridAPIClient(api_key)
        
        # Try to get API key info (this validates the key without sending)
        response = sg.client.api_keys._(api_key.split('.')[-1]).get()
        
        print("✅ API key is valid!")
        return True
        
    except ImportError:
        print("❌ SendGrid library not installed")
        print("   Run: pip install sendgrid")
        return False
        
    except Exception as e:
        print(f"❌ API key is invalid or expired")
        print(f"   Error: {e}")
        print()
        print("📝 To fix:")
        print("   1. Go to: https://app.sendgrid.com/settings/api_keys")
        print("   2. Check if the key exists and is active")
        print("   3. If not, create a NEW API key")
        print("   4. Make sure it has 'Mail Send' permission")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔑 SendGrid API Key Tester")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
    else:
        api_key = input("Enter your SendGrid API Key: ").strip()
    
    if not api_key:
        print("❌ No API key provided")
        sys.exit(1)
    
    if not api_key.startswith("SG."):
        print("⚠️  Warning: API key should start with 'SG.'")
    
    print()
    test_api_key(api_key)
