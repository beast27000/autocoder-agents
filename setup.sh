#!/bin/bash
# AutoCoder Agents - Quick Setup Script
# Run this to set up everything locally in one go

echo "🚀 AutoCoder Agents - Quick Setup"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.11+"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 16+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo "✅ Node.js found: $(node --version)"
echo ""

# Backend setup
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Return to root
cd ..

echo "✅ Backend setup complete!"
echo ""
echo "⚠️  IMPORTANT: Add your OpenRouter API key to backend/.env"
echo "   1. Get free key at https://openrouter.ai"
echo "   2. Edit backend/.env"
echo "   3. Set: OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE"
echo ""

# Frontend setup
echo "📦 Setting up Frontend..."
cd frontend

echo "Installing Node dependencies..."
npm install

cd ..

echo "✅ Frontend setup complete!"
echo ""

# Final instructions
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "📝 Next steps:"
echo "1. Add your OpenRouter API key to backend/.env"
echo "2. In Terminal 1, run:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   uvicorn main:app --reload"
echo ""
echo "3. In Terminal 2, run:"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "4. Open http://localhost:3000 in your browser"
echo ""
echo "📖 For detailed instructions, see SETUP.md"
echo ""
