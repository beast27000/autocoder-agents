# ⚡ Quick Reference Card

## 🚀 1-Minute Startup

### Start Backend (Terminal 1)
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
uvicorn main:app --reload
# ✅ http://localhost:8000
```

### Start Frontend (Terminal 2)
```bash
cd frontend
npm start
# ✅ http://localhost:3000
```

### Test It
1. Open http://localhost:3000
2. Enter: "React button"
3. Select: TypeScript
4. Click: Generate

---

## 🔑 API Keys

### Get Free OpenRouter Key
1. Go: https://openrouter.ai
2. Sign up
3. Copy key
4. Add to `backend/.env`
```
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
```

---

## 📝 Key Files & Locations

| File | Purpose | Edit? |
|------|---------|-------|
| `backend/main.py` | API endpoints | ✏️ Custom prompts |
| `backend/.env` | Config & API key | ✏️ Add your key |
| `frontend/src/App.tsx` | Main component | ❌ Usually not |
| `frontend/.env` | Dev API URL | ❌ Keep localhost |
| `frontend/.env.production` | Prod API URL | ✏️ After deployment |

---

## 🌐 Deployment URLs

### Render (Backend)
1. https://render.com
2. Create Web Service
3. Connect GitHub repo
4. Deploy
5. Copy URL → `REACT_APP_API_URL`

### Vercel (Frontend)
1. https://vercel.com
2. Import project
3. Set `REACT_APP_API_URL` env var
4. Deploy

---

## 🎯 5-Hour Timeline to Submission

| Time | Task | Duration |
|------|------|----------|
| 0:00 | Start | - |
| 0:00-0:30 | Local testing & fixes | 30 min |
| 0:30-0:45 | GitHub setup & push | 15 min |
| 0:45-1:00 | Deploy backend (Render) | 15 min |
| 1:00-1:15 | Deploy frontend (Vercel) | 15 min |
| 1:15-1:35 | Test live deployment | 20 min |
| 1:35-1:50 | Record Loom video | 15 min |
| 1:50-2:00 | Prepare resume | 10 min |
| 2:00-2:15 | Final checks | 15 min |
| 2:15 | Submit form | 5 min |
| **Total** | **Complete** | **~2 hours** |

---

## 🆘 Emergency Fixes (Do These First)

### "API Key Error"
```bash
# backend/.env
OPENROUTER_API_KEY=sk-or-v1-YOUR_ACTUAL_KEY
```
Restart backend.

### "Connection Refused"
```bash
# Check ports
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000

# Restart both:
# Terminal 1: cd backend && uvicorn main:app --reload
# Terminal 2: cd frontend && npm start
```

### "Module Not Found"
```bash
# Backend
cd backend && pip install -r requirements.txt

# Frontend
cd frontend && npm install
```

### "Build Errors"
```bash
# Frontend
cd frontend
npm run build  # See error details
npm start      # Restart
```

---

## ✅ Pre-Deployment Checklist (5 min)

- [ ] Backend runs locally: `GET http://localhost:8000/health`
- [ ] Frontend loads: `http://localhost:3000`
- [ ] Code generation works end-to-end
- [ ] No console errors in browser
- [ ] All files committed to GitHub
- [ ] GitHub repo is PUBLIC

---

## 🎬 Loom Video Checklist (60 sec)

- [ ] Face visible in webcam (top right)
- [ ] Clear audio (no background noise)
- [ ] Screen readable (zoom in if needed)
- [ ] Under 60 seconds
- [ ] Shows: problem → solution → demo → result
- [ ] Link is shareable (public)

---

## 📋 Submission Form Fields

```
1. Name: Your Full Name
2. Email: your@email.com
3. Title: AutoCoder Agents - AI-Powered Code Generation
4. GitHub: https://github.com/YOU/autocoder-agents
5. Backend URL: https://autocoder-api.onrender.com
6. Frontend URL: https://autocoder-agents.vercel.app
7. Loom: https://loom.com/share/XXXXX
8. Resume: PDF upload
9. Description: ~300 words about your project
10. Features: Multi-agent, Real-time, Multi-language, etc.
```

---

## 💾 Git Quick Commands

```bash
# Initial setup
git init
git add .
git commit -m "Initial commit: AutoCoder Agents"
git remote add origin https://github.com/YOU/autocoder-agents.git
git branch -M main
git push -u origin main

# After changes
git add .
git commit -m "Your message"
git push

# Check status
git status
git log --oneline
```

---

## 🔗 Important Links

| Link | Purpose |
|------|---------|
| https://forms.gle/sJCV51j9uSpXq4LR6 | **SUBMISSION FORM** ⭐ |
| https://openrouter.ai | Free API keys |
| https://render.com | Backend deployment |
| https://vercel.com | Frontend deployment |
| https://github.com | Code repository |
| https://loom.com | Video recording |
| http://localhost:8000 | Local backend |
| http://localhost:3000 | Local frontend |

---

## 📊 Agent Processing Flow

```
User Query
    ↓
Orchestrator (analyzes)
    ↓
Frontend Dev (creates UI)
    ↓
Backend Dev (creates logic)
    ↓
Testing (validates)
    ↓
Documentation (explains)
    ↓
Generated Code + Explanation
```

---

## 🎯 Success Indicators

✅ Backend starts without errors  
✅ Frontend loads in browser  
✅ API responds to requests  
✅ Code generates from user queries  
✅ UI displays results correctly  
✅ Both services deploy successfully  
✅ Live URLs are accessible  
✅ Loom video is recorded  
✅ Submission form filled  
✅ Before 4:00 PM deadline  

---

## ⏰ Time Management

**Ideal Pace**:
- 30 min → Local testing working
- 60 min → GitHub + Backend deployed
- 90 min → Frontend deployed + verified
- 110 min → Video recorded
- 125 min → Form submitted
- **Time Remaining**: Safe buffer!

**Never**:
- ❌ Start testing 5 minutes before deadline
- ❌ Deploy 30 minutes before deadline
- ❌ Record video last-minute
- ❌ Fill form without verification

---

## 🚨 Critical Path

1. **Local testing** (can't skip)
2. **GitHub push** (required for deployment)
3. **Backend deploy** (frontend needs this URL)
4. **Frontend deploy** (depends on backend)
5. **Video record** (can do in parallel)
6. **Form submit** (deadline!)

**If running late**: Can record video while services deploy.

---

## 💡 Pro Tips

✨ Test locally first - saves 30 minutes of deployment issues  
✨ Deploy early - gives time for issues  
✨ Record video first - it's quick  
✨ Use incognito window - tests production properly  
✨ Check logs - tells you what went wrong  
✨ Read error messages - they're helpful  
✨ Keep .env keys secret - never commit them  
✨ Submit 30 minutes early - no last-minute stress  

---

**You've got this! 💪 Keep moving forward!**

Deadline: **4:00 PM Jan 20** | Status: **✅ Ready** | Confidence: **🚀 High**
