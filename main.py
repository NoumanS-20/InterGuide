import threading
import time
from audio_capture import AudioCapture
# Use Google Speech Recognition (compatible with Python 3.14)
from speech_recognition_alt import SpeechRecognizer
from answer_generator import AnswerGenerator
from overlay_gui import OverlayWindow
from screen_capture import ScreenCapture
from config import Config
import keyboard

class InterviewAssistant:
    """Main application class that coordinates all components"""
    
    def __init__(self):
        self.audio_capture = AudioCapture()
        self.speech_recognizer = SpeechRecognizer()
        self.answer_generator = AnswerGenerator()
        self.screen_capture = ScreenCapture()
        self.gui = None
        
        self.is_listening = False
        self.screen_reading_enabled = False
        self.is_running = False
        self.listen_thread = None
        
    def initialize(self):
        """Initialize all components"""
        print("Initializing Interview Assistant...")
        
        # Validate configuration
        try:
            Config.validate()
        except ValueError as e:
            print(f"Configuration error: {e}")
            return False
        
        # Initialize answer generator
        try:
            self.answer_generator.initialize()
        except Exception as e:
            print(f"Failed to initialize answer generator: {e}")
            return False
        
        # Load speech recognition model
        try:
            self.speech_recognizer.load_model()
        except Exception as e:
            print(f"Failed to load speech recognition model: {e}")
            return False
        
        print("Initialization complete!")
        return True
    
    def setup_hotkeys(self):
        """Setup keyboard shortcuts"""
        try:
            keyboard.add_hotkey(Config.HOTKEY_START_STOP, self.toggle_listening)
            keyboard.add_hotkey(Config.HOTKEY_CLEAR, self.clear_display)
            keyboard.add_hotkey(Config.HOTKEY_TOGGLE_WINDOW, self.toggle_window)
            keyboard.add_hotkey(Config.HOTKEY_SCREEN_READING, self.toggle_screen_reading)
            print(f"\n✅ Hotkeys configured:")
            print(f"  {Config.HOTKEY_START_STOP} - Start/Stop listening")
            print(f"  {Config.HOTKEY_CLEAR} - Clear display")
            print(f"  {Config.HOTKEY_TOGGLE_WINDOW} - Hide/Show window")
            print(f"  {Config.HOTKEY_SCREEN_READING} - Toggle screen reading")
        except Exception as e:
            print(f"\n⚠️  WARNING: Hotkeys could not be registered")
            print(f"   Error: {e}")
            print(f"   On Windows, keyboard hotkeys require administrator privileges.")
            print(f"   Please use the buttons in the window instead, or run as administrator.")
    
    def toggle_screen_reading(self):
        """Toggle screen reading on/off"""
        self.screen_reading_enabled = not self.screen_reading_enabled
        if self.gui:
            self.gui.set_screen_reading(self.screen_reading_enabled)
        status = "enabled" if self.screen_reading_enabled else "disabled"
        print(f"\n📸 Screen reading {status}")
    
    def toggle_listening(self):
        """Toggle listening state"""
        if self.is_listening:
            self.stop_listening()
        else:
            self.start_listening()
    
    def start_listening(self):
        """Start listening for questions"""
        if self.is_listening:
            return
        
        self.is_listening = True
        print("\n[LISTENING] Started listening for questions...")
        
        if self.gui:
            self.gui.set_recording_status(True)
            self.gui.update_status("Listening for questions...")
        
        # Start listening in a separate thread
        self.listen_thread = threading.Thread(target=self._listen_loop, daemon=True)
        self.listen_thread.start()
    
    def stop_listening(self):
        """Stop listening"""
        if not self.is_listening:
            return
        
        self.is_listening = False
        print("\n[STOPPED] Stopped listening")
        
        if self.gui:
            self.gui.set_recording_status(False)
            self.gui.update_status("Stopped (Ctrl+Shift+L to start)")
    
    def _listen_loop(self):
        """Main listening loop that runs in a separate thread"""
        while self.is_listening:
            try:
                # Record audio for a duration
                print("Recording audio...")
                self.audio_capture.start_recording()
                
                # Record for 5 seconds at a time
                time.sleep(5)
                
                audio_data = self.audio_capture.stop_recording()
                
                if audio_data is not None and len(audio_data) > 0:
                    # Check if audio is not silent
                    if not self.audio_capture.is_silent(audio_data):
                        print("Processing audio...")
                        
                        if self.gui:
                            self.gui.update_status("Processing audio...")
                        
                        # Transcribe audio to text
                        question = self.speech_recognizer.transcribe_audio(audio_data)
                        
                        if question and len(question) > 10:  # Only process substantial questions
                            print(f"\n[QUESTION DETECTED]: {question}")
                            
                            if self.gui:
                                self.gui.display_question(question)
                                self.gui.update_status("Generating answer...")
                            
                            # Capture screen if enabled
                            screenshot = None
                            if self.screen_reading_enabled:
                                screenshot = self.screen_capture.capture_screen()
                                if screenshot:
                                    print("📸 Screen captured for analysis")
                                else:
                                    print("⚠️  Screen capture failed or returned None")
                            else:
                                print("[DEBUG] Screen reading is OFF, not capturing screen.")
                            # Generate answer with optional screenshot
                            print(f"[DEBUG] Calling generate_answer with screenshot={'Yes' if screenshot else 'No'}")
                            answer = self.answer_generator.generate_answer(question, screenshot=screenshot)
                            print(f"[DEBUG] Answer received: {answer[:80]}...")
                            print(f"\n[ANSWER GENERATED]:\n{answer}\n")
                            if self.gui:
                                self.gui.display_answer(answer)
                                self.gui.update_status("Answer ready - Listening...")
                        else:
                            if self.gui:
                                self.gui.update_status("Listening for questions...")
                    else:
                        print("Silent audio detected, continuing...")
                
                # Small delay before next recording
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error in listen loop: {e}")
                if self.gui:
                    self.gui.update_status(f"Error: {str(e)}")
                time.sleep(1)
    
    def clear_display(self):
        """Clear the display"""
        if self.gui:
            self.gui.clear_display()
        self.answer_generator.clear_history()
        print("\n[CLEARED] Display and history cleared")
    
    def toggle_window(self):
        """Toggle window visibility"""
        if self.gui:
            self.gui.toggle_visibility()
    
    def run_gui(self):
        """Run the GUI application"""
        self.gui = OverlayWindow()
        
        # Connect button callbacks using new setter methods
        self.gui.set_screen_callback(self.toggle_screen_reading)
        self.gui.set_listen_callback(self.toggle_listening)
        
        # Setup hotkeys after GUI is created
        self.setup_hotkeys()
        
        # Update initial status
        self.gui.update_status("Ready (Click Start or Ctrl+Shift+L)")
        
        # Run GUI main loop
        self.gui.run()
    
    def run(self):
        """Main application entry point"""
        if not self.initialize():
            print("Failed to initialize. Please check your configuration.")
            return
        
        print("\n" + "="*60)
        print("InterGuide - Interview Assistant")
        print("="*60)
        print("\nStarting GUI...")
        
        # Run GUI (this will block until window is closed)
        self.run_gui()


def main():
    """Entry point"""
    try:
        # Suppress NumPy warnings
        import warnings
        warnings.filterwarnings('ignore')
        
        app = InterviewAssistant()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
    except Exception as e:
        print(f"\n❌ Application Error: {e}")
        import traceback
        traceback.print_exc()
        print("\n" + "="*60)
        print("  Troubleshooting Tips:")
        print("="*60)
        print("1. Check that your OpenAI API key is configured in .env")
        print("2. Make sure all dependencies are installed: pip install -r requirements.txt")
        print("3. Try running as Administrator for hotkey support")
        print("4. Check the README_INSTALL.md for more help")
        print("\nPress Enter to exit...")
        try:
            input()
        except:
            import time
            time.sleep(5)


if __name__ == "__main__":
    main()
