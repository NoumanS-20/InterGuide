import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration settings for the Interview Assistant"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
    
    # Whisper Settings
    WHISPER_MODEL_SIZE = os.getenv('WHISPER_MODEL_SIZE', 'base')
    
    # Audio Settings
    SAMPLE_RATE = int(os.getenv('SAMPLE_RATE', '16000'))
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', '1024'))
    CHANNELS = 1
    AUDIO_FORMAT = 'int16'
    SILENCE_THRESHOLD = 500  # Adjust based on your microphone
    SILENCE_DURATION = 2.0  # seconds of silence before processing
    
    # UI Settings
    WINDOW_OPACITY = float(os.getenv('WINDOW_OPACITY', '0.9'))
    WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', '600'))
    WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', '400'))
    
    # Hotkeys
    HOTKEY_START_STOP = 'ctrl+shift+l'  # Start/Stop listening
    HOTKEY_CLEAR = 'ctrl+shift+c'  # Clear display
    HOTKEY_TOGGLE_WINDOW = 'ctrl+shift+h'  # Hide/Show window
    HOTKEY_SCREEN_READING = 'ctrl+shift+s'  # Toggle screen reading
    
    # System Prompt for Answer Generation
    SYSTEM_PROMPT = """You are an intelligent interview assistant. Your role is to provide clear, 
concise, and accurate answers to interview questions.

When analyzing screenshots:
- Look for visible text, code, diagrams, or questions on screen
- Incorporate relevant visual information into your answer
- Mention if you see technical details that support your response

Focus on:
1. Providing technically accurate information
2. Structuring answers using the STAR method when appropriate (Situation, Task, Action, Result)
3. Being concise but comprehensive (under 200 words)
4. Highlighting key points that demonstrate competence
5. Using any visible screen content to enhance your answer

Keep answers professional and interview-appropriate."""

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in .env file")
        return True
