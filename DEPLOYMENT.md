# Alioop Production Deployment

## 🚀 Automatic Deployment

This repository is configured for automatic deployment to production via GitHub Actions.

### Supported Platforms

#### Railway (Recommended)
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Zero-config deployments
- ✅ PostgreSQL database option

#### Render
- ✅ Free tier available
- ✅ Automatic SSL
- ✅ Simple setup

#### Fly.io
- ✅ Free tier
- ✅ Global CDN
- ✅ PostgreSQL included

---

## 📋 Setup Instructions

### Option 1: Deploy to Railway (Easiest)

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `trentbecknell/audomte`

3. **Configure Environment Variables**
   Add these in Railway dashboard:
   ```
   SENDGRID_API_KEY=your_sendgrid_key
   SENDGRID_FROM_EMAIL=your@email.com
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_token
   TWILIO_PHONE_NUMBER=your_twilio_number
   ```

4. **Get Railway Token (for GitHub Actions)**
   - Railway Dashboard → Account Settings → Tokens
   - Create new token
   - Copy the token

5. **Add to GitHub Secrets**
   - Go to: https://github.com/trentbecknell/audomte/settings/secrets/actions
   - Click "New repository secret"
   - Name: `RAILWAY_TOKEN`
   - Value: [paste your token]
   - Click "Add secret"

6. **Deploy!**
   - Push to main branch
   - GitHub Actions will automatically deploy
   - Your app will be live at: `https://your-app.railway.app`

---

### Option 2: Deploy to Render

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Name: `alioop`
   - Root Directory: `alioop-microservice-prototype`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Add Environment Variables**
   ```
   SENDGRID_API_KEY=your_sendgrid_key
   SENDGRID_FROM_EMAIL=your@email.com
   TWILIO_ACCOUNT_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_token
   TWILIO_PHONE_NUMBER=your_twilio_number
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Render will auto-deploy on every push to main

---

### Option 3: Deploy to Fly.io

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login**
   ```bash
   fly auth login
   ```

3. **Create App**
   ```bash
   cd alioop-microservice-prototype
   fly launch
   ```

4. **Set Secrets**
   ```bash
   fly secrets set SENDGRID_API_KEY=your_key
   fly secrets set SENDGRID_FROM_EMAIL=your@email.com
   fly secrets set TWILIO_ACCOUNT_SID=your_sid
   fly secrets set TWILIO_AUTH_TOKEN=your_token
   fly secrets set TWILIO_PHONE_NUMBER=your_number
   ```

5. **Deploy**
   ```bash
   fly deploy
   ```

---

## 🔒 Environment Variables Required

All platforms need these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `SENDGRID_API_KEY` | SendGrid API key for emails | `SG.xxx...` |
| `SENDGRID_FROM_EMAIL` | Verified sender email | `noreply@yourdomain.com` |
| `TWILIO_ACCOUNT_SID` | Twilio Account SID | `ACxxx...` |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token | `xxx...` |
| `TWILIO_PHONE_NUMBER` | Twilio phone number | `+1234567890` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8000` |
| `DATABASE_URL` | PostgreSQL URL (if not using SQLite) | `sqlite:///./alioop.db` |

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) automatically:

1. ✅ Triggers on push to `main` branch
2. ✅ Checks out the code
3. ✅ Installs Railway CLI
4. ✅ Deploys to production
5. ✅ Runs health checks

### Manual Deployment

You can also trigger deployment manually:
1. Go to: https://github.com/trentbecknell/audomte/actions
2. Select "Deploy to Railway"
3. Click "Run workflow"

---

## 📊 Post-Deployment

After deployment, your app will be accessible at:
- Railway: `https://your-app-name.railway.app`
- Render: `https://your-app-name.onrender.com`
- Fly.io: `https://your-app-name.fly.dev`

### Update URLs in Code

After getting your production URL, update these files:

1. **file_watcher.py** (line ~243)
   ```python
   download_url = f"https://your-app.railway.app/delivery/{token}"
   ```

2. **app/main.py** (wherever localhost URLs appear)
   Replace `http://localhost:8000` with your production URL

---

## 🐛 Troubleshooting

**Deployment fails?**
- Check GitHub Actions logs
- Verify RAILWAY_TOKEN is set in GitHub secrets
- Ensure environment variables are configured

**App not starting?**
- Check Railway/Render logs
- Verify all environment variables are set
- Check `requirements.txt` is complete

**Database issues?**
- SQLite works for testing but use PostgreSQL for production
- Railway offers free PostgreSQL - add it in dashboard
- Update DATABASE_URL environment variable

---

## 📚 Additional Resources

- [Railway Docs](https://docs.railway.app)
- [Render Docs](https://render.com/docs)
- [Fly.io Docs](https://fly.io/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

**Need help?** Open an issue at: https://github.com/trentbecknell/audomte/issues
