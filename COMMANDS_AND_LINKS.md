# 🔗 CRITICAL LINKS & COMMANDS

Keep this handy! All URLs and commands you need in one place.

---

## 🌐 EXTERNAL SERVICES

### Must Use (Required)
| Service | URL | Purpose |
|---------|-----|---------|
| **OpenRouter** | https://openrouter.ai | Get free API key |
| **GitHub** | https://github.com | Version control |
| **Render** | https://render.com | Deploy backend |
| **Vercel** | https://vercel.com | Deploy frontend |
| **Loom** | https://loom.com | Record video |
| **Google Form** | https://forms.gle/sJCV51j9uSpXq4LR6 | **SUBMIT HERE** |

### Optional (Good to Have)
| Service | URL | Purpose |
|---------|-----|---------|
| Postman | https://postman.com | Test API |
| VS Code | https://code.visualstudio.com | Code editor |
| GitHub Desktop | https://desktop.github.com | Git GUI |

---

## 💻 LOCAL DEVELOPMENT

### Backend Startup
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Expected Output:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Verify:**
```bash
# In browser or curl:
curl http://localhost:8000/health
# Should return: {"status": "healthy"}
```

### Frontend Startup
```bash
cd frontend
npm install
npm start
```

**Expected Output:**
```
Compiled successfully!
You can now view autocoder-agents in the browser.
  Local: http://localhost:3000
```

**Verify:**
- Open http://localhost:3000 in browser
- Should see interface with query form

### Stop Services
```bash
# Backend: Press Ctrl+C in backend terminal
# Frontend: Press Ctrl+C in frontend terminal
```

---

## 🔐 API KEY SETUP

### 1. Get Free OpenRouter Key
1. Go: https://openrouter.ai
2. Sign up (or login)
3. Navigate to API keys
4. Copy your key

### 2. Add to Backend
```bash
# Edit backend/.env
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
```

### 3. Test Connection
```bash
# In backend terminal, should work without errors
# Try making a request in frontend
```

---

## 🐙 GIT COMMANDS

### Initial Setup
```bash
cd autocoder-agents
git init
git add .
git commit -m "Initial commit: AutoCoder Agents"
git remote add origin https://github.com/YOUR_USERNAME/autocoder-agents.git
git branch -M main
git push -u origin main
```

### After Changes
```bash
git add .
git commit -m "Your change description"
git push
```

### Check Status
```bash
git status          # See what changed
git log --oneline   # See commit history
git remote -v       # See remote URL
```

---

## 🚀 DEPLOYMENT COMMANDS

### For Render (Backend)

1. Login to https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub (if not already)
4. Select `autocoder-agents` repo
5. Fill details:
   ```
   Name: autocoder-agents-api
   Runtime: Python 3
   Build command: pip install -r requirements.txt
   Start command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Add environment variables:
   ```
   OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY
   PRIMARY_MODEL=mistralai/mistral-7b-instruct
   FALLBACK_MODEL=meta-llama/llama-2-7b-chat
   CORS_ORIGINS=["https://YOUR_VERCEL_URL.vercel.app"]
   ```
7. Click "Create Web Service"
8. Wait for deployment
9. **Copy the URL** (e.g., https://autocoder-agents-api.onrender.com)

### For Vercel (Frontend)

1. Login to https://vercel.com
2. Click "Add New..." → "Project"
3. Select GitHub and authorize
4. Find `autocoder-agents` repo
5. Import it
6. Set environment variables:
   ```
   REACT_APP_API_URL=https://YOUR_RENDER_URL.onrender.com
   REACT_APP_ENV=production
   ```
7. Click "Deploy"
8. Wait for deployment
9. **Copy the URL** (e.g., https://autocoder-agents.vercel.app)

### After Both Deploy
```bash
# Update frontend/.env.production with backend URL
# Redeploy frontend on Vercel if needed
```

---

## 🎬 LOOM VIDEO

### Recording Setup
1. Go to https://loom.com
2. Sign up or login
3. Click "Start recording"
4. Allow access to camera + screen
5. Start recording

### What to Show (60 seconds)
```
0-10s:   "This is AutoCoder Agents..."
10-20s:  Explain the problem being solved
20-30s:  Show live application interface
30-45s:  Enter query, click generate, watch processing
45-55s:  Show generated code with syntax highlighting
55-60s:  "Thank you, this has been AutoCoder Agents"
```

### After Recording
1. Click "Stop"
2. Wait for processing
3. Click "Share"
4. Copy the public link
5. Save for submission

---

## 📋 SUBMISSION FORM

**URL**: https://forms.gle/sJCV51j9uSpXq4LR6

### Fields to Fill
```
1. Your Full Name
   Example: John Smith

2. Email Address
   Example: john@example.com

3. Project Title
   Example: AutoCoder Agents - AI-Powered Code Generation

4. Problem Statement
   (Copy from your documentation)

5. GitHub Repository URL
   Example: https://github.com/jsmith/autocoder-agents
   (Must be PUBLIC)

6. Backend Live URL
   Example: https://autocoder-agents-api.onrender.com
   (Test this works before submitting!)

7. Frontend Live URL
   Example: https://autocoder-agents.vercel.app
   (Test this works before submitting!)

8. Loom Video Link
   Example: https://loom.com/share/12345...
   (Must be publicly shareable)

9. Resume PDF
   (Upload PDF file)

10. Project Description
    (300-500 words about your project)

11. Key Features
    (List of features you implemented)

12. Additional Links
    (Portfolio, LinkedIn, etc. - optional)
```

---

## ✅ VERIFICATION COMMANDS

### Test Backend Health
```bash
# Windows (in PowerShell)
Invoke-WebRequest http://localhost:8000/health

# Mac/Linux (in terminal)
curl http://localhost:8000/health
```

**Expected response:**
```json
{"status": "healthy", "timestamp": "2024-01-20T15:30:00Z"}
```

### Test API Endpoints
```bash
# List agents
curl http://localhost:8000/agents

# Test code generation
curl -X POST http://localhost:8000/api/process-query \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello world", "language": "python"}'
```

### Test Frontend Connection
1. Open http://localhost:3000
2. Open browser DevTools (F12)
3. Go to Network tab
4. Generate code
5. Should see successful POST to /api/process-query

---

## 🆘 EMERGENCY FIXES

### Backend Won't Start
```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check for syntax errors
python -m py_compile main.py

# Try different port
uvicorn main:app --port 8001
```

### Frontend Won't Start
```bash
# Clear cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Kill port 3000
# Windows: netstat -ano | findstr :3000
# Mac/Linux: lsof -i :3000
```

### API Key Error
```bash
# Get new key from https://openrouter.ai
# Edit backend/.env
OPENROUTER_API_KEY=sk-or-v1-NEW_KEY_HERE
# Restart backend
```

### CORS Error
```bash
# Edit backend/.env
# Add your frontend URL to CORS_ORIGINS
CORS_ORIGINS=["http://localhost:3000", "https://your-vercel-url.vercel.app"]
# Restart backend
```

### Deploy Failure
```bash
# Manually trigger redeploy
git commit --allow-empty -m "Trigger redeploy"
git push
# Wait 5 minutes for redeployment
```

---

## 📊 STATUS CHECKING

### Backend Status
- Health: http://localhost:8000/health
- Docs: http://localhost:8000/docs (Swagger)
- Logs: Check terminal where uvicorn is running

### Frontend Status
- App: http://localhost:3000
- Console: F12 → Console tab (check for errors)
- Network: F12 → Network tab (see API calls)

### Deployment Status
- Render: https://render.com/dashboard (select your service)
- Vercel: https://vercel.com/dashboard (select your project)
- GitHub: https://github.com/YOUR_USERNAME/autocoder-agents (commits, workflows)

---

## ⏰ TIME-SAVING SHORTCUTS

### One-Command Setup (Unix)
```bash
./setup.sh
```

### One-Command Setup (Windows)
```bash
setup.bat
```

### View All Your Files at Once
```bash
# Windows
dir /s /b

# Mac/Linux
find . -type f -name "*.ts" -o -name "*.tsx" -o -name "*.py"
```

### Quick Test Everything
```bash
# Test backend health
curl http://localhost:8000/health && echo "✅ Backend OK"

# Test frontend loads
curl http://localhost:3000 | head -20
```

---

## 📚 DOCUMENTATION QUICK LINKS

| Need | File |
|------|------|
| Start here | [START_HERE.md](START_HERE.md) |
| Quick setup | [SETUP.md](SETUP.md) |
| Deploy guide | [DEPLOYMENT.md](DEPLOYMENT.md) |
| Submit guide | [SUBMISSION.md](SUBMISSION.md) |
| Quick answers | [QUICKREF.md](QUICKREF.md) |
| Progress tracking | [CHECKLIST.md](CHECKLIST.md) |
| Code structure | [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) |

---

## 🎯 CRITICAL DEADLINES

```
2024-01-20 (TODAY)
├─ 2:00 PM - Submit completely done (leave 2 hours buffer)
├─ 3:30 PM - Last minute checks (30 min before deadline)
└─ 4:00 PM - DEADLINE (No submissions after this!)
```

---

## 💾 BACKUP EVERYTHING

Before submitting:
```bash
# Backup your code
cp -r . ../autocoder-agents-backup

# Save your URLs
# Backend: ___________________________
# Frontend: ___________________________
# Video: ___________________________

# Save your form response
# Screenshot confirmation message
```

---

## ✨ FINAL REMINDERS

✅ **Do these before submitting:**
- [ ] Test both URLs in incognito window (fresh session)
- [ ] Try code generation on deployed app
- [ ] Check browser console for errors
- [ ] Verify video is watchable
- [ ] Verify resume PDF opens
- [ ] Read form one more time before submitting

❌ **Never:**
- Don't hardcode API keys
- Don't submit without testing
- Don't miss the deadline
- Don't submit private repo
- Don't skip local testing

✅ **Always:**
- Use .env files for secrets
- Test before deploying
- Test after deploying
- Keep 30-min buffer before deadline
- Screenshot your confirmation

---

**You have all the links and commands you need.**  
**Execute them in order.**  
**You'll be done in 2 hours.**  
**Submit with confidence!** 🚀

---

*Last Updated: January 20, 2024*  
*All links verified and working*  
*Ready to go!*
