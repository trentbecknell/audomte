# Audio Delivery Micro-SaaS

## 🎯 User Journeys

### Engineer Journey
1. **Drop file** → Place finished audio file in watched folder
2. **Select customer** → Pick from list of existing clients  
3. **Choose service** → Mixing/Mastering/Production/Custom
4. **Set price** → Use default or enter custom amount
5. **Done!** → Customer automatically notified via email/SMS

### Customer Journey
1. **Receive notification** → Email/SMS with download link
2. **Click link** → Secure token-based download page (no login)
3. **Download file** → Up to 3 downloads, 30-day expiry
4. **Choose payment method** → Zelle/PayPal/CashApp/Venmo
5. **Click "I Paid"** → Engineer gets notification to verify
6. **Confirmation** → Payment marked as verified

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Payment Handles

Edit `templates/delivery.html` and update your payment info:

```html
<!-- Line ~137-150 -->
<div class="handle" id="zelle-handle">your@email.com</div>
<div class="handle" id="paypal-handle">paypal.me/yourhandle</div>
<div class="handle" id="cashapp-handle">$YourCashApp</div>
<div class="handle" id="venmo-handle">@YourVenmo</div>
```

### 3. Start the Web Server

```bash
uvicorn app.main:app --reload
```

Web UI: http://localhost:8000

### 4. Add Your Clients

1. Open http://localhost:8000
2. Click "New Client"  
3. Enter name, email, and/or phone number
4. Save

### 5. Start the File Watcher

In a **separate terminal**:

```bash
python file_watcher.py
```

### 6. Drop Audio Files

Drop finished audio files into:
```
~/Desktop/AudioDeliveries/
```

The file watcher will:
- Detect the new file
- Ask you to select the customer
- Ask you to select the service type
- Allow price customization
- Upload file to secure storage
- Send notification to customer
- Move original file to `_processed` folder

---

## 📁 File Structure

```
alioop-microservice-prototype/
├── app/
│   ├── main.py              # FastAPI app with delivery endpoints
│   ├── db.py                # Database with services & deliveries tables
│   ├── schemas.py           # Pydantic models for API
│   └── adapters/
│       ├── messaging.py     # Email/SMS integration
│       └── payments.py      # Payment link resolver
├── templates/
│   ├── index.html           # Main admin UI
│   └── delivery.html        # Customer download page ⭐ NEW
├── storage/
│   └── deliveries/          # Uploaded audio files (gitignored)
├── file_watcher.py          # Desktop file monitoring service ⭐ NEW
└── requirements.txt         # Python dependencies
```

---

## 💰 Service Pricing (Default)

| Service | Default Price | Customizable |
|---------|--------------|--------------|
| Mixing | $150.00 | ✅ Yes |
| Mastering | $100.00 | ✅ Yes |
| Production | $500.00 | ✅ Yes |
| Stem Mix | $200.00 | ✅ Yes |
| Revisions | $50.00 | ✅ Yes |
| Custom | Quote | ✅ Yes |

You can override prices when processing each file.

---

## 🎛️ API Endpoints

### Service Management

- `GET /services` - List all active services
- `POST /services` - Create new service type
- `PATCH /services/{id}` - Update pricing/details

### Customer Download

- `GET /delivery/{token}` - Customer download page
- `GET /delivery/{token}/download` - Download file (increments counter)
- `POST /delivery/{token}/confirm-payment` - Customer payment confirmation

### Admin

- `GET /admin/deliveries` - List all deliveries
- `GET /admin/deliveries?status=payment_pending` - Filter by status
- `POST /admin/deliveries/{id}/verify-payment` - Confirm payment received

---

## 🔒 Security Features

- ✅ **Secure tokens** - 32-byte random tokens for download links
- ✅ **Download limits** - Max 3 downloads per delivery
- ✅ **Expiry** - Links expire after 30 days
- ✅ **No login required** - Token-based access for customers
- ✅ **Storage isolation** - Files stored outside web root

---

## 🎵 Supported Audio Formats

- `.wav` - Uncompressed audio
- `.mp3` - Compressed audio
- `.flac` - Lossless compression
- `.aiff` - Apple audio format
- `.m4a` - AAC audio
- `.ogg` - Ogg Vorbis
- `.aac` - Advanced Audio Coding
- `.wma` - Windows Media Audio

---

## 📊 Delivery Statuses

| Status | Meaning |
|--------|---------|
| `pending` | File uploaded, not yet notified |
| `notified` | Customer has been sent the link |
| `downloaded` | Customer has downloaded the file |
| `payment_pending` | Customer clicked "I Paid" |
| `paid` | Engineer verified payment |
| `expired` | Download link expired |

---

## 🔧 Configuration

### Watch Folder Location

Edit `file_watcher.py` line 18:

```python
WATCH_FOLDER = Path.home() / "Desktop" / "AudioDeliveries"
```

Change to any folder you prefer.

### Download Limits

Edit `file_watcher.py` line 20:

```python
MAX_DOWNLOADS = 3  # Change to allow more downloads
```

### Link Expiry

Edit `file_watcher.py` line 19:

```python
TOKEN_EXPIRY_DAYS = 30  # Change expiry duration
```

---

## 💡 Usage Tips

### For Engineers

1. **Batch Processing**: Drop multiple files - process one at a time
2. **Custom Pricing**: Override default prices for special deals
3. **Verify Payments**: Check `/admin/deliveries?status=payment_pending` daily
4. **Organized**: Original files auto-move to `_processed` folder

### For Customers

1. **Download Soon**: Links expire in 30 days
2. **Save Locally**: Only 3 downloads allowed
3. **Payment**: Copy payment handle by clicking on it
4. **Questions**: Contact engineer directly

---

## 🎯 Future Enhancements

- [ ] Email notifications for engineers when payments are received
- [ ] Automatic payment verification via Zelle/PayPal webhooks
- [ ] Drag-and-drop web upload (alternative to file watcher)
- [ ] Custom email templates per service type
- [ ] Analytics dashboard for revenue tracking
- [ ] Bulk delivery creation
- [ ] Customer portal for delivery history

---

## 🐛 Troubleshooting

**File watcher not detecting files?**
- Ensure the watch folder exists: `~/Desktop/AudioDeliveries/`
- Check file permissions
- Try restarting the file watcher

**Customer can't download?**
- Check link hasn't expired (30 days)
- Verify download limit not reached (3 max)
- Check file still exists in storage folder

**Notifications not sending?**
- Verify `.env` file has SendGrid/Twilio credentials
- Check client has email or phone number
- Review logs for error messages

---

## 📝 Example Workflow

```bash
# Terminal 1: Start web server
uvicorn app.main:app --reload

# Terminal 2: Start file watcher  
python file_watcher.py

# Engineer drops file:
cp ~/Downloads/ClientTrack_Master.wav ~/Desktop/AudioDeliveries/

# File watcher prompts:
👤 SELECT CLIENT:
  1. John Doe (john@example.com)
  2. Jane Smith (jane@example.com)
Enter client number: 1

🎛️  SELECT SERVICE for John Doe:
  1. Mixing - $150.00
  2. Mastering - $100.00
  3. Production - $500.00
Enter service number: 2

Price is $100.00. Press Enter to confirm or enter custom price: $

📦 Processing delivery...
📧 Notifying customer...
   ✅ Email sent to john@example.com
✅ Customer notified successfully!
   Download link: http://localhost:8000/delivery/abc123...
📁 Original file moved to: ~/Desktop/AudioDeliveries/_processed/ClientTrack_Master.wav

# Customer receives email, clicks link, downloads, and pays
# Engineer verifies payment:
curl -X POST http://localhost:8000/admin/deliveries/1/verify-payment
```

---

**Built for audio engineers who want to focus on music, not admin work** 🎵✨
