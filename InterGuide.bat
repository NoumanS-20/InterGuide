@echo off
REM InterGuide Launcher
cd /d "%~dp0"
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application encountered an error.
    pause
)
