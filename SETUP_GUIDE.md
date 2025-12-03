# InterGuide Setup Guide for Python 3.14

## Current Status

✅ **Successfully Installed:**
- numpy
- python-dotenv
- requests
- sounddevice
- openai
- tiktoken
- pynput
- keyboard
- SpeechRecognition
- pywin32
- torch & torchaudio

❌ **PyAudio Issue:**
PyAudio requires Microsoft Visual C++ Build Tools to compile on Windows with Python 3.14.

## Option 1: Skip PyAudio (Recommended - Already Working!)

The app works WITHOUT PyAudio! We're using `sounddevice` instead which is already installed.

**No additional steps needed - you can run the app now!**

## Option 2: Install PyAudio (Optional)

If you want PyAudio for advanced audio features:

### Method A: Download Pre-built Wheel
1. Visit: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download: `PyAudio‑0.2.14‑cp314‑cp314‑win_amd64.whl` (for Python 3.14, 64-bit)
3. Install:
   ```powershell
   pip install path\to\PyAudio‑0.2.14‑cp314‑cp314‑win_amd64.whl
   ```

### Method B: Install Visual C++ Build Tools
1. Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Install "Desktop development with C++"
3. Restart terminal and run:
   ```powershell
   pip install PyAudio
   ```

## Final Setup Steps

### 1. Configure OpenAI API Key

Edit `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

### 2. Test the Application

```powershell
python main.py
```

### 3. Using the App

1. **Start the app**: The overlay window will appear in the top-right corner
2. **Press Ctrl+Shift+L**: Start listening for questions
3. **Speak or let the interviewer speak**: The app will transcribe and generate answers
4. **Read the suggested answer**: Use it as guidance during your response
5. **Press Ctrl+Shift+C**: Clear the display
6. **Press Ctrl+Shift+H**: Hide/Show the window

## Keyboard Shortcuts

- **Ctrl+Shift+L** - Start/Stop listening
- **Ctrl+Shift+C** - Clear display
- **Ctrl+Shift+H** - Hide/Show window

## Troubleshooting

### "OPENAI_API_KEY is required"
- Edit `.env` file and add your API key
- Make sure there are no quotes or extra spaces

### "No audio input detected"
- Check Windows sound settings
- Make sure your microphone is set as the default device
- Allow microphone permissions for Python

### "Could not understand audio"
- Speak more clearly or louder
- Check microphone levels in Windows sound settings
- Adjust `SILENCE_THRESHOLD` in `config.py`

### Speech Recognition Not Working
- You need an internet connection (uses Google Speech Recognition API)
- Alternatively, install Whisper with Python 3.13 or lower

## About Speech Recognition

This app uses **Google Speech Recognition API** which:
- ✅ Works with Python 3.14
- ✅ Free to use
- ✅ Good accuracy
- ⚠️ Requires internet connection
- ⚠️ May have rate limits

**Alternative**: If you want offline speech recognition:
1. Downgrade to Python 3.13
2. Install: `pip install openai-whisper torch torchaudio`
3. Use the original `speech_recognition.py` instead of `speech_recognition_alt.py`

## Cost Estimate

### OpenAI API (GPT-4o-mini)
- Input: ~$0.15 per 1M tokens
- Output: ~$0.60 per 1M tokens
- **Typical 1-hour interview**: $0.10 - $0.30

### Google Speech Recognition
- Free for moderate use
- No API key required

## Ready to Use!

Your app is ready to go! Just:
1. Add your OpenAI API key to `.env`
2. Run `python main.py`
3. Press Ctrl+Shift+L to start

Good luck with your interviews! 🚀
