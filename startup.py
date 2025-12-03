"""
InterGuide Startup - Handles initialization and error checking
"""

import sys
import os

def check_environment():
    """Check if the environment is properly set up"""
    print("Checking InterGuide environment...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print(f"❌ Python 3.8+ required. You have {sys.version}")
        return False
    
    if sys.version_info >= (3, 14):
        print(f"⚠️  WARNING: Python {sys.version_info.major}.{sys.version_info.minor} detected")
        print("   NumPy has compatibility issues with Python 3.14")
        print("   The app may crash unexpectedly")
        print()
    
    # Check critical imports
    print("Testing imports...")
    try:
        import warnings
        warnings.filterwarnings('ignore')
        
        # Test each critical module
        modules_to_test = [
            ('tkinter', 'Tkinter (GUI)'),
            ('dotenv', 'python-dotenv'),
            ('openai', 'OpenAI API'),
            ('sounddevice', 'sounddevice'),
            ('speech_recognition', 'SpeechRecognition'),
            ('keyboard', 'keyboard'),
            ('mss', 'mss (screen capture)'),
            ('PIL', 'Pillow'),
        ]
        
        for module_name, display_name in modules_to_test:
            try:
                __import__(module_name)
                print(f"  ✓ {display_name}")
            except ImportError as e:
                print(f"  ✗ {display_name} - MISSING")
                print(f"     Error: {e}")
                return False
        
        # Test numpy last (it may crash)
        try:
            import numpy
            print(f"  ✓ numpy")
        except Exception as e:
            print(f"  ✗ numpy - FAILED")
            print(f"     Error: {e}")
            print()
            print("NumPy is required but failed to load.")
            print("This is a known issue with Python 3.14.")
            print()
            print("SOLUTION: Downgrade to Python 3.11 or 3.12")
            print("  1. Uninstall Python 3.14")
            print("  2. Install Python 3.12 from python.org")
            print("  3. Reinstall dependencies: pip install -r requirements.txt")
            return False
            
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False
    
    print("\n✓ All dependencies loaded successfully")
    return True

def main():
    """Main startup function"""
    print("="*60)
    print("  InterGuide - Interview Assistant")
    print("="*60)
    print()
    
    # Check environment first
    if not check_environment():
        print("\n" + "="*60)
        print("  Environment Check Failed")
        print("="*60)
        print("\nPlease fix the issues above and try again.")
        print("\nPress Enter to exit...")
        input()
        sys.exit(1)
    
    # Import and run main app
    print("\nStarting InterGuide...")
    print()
    
    try:
        from main import InterviewAssistant
        app = InterviewAssistant()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
    except Exception as e:
        print(f"\n❌ Application Error: {e}")
        import traceback
        traceback.print_exc()
        print("\n" + "="*60)
        print("  Troubleshooting")
        print("="*60)
        print("1. Check .env file has your OpenAI API key")
        print("2. Try running as Administrator")
        print("3. Consider downgrading to Python 3.12")
        print("\nPress Enter to exit...")
        input()
        sys.exit(1)

if __name__ == "__main__":
    main()
