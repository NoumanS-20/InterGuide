# InterGuide - Interview Assistant

An AI-powered Windows application that listens to interview questions and provides intelligent answer suggestions in real-time. Compatible with Zoom, Google Meet, Microsoft Teams (both desktop apps and browser versions).

## Features

- 🎤 **Real-time Audio Capture**: Listens to interview questions through your microphone
- 🗣️ **Speech-to-Text**: Uses OpenAI Whisper for accurate transcription
- 🤖 **AI-Powered Answers**: Generates contextual answers using OpenAI GPT models
- 🪟 **Always-On-Top Overlay**: Transparent window that stays above meeting apps
- ⌨️ **Keyboard Shortcuts**: Quick controls without interrupting your interview
- 📝 **Conversation Context**: Maintains conversation history for better context
- 🎨 **Customizable UI**: Adjustable opacity and positioning

## Prerequisites

- Windows 10/11
- Python 3.8 or higher
- OpenAI API key
- Microphone

## Installation

### 1. Clone or Download the Project

```powershell
cd C:\Users\nouma\OneDrive\Desktop\InterGuide
```

### 2. Create a Virtual Environment (Recommended)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

**Note**: Installing `openai-whisper` will also install PyTorch, which is quite large (~2GB). This is normal.

### 4. Install PyAudio (Special Instructions for Windows)

PyAudio can be tricky on Windows. If the pip install fails:

**Option A**: Use a pre-built wheel
```powershell
pip install pipwin
pipwin install pyaudio
```

**Option B**: Download from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Download the appropriate `.whl` file for your Python version
- Install it: `pip install PyAudio‑0.2.14‑cp311‑cp311‑win_amd64.whl`

### 5. Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```powershell
   copy .env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

3. (Optional) Adjust other settings like model size, window dimensions, etc.

## Configuration

Edit the `.env` file to customize:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini  # or gpt-4, gpt-3.5-turbo

# Whisper Model Size (tiny, base, small, medium, large)
# Smaller = faster, larger = more accurate
WHISPER_MODEL_SIZE=base

# Audio Settings
SAMPLE_RATE=16000
CHUNK_SIZE=1024

# UI Settings
WINDOW_OPACITY=0.9
WINDOW_WIDTH=600
WINDOW_HEIGHT=400
```

## Usage

### Starting the Application

```powershell
python main.py
```

### Keyboard Shortcuts

- **Ctrl+Shift+L**: Start/Stop listening for questions
- **Ctrl+Shift+C**: Clear the display and conversation history
- **Ctrl+Shift+H**: Hide/Show the overlay window

### Workflow

1. **Start the app**: Run `python main.py`
2. **Position the window**: Drag it to a convenient location on your screen
3. **Join your interview**: Open Zoom, Google Meet, or Teams
4. **Start listening**: Press `Ctrl+Shift+L` to begin
5. **Read answers**: The app will display detected questions and suggested answers
6. **Respond naturally**: Use the suggestions as guidance, personalize your response
7. **Clear as needed**: Press `Ctrl+Shift+C` to clear the display

## How It Works

1. **Audio Capture**: The app continuously records audio from your microphone in 5-second chunks
2. **Speech Recognition**: OpenAI Whisper transcribes the audio to text
3. **Question Detection**: Only processes audio that contains speech (filters silence)
4. **Answer Generation**: Sends the question to OpenAI GPT for intelligent answer generation
5. **Display**: Shows both the question and suggested answer in the overlay window

## Tips for Best Results

### Audio Setup
- Use a good quality microphone
- Test your microphone levels before the interview
- Ensure the interviewer's voice is clear in your speakers/headphones
- Adjust `SILENCE_THRESHOLD` in `config.py` if needed

### Model Selection
- **Whisper base**: Good balance of speed and accuracy (recommended)
- **Whisper small**: Faster, slightly less accurate
- **Whisper medium/large**: More accurate but slower

### GPT Model
- **gpt-4o-mini**: Fast and cost-effective (recommended for testing)
- **gpt-4o**: More accurate and contextual answers
- **gpt-3.5-turbo**: Fastest and cheapest option

### During the Interview
- Position the window where you can see it naturally without obvious eye movement
- Don't read answers verbatim - use them as talking points
- Pause briefly before answering to appear thoughtful
- Personalize the answers with your own experience

## Compatibility

### Meeting Platforms
- ✅ Zoom Desktop App
- ✅ Zoom in Chrome/Edge
- ✅ Google Meet (Chrome/Edge)
- ✅ Microsoft Teams Desktop App
- ✅ Microsoft Teams (Chrome/Edge)

### Browser Compatibility
- Chrome (all features)
- Edge (all features)
- Firefox (all features)

## Troubleshooting

### "No module named 'pyaudio'"
- Follow the PyAudio installation instructions in step 4 above
- Make sure you're using the correct Python version wheel file

### "OPENAI_API_KEY is required"
- Ensure your `.env` file exists and contains your API key
- Check that there are no extra spaces or quotes around the key

### Audio Not Being Captured
- Check Windows sound settings - ensure your microphone is set as default
- Test with: `python -c "from audio_capture import AudioCapture; a = AudioCapture(); a.list_audio_devices()"`
- Adjust `SILENCE_THRESHOLD` in `config.py` if audio is always detected as silent

### Transcription Not Working
- First run will download the Whisper model (this can take a few minutes)
- Try a smaller model size if having performance issues
- Ensure PyTorch is installed correctly: `pip list | grep torch`

### Window Not Showing
- Press `Ctrl+Shift+H` to show the window
- Check if it's hidden behind other windows
- Restart the application

### High CPU/Memory Usage
- Use a smaller Whisper model (tiny or base)
- Switch to `gpt-3.5-turbo` for faster responses
- Close other unnecessary applications

## Cost Considerations

### OpenAI API Costs
- **Whisper**: Runs locally, no API costs
- **GPT-4o-mini**: ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens
- **GPT-4o**: ~$2.50 per 1M input tokens, ~$10 per 1M output tokens

Typical interview (1 hour, ~20 questions):
- With gpt-4o-mini: ~$0.10-0.30
- With gpt-4o: ~$1-3

## Privacy & Ethics

⚠️ **Important Disclaimer**:
- This tool is for educational and practice purposes
- Using AI assistance during real interviews may violate company policies
- Many companies consider this cheating and may revoke offers if discovered
- Use responsibly and ethically
- Best used for interview preparation and practice sessions

## File Structure

```
InterGuide/
├── main.py                  # Main application entry point
├── config.py                # Configuration settings
├── audio_capture.py         # Audio recording functionality
├── speech_recognition.py    # Whisper integration
├── answer_generator.py      # OpenAI GPT integration
├── overlay_gui.py           # GUI overlay window
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment variables
├── .env                    # Your actual config (create this)
└── README.md               # This file
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

MIT License - feel free to use and modify as needed.

## Disclaimer

This software is provided as-is for educational purposes. The authors are not responsible for any misuse or consequences of using this software. Always follow ethical guidelines and company policies during interviews.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Ensure all dependencies are correctly installed
3. Verify your `.env` configuration
4. Check that your OpenAI API key is valid and has credits

---

**Good luck with your interview preparation! 🚀**
