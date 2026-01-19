# GitHub Setup & Deployment Guide

## 1️⃣ Initialize Git Repository Locally

```bash
cd c:\Potpie ai\autocoder-agents

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AutoCoder Agents - AI-powered code generation"
```

## 2️⃣ Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `autocoder-agents`
3. Description: "AI-Powered Multi-Agent Code Generation Assistant"
4. Public (for assignment visibility)
5. **Don't** initialize with README (already have one)
6. Click "Create repository"

## 3️⃣ Connect Local Repo to GitHub

Copy the commands from GitHub and run:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/autocoder-agents.git
git push -u origin main
```

## 4️⃣ Deploy Backend to Render

1. Push code to GitHub (done above)
2. Go to https://render.com
3. Sign in with GitHub
4. Click **"New +"** → **"Web Service"**
5. Connect your GitHub account if needed
6. Select `autocoder-agents` repository
7. Fill in deployment details:
   - **Name**: `autocoder-agents-api` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Branch**: `main`

8. Set environment variables:
   ```
   OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
   PRIMARY_MODEL=mistralai/mistral-7b-instruct
   FALLBACK_MODEL=meta-llama/llama-2-7b-chat
   CORS_ORIGINS=["https://YOUR_VERCEL_URL.vercel.app"]
   ```

9. Click **"Create Web Service"**
10. Wait for deployment (~3-5 minutes)
11. **Copy your service URL** (e.g., `https://autocoder-agents-api.onrender.com`)

## 5️⃣ Deploy Frontend to Vercel

1. Go to https://vercel.com/new
2. Sign in with GitHub
3. Select `autocoder-agents` repository
4. Framework: **Next.js** (but it's React - Vercel handles it)
   - Or select **Other** for custom config
5. Root Directory: `frontend`
6. Build command: `npm run build`
7. Output directory: `build`
8. Set environment variables:
   ```
   REACT_APP_API_URL=https://autocoder-agents-api.onrender.com
   REACT_APP_ENV=production
   ```
9. Click **"Deploy"**
10. Wait for deployment (~2-3 minutes)
11. **Copy your Vercel URL** (e.g., `https://autocoder-agents.vercel.app`)

## 6️⃣ Update Backend CORS for Production

After getting Vercel URL:

```bash
# Local: Edit backend/.env
CORS_ORIGINS=["https://YOUR_VERCEL_URL.vercel.app"]

# Push changes
git add backend/.env
git commit -m "Update CORS for production Vercel URL"
git push
```

Render will auto-redeploy. Wait 2-3 minutes.

## 7️⃣ Test Live Deployment

1. Open your Vercel URL in browser
2. Enter a code query
3. Should connect to your live backend
4. Verify code generation works
5. Check browser console for errors

## 🆘 Troubleshooting Deployments

### Backend (Render) Issues

**"Build failed" error:**
- Check Procfile exists
- Check runtime.txt has `python-3.11.0`
- Ensure requirements.txt formatted correctly
- Run locally: `pip install -r requirements.txt`

**"Health check failed":**
- Verify backend can start: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Check logs in Render dashboard
- Ensure OPENROUTER_API_KEY is set

**"CORS errors" in frontend:**
- Update CORS_ORIGINS in Render environment
- Include full Vercel URL
- Redeploy backend

### Frontend (Vercel) Issues

**"Failed to fetch":**
- Check REACT_APP_API_URL matches backend URL
- Verify backend is running and accessible
- Check browser console for errors
- Redeploy frontend if env vars changed

**"Module not found":**
- Ensure package.json has all dependencies
- Run locally: `npm install`
- Check build output for errors

**Build timeout:**
- Dependencies taking too long to install
- Split node_modules if needed
- Use build cache

## 📊 Monitoring

### Render Backend Monitoring
1. Go to Render dashboard
2. Select your web service
3. Check:
   - Logs tab (real-time logs)
   - Events tab (deployment history)
   - Settings tab (update env vars)

### Vercel Frontend Monitoring
1. Go to Vercel dashboard
2. Select your project
3. Check:
   - Deployments tab (deployment history)
   - Logs tab (build and runtime logs)
   - Settings tab (env vars, domains)

## 🔄 Continuous Deployment

Both Render and Vercel auto-deploy on every push to `main` branch.

```bash
# Make changes locally
git add .
git commit -m "Your change description"
git push

# Render: Auto-deploys backend (watch logs)
# Vercel: Auto-deploys frontend (watch logs)
```

## ✅ Final Verification Checklist

- [ ] GitHub repo created and pushed
- [ ] Backend deployed on Render
- [ ] Frontend deployed on Vercel
- [ ] Backend health check working: `GET /health`
- [ ] Frontend loads without errors
- [ ] Can generate code from live frontend
- [ ] Copy-to-clipboard works
- [ ] Agent display shows correctly
- [ ] No console errors in browser
- [ ] Backend logs show successful requests

## 📝 Deployment Checklist

| Step | Render | Vercel |
|------|--------|--------|
| Connect GitHub | ✅ | ✅ |
| Set env variables | ✅ | ✅ |
| Configure build | ✅ | ✅ |
| Configure start | ✅ | - |
| First deploy | ✅ | ✅ |
| Test live | ✅ | ✅ |
| Monitor logs | ✅ | ✅ |

## 🚨 Emergency Recovery

**If backend goes down:**
```bash
# Re-trigger deployment
git commit --allow-empty -m "Trigger redeploy"
git push
```

**If frontend goes down:**
```bash
# Same as above
git commit --allow-empty -m "Trigger redeploy"
git push
```

**Check status:**
- Render: Dashboard → Logs
- Vercel: Dashboard → Deployments

---

**Your live application is now deployed! 🎉**
