from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

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

class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    default_price: float
    is_active: bool = True

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    default_price: Optional[float] = None
    is_active: Optional[bool] = None

class DeliveryCreate(BaseModel):
    client_id: int
    project_id: Optional[int] = None
    service_id: int
    filename: str
    file_path: str
    file_size: Optional[int] = None
    price: float
    max_downloads: int = 3
    
class DeliveryUpdate(BaseModel):
    status: Optional[str] = None
    payment_method: Optional[str] = None
    payment_confirmed: Optional[bool] = None

class FileUploadRequest(BaseModel):
    client_id: int
    service_id: int
    custom_price: Optional[float] = None
    project_id: Optional[int] = None
    notes: Optional[str] = None

