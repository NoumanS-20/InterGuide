@echo off
echo ========================================
echo   InterGuide - Interview Assistant
echo ========================================
echo.
echo Starting application...
echo.
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ========================================
    echo   Application Error
    echo ========================================
    echo.
    echo The application crashed. This may be due to:
    echo   1. NumPy compatibility issues with Python 3.14
    echo   2. Missing administrator privileges for hotkeys
    echo.
    echo Solutions:
    echo   - Try running as Administrator right-click ^> Run as administrator^)
    echo   - Or use the GUI buttons instead of hotkeys
    echo.
    pause
)
