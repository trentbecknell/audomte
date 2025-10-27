import os
import random
import string
from typing import Optional

class PhoneMaskingAdapter:
    """
    Phone masking service adapter to provide proxy phone numbers.
    In production, this would integrate with services like:
    - Twilio Proxy
    - Bandwidth Masking
    - Plivo Mask
    """
    
    def __init__(self):
        self.service_enabled = os.getenv("PHONE_MASKING_ENABLED", "true").lower() == "true"
        self.masking_provider = os.getenv("PHONE_MASKING_PROVIDER", "twilio")  # twilio | bandwidth | plivo
        self.pool_number = os.getenv("MASKING_POOL_NUMBER", "+1-555-PROXY")
        
    def generate_masked_number(self, real_phone: str, client_id: int) -> str:
        """
        Generate a masked phone number for a client.
        In production, this would call the masking service API.
        For now, generates a simulated masked number.
        """
        if not self.service_enabled:
            return real_phone
            
        # Simulate generating a masked number from a pool
        # In production: Call provider API to allocate from pool
        suffix = ''.join(random.choices(string.digits, k=4))
        masked = f"+1-555-MASK-{suffix}"
        
        print(f"[PHONE_MASK:{self.masking_provider.upper()}] Generated masked number {masked} for client {client_id}")
        return masked
    
    def get_masked_number(self, client_id: int, from_db_func) -> Optional[str]:
        """
        Retrieve existing masked number for a client from database.
        """
        if not self.service_enabled:
            return None
            
        conn = from_db_func()
        cur = conn.cursor()
        cur.execute("SELECT masked_phone FROM masked_phones WHERE client_id=?", (client_id,))
        row = cur.fetchone()
        conn.close()
        
        if row:
            return row["masked_phone"]
        return None
    
    def create_phone_mask(self, client_id: int, real_phone: str, from_db_func) -> str:
        """
        Create and store a new phone mask for a client.
        """
        # Check if mask already exists
        existing = self.get_masked_number(client_id, from_db_func)
        if existing:
            return existing
            
        # Generate new masked number
        masked_phone = self.generate_masked_number(real_phone, client_id)
        
        # Store in database
        conn = from_db_func()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO masked_phones (client_id, real_phone, masked_phone)
            VALUES (?, ?, ?)
        ''', (client_id, real_phone, masked_phone))
        conn.commit()
        conn.close()
        
        return masked_phone
    
    def route_message(self, masked_or_real_phone: str, body: str, from_db_func) -> dict:
        """
        Route a message through the masking service.
        If the number is masked, resolve it to the real number.
        Returns the real phone number and routing info.
        """
        if not self.service_enabled:
            return {"real_phone": masked_or_real_phone, "was_masked": False}
        
        # Check if this is a masked number
        conn = from_db_func()
        cur = conn.cursor()
        cur.execute("SELECT real_phone FROM masked_phones WHERE masked_phone=?", (masked_or_real_phone,))
        row = cur.fetchone()
        conn.close()
        
        if row:
            print(f"[PHONE_MASK:ROUTE] Routing masked {masked_or_real_phone} -> real {row['real_phone']}")
            return {"real_phone": row["real_phone"], "was_masked": True}
        
        return {"real_phone": masked_or_real_phone, "was_masked": False}
    
    def delete_phone_mask(self, client_id: int, from_db_func) -> bool:
        """
        Delete a phone mask for a client (releases the masked number back to pool).
        """
        if not self.service_enabled:
            return False
            
        conn = from_db_func()
        cur = conn.cursor()
        cur.execute("DELETE FROM masked_phones WHERE client_id=?", (client_id,))
        deleted = cur.rowcount > 0
        conn.commit()
        conn.close()
        
        if deleted:
            print(f"[PHONE_MASK:DELETE] Released masked number for client {client_id}")
        
        return deleted
