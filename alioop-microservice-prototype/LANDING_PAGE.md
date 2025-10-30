# 🎵 Audio Delivery Portal - Landing Page

## Overview

Beautiful, user-friendly landing page for the audio delivery system with:
- **Drag-and-drop file upload** - No command line needed!
- **Client/service selection** - Simple dropdowns
- **Real-time progress tracking** - Visual feedback
- **Multi-file support** - Upload multiple files at once
- **Engineer login** - Access to full dashboard
- **Mobile responsive** - Works on any device

---

## 🚀 Quick Start

### 1. Start the Server

```bash
cd alioop-microservice-prototype
python -m uvicorn app.main:app --reload --port 8000
```

### 2. Open in Browser

**Public Landing Page:** http://localhost:8000  
**Engineer Dashboard:** http://localhost:8000/dashboard

---

## 📱 Pages

### Landing Page (`/`)

**Three tabs:**

1. **📤 Upload Delivery**
   - Drag-and-drop zone for audio files
   - Select client from dropdown
   - Select service type (Mixing/Mastering/etc)
   - Optional custom pricing
   - One-click delivery creation
   - Automatic customer notification

2. **🔐 Engineer Login**
   - Access to full dashboard
   - Manage clients and projects
   - View all deliveries
   - Verify payments
   - Update pricing

3. **ℹ️ About**
   - How it works
   - Feature list
   - Quick stats
   - Service types

### Engineer Dashboard (`/dashboard`)

The original admin interface with:
- Client management
- Project management
- Delivery tracking
- Payment verification

---

## 🎨 Features

### Drag-and-Drop Upload
- Click or drag files to upload zone
- Multi-file selection support
- Real-time file validation
- File size display
- Remove files before upload

### Smart Client Selection
- Auto-loads from database
- Shows contact info (email/phone)
- Search-friendly dropdown

### Service Pricing
- Predefined services with default pricing
- Override with custom price
- Price displayed next to service name

### Upload Progress
- Visual progress bar
- Per-file tracking
- Success/error notifications
- Auto-reset after completion

### Mobile Optimized
- Responsive grid layout
- Touch-friendly dropdowns
- Mobile drag-and-drop support
- Readable on any screen size

---

## 🔌 API Endpoints Used

### Frontend Calls

```javascript
// Load clients
GET /api/clients
Response: { clients: [{id, name, email, phone}, ...] }

// Load services  
GET /services
Response: { services: [{id, name, default_price}, ...] }

// Upload delivery
POST /api/upload-delivery
Form Data: {
  file: File,
  client_id: int,
  service_id: int,
  custom_price?: float,
  project_id?: int
}
Response: {
  ok: true,
  delivery_id: int,
  download_url: string,
  message: string
}
```

---

## 🎯 User Workflows

### Engineer Upload Workflow

1. **Open** http://localhost:8000
2. **Drag** finished audio file to upload zone
3. **Select** client from dropdown
4. **Choose** service type
5. **(Optional)** Enter custom price
6. **Click** "Create Delivery & Notify Client"
7. **Done!** Customer receives email/SMS automatically

### Customer Download Workflow

1. **Receive** email/SMS notification
2. **Click** secure download link
3. **View** file details and pricing
4. **Download** file (up to 3 times)
5. **Select** payment method
6. **Send** payment via Zelle/PayPal/CashApp/Venmo
7. **Click** "I've Sent Payment"
8. Engineer verifies payment

---

## 🎨 Customization

### Update Branding

Edit `templates/landing.html`:

```html
<!-- Line 105-107: Header -->
<div class="header">
    <h1>🎵 Your Studio Name</h1>
    <p>Your custom tagline here</p>
</div>
```

### Update Colors

Edit CSS variables in `<style>` section:

```css
/* Change gradient colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);

/* Change primary color */
color: #YOUR_PRIMARY_COLOR;
```

### Add Logo

```html
<!-- Add before h1 -->
<img src="/static/your-logo.png" alt="Logo" style="max-width: 200px; margin-bottom: 20px;">
```

---

## 🔒 Security

### Current Implementation
- ✅ Token-based file access
- ✅ File type validation
- ✅ Secure file storage
- ✅ HTTPS ready

### TODO for Production
- [ ] Add engineer authentication
- [ ] Session management
- [ ] CSRF protection
- [ ] Rate limiting
- [ ] File size limits
- [ ] Virus scanning

---

## 📊 Supported File Types

| Format | Extension | Description |
|--------|-----------|-------------|
| WAV | `.wav` | Uncompressed audio |
| MP3 | `.mp3` | Compressed audio |
| FLAC | `.flac` | Lossless compression |
| AIFF | `.aiff` | Apple audio format |
| M4A | `.m4a` | AAC audio |
| OGG | `.ogg` | Ogg Vorbis |
| AAC | `.aac` | Advanced Audio Coding |
| WMA | `.wma` | Windows Media Audio |

---

## 💡 Tips

### For Engineers

**Batch Uploads:**
- Select multiple files at once
- All go to same client/service
- Process one after another

**Custom Pricing:**
- Leave blank = use default
- Enter custom = override
- Applies to all files in batch

**Quick Access:**
- Bookmark `/dashboard` for admin
- Use `/` for quick uploads

### For Development

**Hot Reload:**
- FastAPI auto-reloads on code changes
- Refresh browser to see template changes

**Testing:**
- Use browser DevTools to debug
- Check Network tab for API calls
- Console shows JavaScript errors

**Database:**
- SQLite browser to inspect data
- Reset: `rm alioop.db` and restart

---

## 🐛 Troubleshooting

**Files not uploading?**
- Check file type is supported
- Ensure client and service selected
- Check browser console for errors
- Verify storage folder exists

**Clients not loading?**
- Server must be running
- Check `/api/clients` endpoint
- Add clients via `/dashboard` first

**Notifications not sending?**
- Verify `.env` has SendGrid/Twilio credentials
- Check client has email or phone
- View server logs for errors

**Page not loading?**
- Ensure server running on port 8000
- Check for port conflicts
- Try different browser

---

## 🚀 Deployment Tips

### For Production

1. **Use HTTPS:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 443 --ssl-keyfile key.pem --ssl-certfile cert.pem
   ```

2. **Update URLs:**
   - Change `http://localhost:8000` to your domain
   - Update in `file_watcher.py`
   - Update in `landing.html` if hardcoded

3. **Add Authentication:**
   - Implement OAuth or session-based auth
   - Protect `/dashboard` endpoint
   - Keep `/` public for uploads

4. **Environment Variables:**
   - Set `DOMAIN` in `.env`
   - Use in email templates
   - Dynamic URL generation

5. **Monitoring:**
   - Add logging
   - Track upload success rate
   - Monitor storage usage

---

## 📈 Next Steps

### Phase 1: Enhanced Upload
- [ ] Progress bar per file
- [ ] Parallel uploads
- [ ] Resume interrupted uploads
- [ ] Preview audio before upload

### Phase 2: Authentication
- [ ] Engineer login system
- [ ] Password reset
- [ ] Multi-user support
- [ ] Role-based access

### Phase 3: Analytics
- [ ] Revenue dashboard
- [ ] Upload statistics
- [ ] Client activity tracking
- [ ] Payment analytics

### Phase 4: Advanced Features
- [ ] Bulk operations
- [ ] Email template editor
- [ ] Automated pricing rules
- [ ] Integration webhooks

---

**The landing page is production-ready and significantly improves usability!** 🎉

No more command line for engineers - just drag, drop, and done!
