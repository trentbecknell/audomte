#!/bin/bash
# Simple Twilio Setup Script
# This will guide you through setting up Twilio environment variables

echo "=========================================="
echo "  Twilio Environment Variables Setup"
echo "=========================================="
echo ""

# Check if variables are already set
if [ ! -z "$TWILIO_ACCOUNT_SID" ] && [ ! -z "$TWILIO_AUTH_TOKEN" ] && [ ! -z "$TWILIO_FROM_NUMBER" ]; then
    echo "✅ Twilio variables are already set!"
    echo "   Account SID: ${TWILIO_ACCOUNT_SID:0:8}..."
    echo "   From Number: $TWILIO_FROM_NUMBER"
    echo ""
    read -p "Do you want to reconfigure? (y/n): " reconfigure
    if [ "$reconfigure" != "y" ]; then
        echo "Configuration unchanged."
        exit 0
    fi
fi

echo "Let's set up your Twilio credentials!"
echo ""
echo "You'll need:"
echo "  1. Account SID (starts with 'AC')"
echo "  2. Auth Token (32 characters)"
echo "  3. Your Twilio phone number (format: +15551234567)"
echo ""
echo "Find these at: https://console.twilio.com/"
echo ""
read -p "Press Enter when ready..."

echo ""
echo "=========================================="
echo ""

# Get Account SID
read -p "Enter your TWILIO_ACCOUNT_SID (starts with AC): " account_sid

# Get Auth Token
read -p "Enter your TWILIO_AUTH_TOKEN: " auth_token

# Get Phone Number
echo ""
echo "Phone number format: +15551234567 (no spaces or dashes)"
read -p "Enter your TWILIO_FROM_NUMBER: " from_number

# Clean up phone number (remove spaces and dashes)
from_number=$(echo "$from_number" | tr -d ' -')

# Add + if missing
if [[ ! "$from_number" =~ ^\+ ]]; then
    from_number="+$from_number"
fi

echo ""
echo "=========================================="
echo "  Your Configuration:"
echo "=========================================="
echo "  TWILIO_ACCOUNT_SID: ${account_sid:0:8}...${account_sid: -4}"
echo "  TWILIO_AUTH_TOKEN: [hidden]"
echo "  TWILIO_FROM_NUMBER: $from_number"
echo ""

read -p "Does this look correct? (y/n): " confirm

if [ "$confirm" != "y" ]; then
    echo "Setup cancelled. Please run the script again."
    exit 1
fi

echo ""
echo "=========================================="
echo "  Choose setup method:"
echo "=========================================="
echo "  1. Export in terminal (temporary - this session only)"
echo "  2. Add to ~/.bashrc (permanent for all terminals)"
echo "  3. Create .env file (recommended for this project)"
echo ""
read -p "Enter your choice (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "Setting variables for this terminal session..."
        export TWILIO_ACCOUNT_SID="$account_sid"
        export TWILIO_AUTH_TOKEN="$auth_token"
        export TWILIO_FROM_NUMBER="$from_number"
        echo "✅ Variables set!"
        echo ""
        echo "⚠️  Remember: These will be lost when you close this terminal."
        echo "    You can add them to ~/.bashrc for persistence."
        ;;
    2)
        echo ""
        echo "Adding to ~/.bashrc..."
        echo "" >> ~/.bashrc
        echo "# Twilio Configuration" >> ~/.bashrc
        echo "export TWILIO_ACCOUNT_SID=\"$account_sid\"" >> ~/.bashrc
        echo "export TWILIO_AUTH_TOKEN=\"$auth_token\"" >> ~/.bashrc
        echo "export TWILIO_FROM_NUMBER=\"$from_number\"" >> ~/.bashrc
        echo "✅ Added to ~/.bashrc"
        echo ""
        echo "Reload your shell:"
        echo "  source ~/.bashrc"
        ;;
    3)
        echo ""
        echo "Creating .env file..."
        
        # Create or append to .env
        if [ -f .env ]; then
            echo "⚠️  .env file already exists. Backing up to .env.backup"
            cp .env .env.backup
            # Remove old Twilio variables
            sed -i '/^TWILIO_/d' .env
        fi
        
        echo "" >> .env
        echo "# Twilio Configuration" >> .env
        echo "TWILIO_ACCOUNT_SID=$account_sid" >> .env
        echo "TWILIO_AUTH_TOKEN=$auth_token" >> .env
        echo "TWILIO_FROM_NUMBER=$from_number" >> .env
        
        echo "✅ Saved to .env file"
        echo ""
        echo "Make sure you have python-dotenv installed:"
        echo "  pip install python-dotenv"
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "  ✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Verify configuration: python check_config.py"
echo "  2. Restart the server: ./start_server.sh"
echo "  3. Test by sending an SMS!"
echo ""
echo "⚠️  Trial Account Note:"
echo "  You can only send to verified phone numbers."
echo "  Verify at: https://console.twilio.com/"
echo ""
