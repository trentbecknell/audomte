#!/usr/bin/env python3
"""
Interactive Twilio Setup Assistant
Helps you configure Twilio for SMS messaging step-by-step
"""

import os
import sys

def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_step(number, text):
    print(f"\n📌 Step {number}: {text}")

def print_success(text):
    print(f"✅ {text}")

def print_info(text):
    print(f"ℹ️  {text}")

def print_warning(text):
    print(f"⚠️  {text}")

def get_input(prompt):
    return input(f"\n{prompt}: ").strip()

def main():
    print_header("🚀 Twilio SMS Setup Assistant")
    
    print("\nThis guide will help you:")
    print("  1. Get your Twilio credentials")
    print("  2. Set up environment variables")
    print("  3. Test your configuration")
    
    input("\nPress Enter to continue...")
    
    # Step 1: Check if already configured
    print_step(1, "Checking Current Configuration")
    
    existing_sid = os.getenv("TWILIO_ACCOUNT_SID")
    existing_token = os.getenv("TWILIO_AUTH_TOKEN")
    existing_number = os.getenv("TWILIO_FROM_NUMBER")
    
    if existing_sid and existing_token and existing_number:
        print_success("Twilio is already configured!")
        print(f"  Account SID: {existing_sid[:8]}...")
        print(f"  From Number: {existing_number}")
        
        reconfigure = get_input("Want to reconfigure? (y/n)").lower()
        if reconfigure != 'y':
            print("\n✅ Configuration looks good! Test it in the app.")
            return
    else:
        print_info("No Twilio configuration found. Let's set it up!")
    
    # Step 2: Get Twilio account
    print_step(2, "Create/Access Your Twilio Account")
    
    print("\n  If you don't have a Twilio account:")
    print("  1. Go to: https://www.twilio.com/try-twilio")
    print("  2. Sign up (it's free!)")
    print("  3. Verify your phone number")
    print("  4. You'll get free trial credits")
    
    has_account = get_input("\nDo you have a Twilio account? (y/n)").lower()
    
    if has_account != 'y':
        print("\n🌐 Opening Twilio signup page...")
        print("   URL: https://www.twilio.com/try-twilio")
        print("\n   After signing up, come back here and rerun this script.")
        return
    
    # Step 3: Find credentials
    print_step(3, "Get Your Twilio Credentials")
    
    print("\n  To find your credentials:")
    print("  1. Go to: https://console.twilio.com/")
    print("  2. Log in to your account")
    print("  3. Look at the main dashboard")
    print("  4. You'll see 'Account Info' section with:")
    print("     - Account SID (starts with 'AC')")
    print("     - Auth Token (click to reveal)")
    
    input("\n  Press Enter when you're ready to enter your credentials...")
    
    # Get Account SID
    print("\n" + "-" * 60)
    account_sid = get_input("Enter your ACCOUNT SID (starts with AC)")
    
    if not account_sid.startswith("AC"):
        print_warning("Account SID should start with 'AC'. Please double-check.")
        confirm = get_input("Continue anyway? (y/n)").lower()
        if confirm != 'y':
            print("Setup cancelled. Please try again.")
            return
    
    # Get Auth Token
    auth_token = get_input("Enter your AUTH TOKEN (click 'show' in console to reveal)")
    
    if len(auth_token) < 20:
        print_warning("Auth token seems short. Please double-check it's correct.")
    
    # Step 4: Get phone number
    print_step(4, "Get Your Twilio Phone Number")
    
    print("\n  To get a phone number:")
    print("  1. In Twilio Console, go to: Phone Numbers → Manage → Buy a number")
    print("  2. Or if you already have one: Phone Numbers → Manage → Active numbers")
    print("  3. Choose a number with SMS capability")
    print("  4. Copy the phone number (e.g., +1-555-123-4567)")
    
    print("\n  ⚠️  IMPORTANT: Use E.164 format!")
    print("     ✅ Correct: +15551234567")
    print("     ❌ Wrong: (555) 123-4567 or 555-123-4567")
    
    from_number = get_input("\nEnter your Twilio phone number (with +1)")
    
    # Validate phone number format
    if not from_number.startswith("+"):
        print_warning("Phone number should start with '+'. Let me fix that...")
        from_number = "+" + from_number.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    
    # Remove any formatting
    from_number = from_number.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    
    print_info(f"Formatted number: {from_number}")
    
    # Step 5: Verify credentials
    print_step(5, "Testing Your Credentials")
    
    print("\n  Let me verify these credentials work...")
    
    try:
        from twilio.rest import Client
        
        print("  • Creating Twilio client...")
        client = Client(account_sid, auth_token)
        
        print("  • Fetching account info...")
        account = client.api.accounts(account_sid).fetch()
        
        print_success(f"Connected! Account: {account.friendly_name}")
        print_success("Credentials are valid!")
        
    except ImportError:
        print_warning("Twilio library not found. Install it with: pip install twilio")
        print_info("Credentials saved, but couldn't test them.")
    except Exception as e:
        print_warning(f"Could not verify credentials: {e}")
        print_info("This might be okay - they'll be tested when you send a message.")
        
        proceed = get_input("\nContinue anyway? (y/n)").lower()
        if proceed != 'y':
            print("Setup cancelled.")
            return
    
    # Step 6: Set environment variables
    print_step(6, "Setting Environment Variables")
    
    print("\n  Choose how to configure:")
    print("  1. Export commands (temporary - for this terminal session)")
    print("  2. Create .env file (persistent - recommended)")
    print("  3. Both (belt and suspenders!)")
    
    choice = get_input("\nEnter your choice (1/2/3)").strip()
    
    if choice in ['1', '3']:
        print("\n  📋 Copy and paste these commands:")
        print(f"\n  export TWILIO_ACCOUNT_SID=\"{account_sid}\"")
        print(f"  export TWILIO_AUTH_TOKEN=\"{auth_token}\"")
        print(f"  export TWILIO_FROM_NUMBER=\"{from_number}\"")
        print("\n  Then restart your server: ./start_server.sh")
        input("\n  Press Enter after running the commands...")
    
    if choice in ['2', '3']:
        env_file = ".env"
        
        # Read existing .env if it exists
        env_content = ""
        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                env_content = f.read()
        
        # Add/update Twilio variables
        lines = env_content.split('\n')
        new_lines = []
        twilio_vars = {
            'TWILIO_ACCOUNT_SID': account_sid,
            'TWILIO_AUTH_TOKEN': auth_token,
            'TWILIO_FROM_NUMBER': from_number
        }
        
        # Remove existing Twilio vars
        for line in lines:
            if not any(line.startswith(var) for var in twilio_vars.keys()):
                new_lines.append(line)
        
        # Add new Twilio vars
        new_lines.append("\n# Twilio Configuration")
        for key, value in twilio_vars.items():
            new_lines.append(f"{key}={value}")
        
        with open(env_file, 'w') as f:
            f.write('\n'.join(new_lines))
        
        print_success(f"Saved to {env_file}")
        print_info("Note: You need python-dotenv to use .env files")
        print("      Install with: pip install python-dotenv")
    
    # Step 7: Verify trial account limitations
    print_step(7, "Important: Trial Account Limitations")
    
    print("\n  📱 Twilio Trial Account Notes:")
    print("  • You can only send to VERIFIED phone numbers")
    print("  • Messages will include 'Sent from your Twilio trial account'")
    print("  • You have limited free credits")
    
    print("\n  To verify a phone number:")
    print("  1. Go to: Phone Numbers → Manage → Verified Caller IDs")
    print("  2. Click 'Add a new Caller ID'")
    print("  3. Enter the phone number you want to text")
    print("  4. Complete the verification (you'll get a code via SMS)")
    
    print_info("\n  Upgrade to a paid account to remove these limitations.")
    
    # Final summary
    print_header("🎉 Setup Complete!")
    
    print("\n✅ Your Twilio configuration:")
    print(f"   Account SID: {account_sid[:8]}...{account_sid[-4:]}")
    print(f"   From Number: {from_number}")
    
    print("\n📋 Next Steps:")
    print("   1. Verify recipient phone numbers (if on trial)")
    print("   2. Restart your server: ./start_server.sh")
    print("   3. Check config: python check_config.py")
    print("   4. Test by sending an SMS through the app!")
    
    print("\n💡 Tips:")
    print("   • Use your verified number as recipient for testing")
    print("   • Check Twilio console for detailed logs")
    print("   • Monitor your usage at: https://console.twilio.com/")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("Please try again or check REAL_MESSAGING_SETUP.md for manual setup.")
