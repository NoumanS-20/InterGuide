import whisper
import numpy as np
import tempfile
import wave
from config import Config

class SpeechRecognizer:
    """Handles speech-to-text conversion using Whisper"""
    
    def __init__(self):
        self.model_size = Config.WHISPER_MODEL_SIZE
        self.model = None
        self.sample_rate = Config.SAMPLE_RATE
        
    def load_model(self):
        """Load the Whisper model"""
        if self.model is None:
            print(f"Loading Whisper model ({self.model_size})...")
            try:
                self.model = whisper.load_model(self.model_size)
                print("Model loaded successfully")
            except Exception as e:
                print(f"Error loading model: {e}")
                raise
                
    def transcribe_audio(self, audio_data):
        """
        Transcribe audio data to text
        
        Args:
            audio_data: numpy array of audio samples
            
        Returns:
            str: Transcribed text
        """
        if self.model is None:
            self.load_model()
            
        if audio_data is None or len(audio_data) == 0:
            return ""
        
        try:
            # Normalize audio to float32
            if audio_data.dtype != np.float32:
                audio_data = audio_data.astype(np.float32)
                
            # Normalize to [-1, 1] range if needed
            if audio_data.max() > 1.0 or audio_data.min() < -1.0:
                audio_data = audio_data / np.abs(audio_data).max()
            
            # Transcribe
            result = self.model.transcribe(
                audio_data,
                language='english',
                fp16=False,
                verbose=False
            )
            
            text = result['text'].strip()
            print(f"Transcribed: {text}")
            return text
            
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""
    
    def transcribe_from_file(self, audio_file_path):
        """
        Transcribe audio from a file
        
        Args:
            audio_file_path: Path to audio file
            
        Returns:
            str: Transcribed text
        """
        if self.model is None:
            self.load_model()
            
        try:
            result = self.model.transcribe(audio_file_path, language='english')
            return result['text'].strip()
        except Exception as e:
            print(f"Error transcribing file: {e}")
            return ""
    
    def save_audio_to_file(self, audio_data, filename=None):
        """Save audio data to a WAV file"""
        if filename is None:
            filename = tempfile.mktemp(suffix='.wav')
            
        # Normalize audio data
        if audio_data.dtype == np.float32:
            # Convert float32 to int16
            audio_data = (audio_data * 32767).astype(np.int16)
        
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(Config.CHANNELS)
            wf.setsampwidth(2)  # 2 bytes for int16
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio_data.tobytes())
            
        return filename
