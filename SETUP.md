# Quick Setup Guide - AutoCoder Agents

Complete setup in under 10 minutes.

## ⏱️ 5-Minute Local Setup

### 1. Backend (2 minutes)
```bash
cd backend

# Windows:
python -m venv venv
venv\Scripts\activate

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup .env file
# Edit .env and add your OpenRouter API key (get free at https://openrouter.ai)
# OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE

# Start backend
uvicorn main:app --reload
# Server running at: http://localhost:8000
```

### 2. Frontend (2 minutes)
```bash
cd frontend

# Install dependencies
npm install

# Start frontend
npm start
# App opens at: http://localhost:3000
```

### 3. Test It (1 minute)
1. Go to http://localhost:3000
2. Enter: "Create a React button component"
3. Select: TypeScript
4. Click: "Generate Code"
5. Watch agents process in real-time
6. See generated code with syntax highlighting

## 🚀 Deploy to Production (15 minutes)

### Backend to Render

1. Push your code to GitHub
2. Go to https://render.com/dashboard
3. Create new **Web Service**
4. Connect your GitHub repo
5. Fill in:
   - **Name**: `autocoder-api`
   - **Runtime**: `Python 3`
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variable:
   - **OPENROUTER_API_KEY**: Your key
   - Other vars in .env
7. Click Deploy
8. Copy your backend URL (e.g., `https://autocoder-api.onrender.com`)

### Frontend to Vercel

1. Go to https://vercel.com
2. Click "Add New..." → "Project"
3. Import your GitHub repo
4. Add environment variable:
   - **REACT_APP_API_URL**: `https://autocoder-api.onrender.com`
5. Click Deploy
6. You're live! 🎉

## 📋 Configuration Checklist

- [ ] Created backend/.env with OpenRouter API key
- [ ] Created frontend/.env (for localhost)
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Successfully generated code from frontend
- [ ] Code output displays correctly
- [ ] Backend deployed to Render
- [ ] Frontend deployed to Vercel
- [ ] Updated frontend/.env.production with backend URL

## 🆘 Common Issues

**"Connection refused" - Backend not running**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn main:app --reload
```

**"API key error" - Invalid OpenRouter key**
```bash
# Get free key at https://openrouter.ai
# Add to backend/.env:
OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
# Restart backend
```

**"Port 3000 already in use" - Frontend port taken**
```bash
cd frontend
npm start  # Will auto-use 3001
```

**"Module not found" - Dependencies not installed**
```bash
# Backend
cd backend && pip install -r requirements.txt

# Frontend
cd frontend && npm install
```

## 📝 Project Structure

```
autocoder-agents/
├── backend/
│   ├── main.py (FastAPI app with endpoints)
│   ├── config.py (Configuration)
│   ├── agents.py (Agent definitions)
│   ├── requirements.txt (Dependencies)
│   ├── .env (Your API key here)
│   ├── Procfile (Render config)
│   └── runtime.txt (Python version)
├── frontend/
│   ├── src/App.tsx (Main component)
│   ├── src/components/ (UI components)
│   ├── package.json (Dependencies)
│   ├── .env (Dev - localhost:8000)
│   ├── .env.production (Prod - your Render URL)
│   └── public/index.html (Entry point)
├── README.md (Full documentation)
└── vercel.json (Vercel config)
```

## 🔑 Important URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Local Backend | http://localhost:8000 | Development API |
| Local Frontend | http://localhost:3000 | Development UI |
| OpenRouter API | https://openrouter.ai | Get free API key |
| Render | https://render.com | Deploy backend |
| Vercel | https://vercel.com | Deploy frontend |
| GitHub | https://github.com | Version control |

## ✅ Success Indicators

- Backend server started: `INFO: Started server process`
- Frontend running: `Compiled successfully!`
- API responds: `GET http://localhost:8000/health` returns `{ "status": "healthy" }`
- Form loads: Can see query input, language selector, generate button
- Code generates: Can submit query and see code output

## 🎯 Next Steps After Setup

1. Test with different code queries
2. Try different programming languages
3. Observe agent processing in real-time
4. Review generated code quality
5. Customize agent prompts in backend/main.py
6. Add more code templates
7. Deploy to production
8. Record Loom demo
9. Submit assignment

---

**Need help?** Check README.md for detailed documentation.
