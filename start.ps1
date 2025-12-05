# Quick Start Script for InterGuide
# This script helps you set up and run the application

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  InterGuide - Interview Assistant" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if .env exists and has API key
if (Test-Path ".env") {
    $envContent = Get-Content ".env" -Raw
    if ($envContent -match "OPENAI_API_KEY=your_openai_api_key_here" -or $envContent -match "OPENAI_API_KEY=\s*$") {
        Write-Host "⚠️  WARNING: OpenAI API key not configured!" -ForegroundColor Yellow
        Write-Host "`nPlease edit .env file and add your OpenAI API key:" -ForegroundColor Yellow
        Write-Host "   OPENAI_API_KEY=sk-your-actual-api-key`n" -ForegroundColor White
        
        $response = Read-Host "Do you want to open .env file now? (y/n)"
        if ($response -eq "y" -or $response -eq "Y") {
            notepad .env
            Write-Host "`nAfter adding your API key, save the file and run this script again." -ForegroundColor Green
            exit
        }
    } else {
        Write-Host "✅ Configuration file found" -ForegroundColor Green
    }
} else {
    Write-Host "❌ .env file not found! Creating from template..." -ForegroundColor Red
    Copy-Item ".env.example" ".env"
    Write-Host "✅ Created .env file. Please edit it and add your OpenAI API key." -ForegroundColor Yellow
    notepad .env
    exit
}

# Check Python version
Write-Host "`nChecking Python version..." -ForegroundColor Cyan
$pythonVersion = python --version 2>&1
Write-Host "  $pythonVersion" -ForegroundColor White

# Test imports
Write-Host "`nTesting dependencies..." -ForegroundColor Cyan
$null = python -c "import sounddevice, speech_recognition, openai, keyboard, pynput; print('OK')" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ All dependencies installed" -ForegroundColor Green
} else {
    Write-Host "  ❌ Missing dependencies!" -ForegroundColor Red
    Write-Host "  Run: pip install -r requirements.txt`n" -ForegroundColor Yellow
    exit
}

# Show instructions
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Ready to Start!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Keyboard Shortcuts:" -ForegroundColor Yellow
Write-Host "  Ctrl+Shift+L  - Start/Stop listening" -ForegroundColor White
Write-Host "  Ctrl+Shift+C  - Clear display" -ForegroundColor White
Write-Host "  Ctrl+Shift+H  - Hide/Show window`n" -ForegroundColor White

Write-Host "Starting InterGuide...`n" -ForegroundColor Green

# Run the application
python main.py
