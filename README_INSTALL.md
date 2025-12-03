# InterGuide - Installation Guide

## 🚀 Quick Install (Desktop Icon)

### Method 1: Automatic Installation (Recommended)

1. **Run the installer:**
   ```cmd
   install.bat
   ```
   
2. **Or run manually:**
   ```cmd
   python setup.py
   ```

3. **Find the desktop icon** and double-click to launch!

### Method 2: Manual Setup

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure API key:**
   - Edit `.env` file
   - Add your OpenAI API key: `OPENAI_API_KEY=sk-your-key-here`

3. **Create desktop shortcut:**
   - Right-click `InterGuide.vbs` → Send to → Desktop (create shortcut)
   - Or right-click `InterGuide.bat` → Send to → Desktop (create shortcut)

## 📱 Using the Desktop Icon

**Double-click the InterGuide icon** on your desktop to launch the app.

The application window will appear in the top-right corner with:
- 🔴 Recording indicator bar
- ▶ Start/Stop listening button
- 📸 Screen reading toggle
- Clear button

## ⌨️ Controls

### GUI Buttons (Always Work)
- **▶ Start Listening** - Begin recording and answering questions
- **⏸ Stop Listening** - Pause the assistant
- **Screen: OFF/ON** - Toggle screen capture analysis
- **Clear** - Clear the display

### Keyboard Shortcuts (Requires Admin)
- `Ctrl+Shift+L` - Start/Stop listening
- `Ctrl+Shift+S` - Toggle screen reading
- `Ctrl+Shift+C` - Clear display
- `Ctrl+Shift+H` - Hide/Show window

## 🔒 Running with Admin Privileges (for Hotkeys)

To enable keyboard shortcuts:

1. Right-click the **InterGuide** desktop icon
2. Select **Properties**
3. Click **Advanced** button
4. Check **"Run as administrator"**
5. Click **OK** twice

## 🎯 How to Use

1. **Launch the app** from desktop icon
2. **Configure your interview:**
   - Click "Start Listening" or press Ctrl+Shift+L
   - Enable "Screen Reading" if you want AI to analyze visible content
3. **During the interview:**
   - Speak or let the interviewer ask questions
   - Read suggested answers from the overlay window
   - Use answers as talking points, personalize your response
4. **Manage the session:**
   - Click "Clear" to reset between questions
   - Adjust opacity slider for transparency

## ⚙️ Configuration

Edit `.env` file to customize:

```env
# Your OpenAI API key
OPENAI_API_KEY=sk-your-key-here

# AI Model (gpt-4o-mini is recommended)
OPENAI_MODEL=gpt-4o-mini

# Window settings
WINDOW_OPACITY=0.9
WINDOW_WIDTH=600
WINDOW_HEIGHT=400
```

## 🔧 Troubleshooting

### Desktop icon doesn't work
- Make sure `InterGuide.vbs` or `InterGuide.bat` exists
- Try running `install.bat` again

### Hotkeys not working
- Run the app as Administrator (see "Running with Admin Privileges" above)
- Or use the GUI buttons instead

### "OPENAI_API_KEY is required" error
- Edit `.env` file and add your API key
- Get your key from: https://platform.openai.com/api-keys

### App crashes or doesn't start
- Run `pip install -r requirements.txt` again
- Check if Python 3.8+ is installed: `python --version`
- Try running from command line to see errors: `python main.py`

### NumPy warnings
- These are normal for Python 3.14 - the app will still work
- Consider using Python 3.11-3.13 for optimal stability

## 📁 File Structure

```
InterGuide/
├── InterGuide.vbs          # Silent launcher (no console)
├── InterGuide.bat          # Launcher with console
├── install.bat             # Quick installer
├── setup.py                # Python installer script
├── main.py                 # Main application
├── .env                    # Your configuration
└── (other project files)
```

## 🎓 Tips for Best Results

- **Position the window** where you can glance at it naturally
- **Don't read answers verbatim** - use them as talking points
- **Enable screen reading** for technical interviews with code/diagrams
- **Practice beforehand** to get comfortable with the interface
- **Adjust opacity** to make the window blend better

## 💰 Cost Information

Using OpenAI API (gpt-4o-mini):
- Typical 1-hour interview: **$0.10 - $0.30**
- Very affordable for practice and real interviews

## ⚠️ Ethical Disclaimer

This tool is designed for:
- ✅ Interview preparation and practice
- ✅ Learning and skill development
- ✅ Building confidence

Be aware that many companies consider AI assistance during real interviews inappropriate. Use responsibly and ethically.

## 🆘 Need More Help?

- Check the main `README.md` for detailed documentation
- See `SETUP_GUIDE.md` for troubleshooting
- Review `QUICKSTART.md` for usage tips

---

**Ready to go! Double-click your desktop icon to start! 🚀**
