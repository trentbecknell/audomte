# Phone Masking Service

## Overview
The phone masking service provides privacy protection by allowing clients to use proxy/masked phone numbers instead of exposing their real phone numbers when receiving SMS messages.

## How It Works

### For Studio Owners
When creating a client, you can enable "Phone Masking" which will:
1. Generate a unique masked phone number for that client
2. Store the mapping between the real phone and masked phone
3. Automatically route all SMS messages through the masked number

### Architecture
- **PhoneMaskingAdapter**: Core service that manages masked phone numbers
- **Database Table**: `masked_phones` stores the mapping between real and masked numbers
- **Automatic Routing**: All SMS messages check if masking is enabled and route accordingly

## Integration Points

### Production Services
This prototype simulates phone masking. In production, you would integrate with:

- **Twilio Proxy**: https://www.twilio.com/docs/proxy
- **Bandwidth Phone Number Masking**: https://www.bandwidth.com/
- **Plivo Mask**: https://www.plivo.com/docs/voice/concepts/masked-calling/

## API Endpoints

### Get Masked Phone for Client
```bash
GET /clients/{client_id}/masked-phone
```

### Create Masked Phone for Client
```bash
POST /clients/{client_id}/masked-phone
```

### Delete Masked Phone (Release Number)
```bash
DELETE /clients/{client_id}/masked-phone
```

## Configuration

Set environment variables to configure the service:

```bash
# Enable/disable phone masking
export PHONE_MASKING_ENABLED=true

# Choose provider (for logging/future integration)
export PHONE_MASKING_PROVIDER=twilio  # or bandwidth, plivo

# Pool number for masking (production would use actual pool)
export MASKING_POOL_NUMBER="+1-555-PROXY"
```

## Database Schema

```sql
CREATE TABLE masked_phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL UNIQUE,
    real_phone TEXT NOT NULL,
    masked_phone TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(client_id) REFERENCES clients(id)
);
```

## Privacy Benefits

1. **Client Privacy**: Clients' real phone numbers are never exposed to the studio
2. **Studio Privacy**: Studio's real phone numbers can be protected
3. **Number Portability**: Easy to change backend numbers without affecting clients
4. **Audit Trail**: Track all communications through masked numbers
5. **Compliance**: Helps meet privacy regulations (GDPR, CCPA, etc.)

## Testing

When testing locally, masked numbers are simulated with format:
- `+1-555-MASK-XXXX` (where XXXX is a random 4-digit suffix)

In production, these would be real phone numbers from your masking provider's pool.

## Example Usage

1. Create a client with phone masking enabled
2. System generates masked number: `+1-555-MASK-1234`
3. Client sees/uses: `+1-555-MASK-1234`
4. Messages automatically route to real number
5. Privacy maintained for both parties
