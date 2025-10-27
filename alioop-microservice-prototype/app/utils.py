"""
Phone number utility functions for formatting and validation
"""
import re
from typing import Optional

def format_phone_number(phone: str, default_country_code: str = "1") -> str:
    """
    Format a phone number to E.164 format.
    Accepts any common format and converts to +1XXXXXXXXXX
    
    Args:
        phone: Input phone number in any format
        default_country_code: Country code without + (default: "1" for US)
    
    Returns:
        Phone number in E.164 format
    """
    if not phone:
        return phone
    
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # If it starts with the country code and has correct length
    if digits_only.startswith(default_country_code) and len(digits_only) == 11:
        return f"+{digits_only}"
    
    # If it has 10 digits, add country code
    elif len(digits_only) == 10:
        return f"+{default_country_code}{digits_only}"
    
    # If it has more than 10 digits, assume country code is included
    elif len(digits_only) > 10:
        return f"+{digits_only}"
    
    # Return what we have with country code
    return f"+{default_country_code}{digits_only}"

def validate_e164_format(phone: str) -> bool:
    """
    Validate if phone number is in E.164 format.
    
    Returns:
        True if valid E.164 format, False otherwise
    """
    if not phone:
        return False
    
    # Must start with +
    if not phone.startswith('+'):
        return False
    
    # Remove + and check if rest is digits
    digits = phone[1:]
    if not digits.isdigit():
        return False
    
    # Must be between 10-15 digits
    return 10 <= len(digits) <= 15
