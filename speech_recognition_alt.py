# Alternative implementation using Google Speech Recognition
# This works with Python 3.14 and doesn't require Numba

import speech_recognition as sr
import tempfile
import wave
import numpy as np
from config import Config

class SpeechRecognizer:
    """Handles speech-to-text conversion using Google Speech Recognition API"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sample_rate = Config.SAMPLE_RATE
        
    def load_model(self):
        """Initialize the recognizer (no model loading needed for Google API)"""
        print("Using Google Speech Recognition API")
        print("Speech recognizer initialized successfully")
                
    def transcribe_audio(self, audio_data):
        """
        Transcribe audio data to text using Google Speech Recognition
        
        Args:
            audio_data: numpy array of audio samples
            
        Returns:
            str: Transcribed text
        """
        if audio_data is None or len(audio_data) == 0:
            return ""
        
        try:
            # Convert numpy array to AudioData format
            # Normalize audio to int16
            if audio_data.dtype == np.float32:
                audio_data = (audio_data * 32767).astype(np.int16)
            elif audio_data.dtype != np.int16:
                audio_data = audio_data.astype(np.int16)
            
            # Create AudioData object
            audio = sr.AudioData(
                audio_data.tobytes(), 
                self.sample_rate, 
                2  # sample width in bytes (int16 = 2 bytes)
            )
            
            # Transcribe using Google Speech Recognition
            try:
                text = self.recognizer.recognize_google(audio, language='en-US')
                print(f"Transcribed: {text}")
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return ""
            
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
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio = self.recognizer.record(source)
                
            try:
                text = self.recognizer.recognize_google(audio, language='en-US')
                return text
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                print(f"Error: {e}")
                return ""
                
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
