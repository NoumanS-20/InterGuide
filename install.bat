@echo off
REM InterGuide Quick Installer
echo ========================================
echo   InterGuide - Quick Install
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "main.py" (
    echo ERROR: main.py not found!
    echo Please run this from the InterGuide directory.
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Checking dependencies...
pip show openai >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Run the Python installer
echo.
echo Running installer...
python setup.py

pause
