"""
InterGuide Installer
Creates a desktop shortcut and sets up the application
"""

import os
import sys
import shutil
from pathlib import Path

def create_launcher_script():
    """Create a launcher script for the application"""
    launcher_content = """@echo off
REM InterGuide Launcher
cd /d "%~dp0"
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application encountered an error.
    pause
)
"""
    
    with open("InterGuide.bat", "w") as f:
        f.write(launcher_content)
    
    print("✓ Created launcher script")

def create_desktop_shortcut():
    """Create a desktop shortcut"""
    desktop = Path.home() / "Desktop"
    current_dir = Path.cwd()
    
    # PowerShell script to create shortcut
    ps_script = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{desktop}\\InterGuide.lnk")
$Shortcut.TargetPath = "{current_dir}\\InterGuide.bat"
$Shortcut.WorkingDirectory = "{current_dir}"
$Shortcut.Description = "InterGuide - AI Interview Assistant"
$Shortcut.Save()
"""
    
    # Save and execute PowerShell script
    ps_file = current_dir / "create_shortcut.ps1"
    with open(ps_file, "w") as f:
        f.write(ps_script)
    
    os.system(f'powershell -ExecutionPolicy Bypass -File "{ps_file}"')
    ps_file.unlink()  # Delete temporary file
    
    print(f"✓ Created desktop shortcut at: {desktop}\\InterGuide.lnk")

def create_icon():
    """Create a simple icon file"""
    # Create a simple .ico file using Python (basic icon)
    icon_content = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAMzSURB
VFiFvZdPaBxVHMe/783s7mY3yWaTNmnTpE1qY6O2YKFQqQcPHrx48SB48eRBEEHwIHgQBEEQPHjw
YD0IHjx5EAQRPHjwUGgP/sFDpdLapKlNs0n+7exmZ3dn3vPQJLubZDeb1A988Jh5v9/v+32/897M
ew8QL774IgDg/fff/0+NqA4ODg4ODg7/L1599dUAgA8++OAfo7GDg4ODg4ODw/8LIQQAQAhR00aj
EYLBoMHBwcHBYb1RFVVVVRVCCAGHQ7/fr6qqSpIkSZKk0Wik0+m02+3W6/VaLBaLxWKx2Ww2m802
Go1ms9loNBqNRqPRaDQajUaj0Wg0Go1Go9FoNBqNRqPRaDQajUajUavVqtVq1Wq1arVatVqtWq1W
rVarVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVar1Wq1Wq1Wq9VqtVqtVqvVarVarVZrLBaL
xWKxWCwWi8VisVgsFovFYrFYLBaLxWKxWCwWi8ViMU3TdF3XdV3XdV3XdV3XdV3XdV3XdV3XdV3X
dV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3XdV3X
dV3XdV3XdV3XdV3XdV3XdV3XdV0Ph8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6H
w+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD
4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8Ph8PHxCYVCoVAoFAqFQqFQKBQKhUKh
UCgUCoVCoVAoFAqFQqFQKBQKhUKhUCgUCoVCoVAoFAqFQqFQKBQKhUKhUCgUCoVCoVAoFAqFQqFQ
KBQKhUKhUCgUCoVCoVAoFAqFQqFQKBQKhUKhUCgUCoVCoVAoFAqFQqFQKBQKBQAIIYQQQgghhBBC
CCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQggh
hBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBC/AU8/fTTAIBP
P/30X6Wxg4ODg4ODg8P/C0899RQA4LPPPvvbaOwwgL8BxNX8fvHgGisAAAAASUVORK5CYII=
"""
    
    print("✓ Icon placeholder created")

def check_dependencies():
    """Check if all dependencies are installed"""
    print("\nChecking dependencies...")
    
    required = [
        'openai', 'sounddevice', 'speech_recognition', 
        'keyboard', 'mss', 'PIL', 'dotenv'
    ]
    
    missing = []
    for module in required:
        try:
            if module == 'PIL':
                __import__('PIL')
            elif module == 'dotenv':
                __import__('dotenv')
            else:
                __import__(module)
            print(f"  ✓ {module}")
        except ImportError:
            print(f"  ✗ {module} - MISSING")
            missing.append(module)
    
    if missing:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True

def check_api_key():
    """Check if API key is configured"""
    if not os.path.exists(".env"):
        print("\n⚠️  .env file not found!")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        if "your_openai_api_key_here" in content or not "OPENAI_API_KEY=sk-" in content:
            print("\n⚠️  OpenAI API key not configured in .env file")
            return False
    
    print("✓ API key configured")
    return True

def main():
    """Main installer function"""
    print("="*60)
    print("  InterGuide - Installation")
    print("="*60)
    print()
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found!")
        print("Please run this script from the InterGuide directory")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Please install dependencies first:")
        print("   pip install -r requirements.txt")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Check API key
    if not check_api_key():
        print("\n❌ Please configure your API key in .env file")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("  Installing InterGuide...")
    print("="*60)
    print()
    
    # Create launcher
    create_launcher_script()
    
    # Create desktop shortcut
    try:
        create_desktop_shortcut()
    except Exception as e:
        print(f"⚠️  Could not create desktop shortcut: {e}")
        print("   You can manually create a shortcut to InterGuide.bat")
    
    print("\n" + "="*60)
    print("  ✓ Installation Complete!")
    print("="*60)
    print()
    print("InterGuide has been installed!")
    print()
    print("📍 Desktop shortcut created: InterGuide")
    print("   Double-click the icon to launch the app")
    print()
    print("⚡ Features:")
    print("   • Click 'Start Listening' button to begin")
    print("   • Click 'Screen: OFF' to enable screen reading")
    print("   • Use Ctrl+Shift+L/C/S/H hotkeys (requires admin)")
    print()
    print("💡 Tip: Run as Administrator for hotkey support")
    print()
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
