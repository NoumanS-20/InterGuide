import sounddevice as sd
import numpy as np
import queue
import threading
from config import Config

class AudioCapture:
    """Handles audio capture from system microphone"""
    
    def __init__(self):
        self.sample_rate = Config.SAMPLE_RATE
        self.channels = Config.CHANNELS
        self.chunk_size = Config.CHUNK_SIZE
        self.is_recording = False
        self.audio_queue = queue.Queue()
        self.recorded_frames = []
        self.stream = None
        self.silence_threshold = Config.SILENCE_THRESHOLD
        self.silence_duration = Config.SILENCE_DURATION
        self.silence_counter = 0
        
    def audio_callback(self, indata, frames, time, status):
        """Callback function for audio stream"""
        if status:
            print(f"Audio status: {status}")
        
        # Add audio data to queue
        if self.is_recording:
            self.audio_queue.put(indata.copy())
            
    def start_recording(self):
        """Start recording audio"""
        if self.is_recording:
            return
            
        self.is_recording = True
        self.recorded_frames = []
        self.audio_queue = queue.Queue()
        self.silence_counter = 0
        
        try:
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                callback=self.audio_callback,
                blocksize=self.chunk_size
            )
            self.stream.start()
            print("Recording started...")
        except Exception as e:
            print(f"Error starting recording: {e}")
            self.is_recording = False
            
    def stop_recording(self):
        """Stop recording and return audio data"""
        if not self.is_recording:
            return None
            
        self.is_recording = False
        
        if self.stream:
            self.stream.stop()
            self.stream.close()
            
        # Collect all recorded frames
        while not self.audio_queue.empty():
            self.recorded_frames.append(self.audio_queue.get())
            
        if not self.recorded_frames:
            return None
            
        # Concatenate all frames
        audio_data = np.concatenate(self.recorded_frames, axis=0)
        print(f"Recording stopped. Captured {len(audio_data)} frames")
        
        return audio_data.flatten()
    
    def get_audio_chunk(self, duration=5):
        """Record audio for a specific duration"""
        self.start_recording()
        
        # Record for specified duration
        frames_to_record = int(self.sample_rate * duration / self.chunk_size)
        
        for _ in range(frames_to_record):
            if not self.audio_queue.empty():
                self.recorded_frames.append(self.audio_queue.get())
                
        return self.stop_recording()
    
    def is_silent(self, audio_chunk):
        """Check if audio chunk is silent"""
        if audio_chunk is None or len(audio_chunk) == 0:
            return True
        
        # Calculate RMS (Root Mean Square) to measure audio level
        rms = np.sqrt(np.mean(audio_chunk**2))
        return rms < self.silence_threshold
    
    def list_audio_devices(self):
        """List all available audio devices"""
        print("\nAvailable audio devices:")
        print(sd.query_devices())
        
    def set_input_device(self, device_id):
        """Set the input device"""
        sd.default.device = device_id
