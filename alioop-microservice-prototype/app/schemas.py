from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientCreate(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    delivery_pref: str = "Drive"         # Drive | Dropbox | WeTransfer | Custom
    delivery_custom_url: Optional[str] = None
    payment_pref: str = "Stripe"         # Stripe | PayPal | Zelle | Custom
    payment_custom_url: Optional[str] = None
    use_masked_phone: bool = False       # Whether to use phone masking service

class ClientUpdate(ClientCreate):
    pass

class ProjectCreate(BaseModel):
    client_id: int
    title: str
    notes: Optional[str] = None

class MessageSend(BaseModel):
    client_id: int
    channel: str  # email | sms
    body: str
