@echo off
REM AutoCoder Agents - Quick Setup Script for Windows
REM Run this to set up everything locally in one go

echo.
echo ======================================
echo 🚀 AutoCoder Agents - Quick Setup
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.11+
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js not found. Please install Node.js 16+
    pause
    exit /b 1
)

echo ✅ Python found
echo ✅ Node.js found
echo.

REM Backend setup
echo 📦 Setting up Backend...
cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt

cd ..

echo ✅ Backend setup complete!
echo.
echo ⚠️  IMPORTANT: Add your OpenRouter API key to backend\.env
echo    1. Get free key at https://openrouter.ai
echo    2. Edit backend\.env
echo    3. Set: OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE
echo.

REM Frontend setup
echo 📦 Setting up Frontend...
cd frontend

echo Installing Node dependencies...
call npm install

cd ..

echo ✅ Frontend setup complete!
echo.

REM Final instructions
echo ======================================
echo ✅ Setup Complete!
echo ======================================
echo.
echo 📝 Next steps:
echo 1. Add your OpenRouter API key to backend\.env
echo.
echo 2. Open Command Prompt and run:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn main:app --reload
echo.
echo 3. Open another Command Prompt and run:
echo    cd frontend
echo    npm start
echo.
echo 4. Open http://localhost:3000 in your browser
echo.
echo 📖 For detailed instructions, see SETUP.md
echo.

pause
