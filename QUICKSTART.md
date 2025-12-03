# 🎯 InterGuide - Quick Start

## ✅ Installation Complete!

All dependencies have been successfully installed. Your app is ready to use!

## 📋 Next Steps

### 1. **Get Your OpenAI API Key** (Required)

1. Go to: https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### 2. **Configure the App**

Edit the `.env` file in this folder and replace:
```
OPENAI_API_KEY=your_openai_api_key_here
```

With your actual key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 3. **Run the App**

**Option A - Easy Start:**
```powershell
.\start.ps1
```

**Option B - Direct Start:**
```powershell
python main.py
```

## 🎮 How to Use

1. **Join your interview** (Zoom, Google Meet, or Teams)
2. **Position the window** - The overlay appears in the top-right corner
3. **Press `Ctrl+Shift+L`** - Start listening for questions
4. **Read the answers** - They appear in the overlay window
5. **Respond naturally** - Use suggestions as talking points, not scripts
6. **Press `Ctrl+Shift+C`** - Clear display when needed

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+L` | Start/Stop listening |
| `Ctrl+Shift+C` | Clear display |
| `Ctrl+Shift+H` | Hide/Show window |

## 🔧 How It Works

1. **Listens** - Captures audio from your microphone in 5-second chunks
2. **Transcribes** - Uses Google Speech Recognition to convert speech to text
3. **Generates** - Sends questions to OpenAI GPT for intelligent answers
4. **Displays** - Shows both question and answer in the overlay window

## 📱 Compatible With

- ✅ Zoom Desktop App
- ✅ Zoom in Browser (Chrome/Edge)
- ✅ Google Meet (Chrome/Edge)
- ✅ Microsoft Teams Desktop
- ✅ Microsoft Teams in Browser

## ⚡ Important Notes

### Audio Setup
- Make sure your **microphone is working** and set as default in Windows
- The app listens to whatever your microphone picks up
- For best results, use headphones so the interviewer's voice comes through clearly

### Internet Required
- Google Speech Recognition API requires internet connection
- OpenAI API also needs internet access

### Speech Recognition
- Uses **Google Speech Recognition** (free, but needs internet)
- Alternatives available if you prefer offline (see SETUP_GUIDE.md)

### API Costs (Minimal)
Using `gpt-4o-mini`:
- Typical 1-hour interview: **$0.10 - $0.30**
- Very affordable for practice and real interviews

## 🎨 Customization

Edit `.env` file to change:
- `WINDOW_WIDTH` - Width of overlay window
- `WINDOW_HEIGHT` - Height of overlay window  
- `WINDOW_OPACITY` - Transparency (0.3 to 1.0)
- `OPENAI_MODEL` - AI model (gpt-4o-mini, gpt-4o, etc.)

## 🐛 Troubleshooting

### "OPENAI_API_KEY is required"
→ Edit `.env` and add your API key

### "No audio detected"
→ Check Windows sound settings
→ Make sure microphone is set as default device
→ Try speaking louder or adjusting `SILENCE_THRESHOLD` in `config.py`

### "Could not understand audio"
→ Check internet connection
→ Speak more clearly
→ Reduce background noise

### Window not showing
→ Press `Ctrl+Shift+H` to show
→ Check if it's behind other windows

## 📚 More Help

- **Full Documentation**: See `README.md`
- **Setup Details**: See `SETUP_GUIDE.md`
- **Troubleshooting**: Check both files above

## ⚠️ Ethical Use

**Important Disclaimer:**
- This tool is for **educational and practice purposes**
- Using AI during real interviews may violate company policies
- Best used for **interview preparation** and practice sessions
- Use responsibly and ethically

## 🚀 Ready to Start!

1. ✅ Dependencies installed
2. ⏳ Add your OpenAI API key to `.env`
3. ⏳ Run `python main.py` or `.\start.ps1`
4. ⏳ Press `Ctrl+Shift+L` to start listening

**Good luck with your interviews!** 🎯

---

**Need Help?** Check the troubleshooting sections in README.md and SETUP_GUIDE.md
