#!/usr/bin/env python3
"""
Phone Number Validator and Formatter
Helps ensure phone numbers are in correct E.164 format for Twilio
"""

import re

def format_phone_number(phone: str, default_country_code: str = "+1") -> str:
    """
    Format a phone number to E.164 format.
    
    Args:
        phone: Input phone number in any common format
        default_country_code: Country code to use if not provided (default: +1 for US)
    
    Returns:
        Phone number in E.164 format (+1XXXXXXXXXX)
    """
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # If it starts with 1 and has 11 digits, it's a US number
    if len(digits_only) == 11 and digits_only.startswith('1'):
        return f"+{digits_only}"
    
    # If it has 10 digits, assume US and add country code
    elif len(digits_only) == 10:
        return f"{default_country_code}{digits_only}"
    
    # If it already looks like it has a country code
    elif len(digits_only) > 10:
        return f"+{digits_only}"
    
    # Otherwise, return as-is with warning
    else:
        print(f"⚠️  Warning: Phone number '{phone}' may be invalid (only {len(digits_only)} digits)")
        return f"{default_country_code}{digits_only}"

def validate_phone_number(phone: str) -> tuple[bool, str]:
    """
    Validate if a phone number is in correct E.164 format.
    
    Returns:
        (is_valid, error_message)
    """
    # Must start with +
    if not phone.startswith('+'):
        return False, "Phone number must start with '+' (country code)"
    
    # Remove the + and check if rest is all digits
    digits = phone[1:]
    if not digits.isdigit():
        return False, "Phone number can only contain digits after '+'"
    
    # Must be between 10-15 digits (E.164 standard)
    if len(digits) < 10:
        return False, f"Phone number too short ({len(digits)} digits, need at least 10)"
    
    if len(digits) > 15:
        return False, f"Phone number too long ({len(digits)} digits, max is 15)"
    
    return True, "Valid E.164 format"

def test_format_phone():
    """Test the formatting function with various inputs"""
    test_numbers = [
        "978-338-7220",
        "(978) 338-7220",
        "9783387220",
        "+19783387220",
        "1-978-338-7220",
        "+1 978 338 7220",
        "978.338.7220",
    ]
    
    print("=" * 60)
    print("Phone Number Formatting Test")
    print("=" * 60)
    
    for number in test_numbers:
        formatted = format_phone_number(number)
        is_valid, message = validate_phone_number(formatted)
        status = "✅" if is_valid else "❌"
        print(f"\n{status} Input:  {number}")
        print(f"   Output: {formatted}")
        print(f"   {message}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Format the provided phone number
        input_phone = sys.argv[1]
        formatted = format_phone_number(input_phone)
        is_valid, message = validate_phone_number(formatted)
        
        print(f"\nInput:  {input_phone}")
        print(f"Output: {formatted}")
        print(f"Status: {message}")
        
        if is_valid:
            print("\n✅ Ready to use with Twilio!")
        else:
            print("\n❌ Not valid - please check the format")
    else:
        # Run tests
        test_format_phone()
        print("\nUsage: python validate_phone.py '+19781234567'")
