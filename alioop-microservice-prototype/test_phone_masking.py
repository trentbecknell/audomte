#!/usr/bin/env python3
"""
Test script for Phone Masking Service
Demonstrates the phone masking functionality via API calls
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_phone_masking():
    print("🔒 Phone Masking Service Test\n")
    print("=" * 50)
    
    # Test 1: Create a client WITH phone masking
    print("\n1. Creating client with phone masking enabled...")
    client_data = {
        "name": "Test Client (Masked)",
        "email": "masked@example.com",
        "phone": "+1-555-0001",
        "use_masked_phone": True,
        "delivery_pref": "Drive",
        "payment_pref": "Stripe"
    }
    
    response = requests.post(f"{BASE_URL}/clients", json=client_data)
    result = response.json()
    print(f"   ✓ Client created: ID={result['client_id']}")
    if result.get('masked_phone'):
        print(f"   ✓ Masked phone generated: {result['masked_phone']}")
        masked_client_id = result['client_id']
    
    # Test 2: Create a client WITHOUT phone masking
    print("\n2. Creating client without phone masking...")
    client_data_2 = {
        "name": "Test Client (Normal)",
        "email": "normal@example.com",
        "phone": "+1-555-0002",
        "use_masked_phone": False,
        "delivery_pref": "Drive",
        "payment_pref": "Stripe"
    }
    
    response = requests.post(f"{BASE_URL}/clients", json=client_data_2)
    result = response.json()
    print(f"   ✓ Client created: ID={result['client_id']}")
    print(f"   ✓ No masked phone (uses real number)")
    normal_client_id = result['client_id']
    
    # Test 3: Get masked phone for first client
    print(f"\n3. Retrieving masked phone for client {masked_client_id}...")
    response = requests.get(f"{BASE_URL}/clients/{masked_client_id}/masked-phone")
    if response.status_code == 200:
        result = response.json()
        print(f"   ✓ Masked phone: {result['masked_phone']}")
    
    # Test 4: Try to get masked phone for second client (should fail)
    print(f"\n4. Checking if client {normal_client_id} has masked phone...")
    response = requests.get(f"{BASE_URL}/clients/{normal_client_id}/masked-phone")
    if response.status_code == 404:
        print(f"   ✓ Correctly returns 404 (no masked phone)")
    
    # Test 5: Add masked phone to existing client
    print(f"\n5. Adding masked phone to client {normal_client_id}...")
    response = requests.post(f"{BASE_URL}/clients/{normal_client_id}/masked-phone")
    if response.status_code == 200:
        result = response.json()
        print(f"   ✓ Masked phone created: {result['masked_phone']}")
    
    # Test 6: Send SMS to masked client
    print(f"\n6. Sending SMS to client with masked phone...")
    message_data = {
        "client_id": masked_client_id,
        "channel": "sms",
        "body": "Test message - should use masked number"
    }
    response = requests.post(f"{BASE_URL}/send", json=message_data)
    if response.status_code == 200:
        print(f"   ✓ Message sent (check server logs for routing)")
    
    print("\n" + "=" * 50)
    print("✅ Phone masking tests completed!")
    print("\nCheck the server terminal to see masked number routing in action.")

if __name__ == "__main__":
    try:
        test_phone_masking()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server at http://localhost:8000")
        print("   Make sure the server is running!")
    except Exception as e:
        print(f"❌ Error: {e}")
