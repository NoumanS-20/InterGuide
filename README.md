<div align="center">

# 🧠 InterGuide

**Invisible AI Interview Copilot for Any Screen**

<!-- Status & Meta Badges -->
<p>
  <img src="https://img.shields.io/badge/Status-Active%20Development-22c55e?style=for-the-badge&logo=github" alt="Status" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-0ea5e9?style=for-the-badge&logo=electron" alt="Platforms" />
  <img src="https://img.shields.io/badge/AI-Gemini%20Powered-f97316?style=for-the-badge&logo=google" alt="AI" />
</p>

<p>
  <img src="https://img.shields.io/badge/Use%20Case-Technical%20Interviews-6366f1?style=flat-square" />
  <img src="https://img.shields.io/badge/Stealth-Overlay%20%2F%20Click--Through-f97316?style=flat-square" />
  <img src="https://img.shields.io/badge/Mode-Screenshot%20%2B%20Chat-22c55e?style=flat-square" />
</p>

---

</div>

InterGuide is a **stealth AI assistant** that lives as a tiny overlay on your screen. 

- Capture your **live interview screen** in one shortcut.
- Let **Gemini** analyze the question.
- Get **structured, language‑specific answers** in a clean, draggable window.
- All while staying visually minimal and disguised as a normal system process.

---

## ✨ Feature Highlights

### 🥷 Stealth‑First Design
- Floating overlay that looks like a regular utility bar.
- Can be set to **click‑through** so it doesnt block your clicks.
- Hides from screen recordings on many setups using content protection.
- Window titles and icons can be disguised as system apps (Terminal / Activity / Settings).

### 🧠 Smart AI Assistance
- Powered by **Google Gemini** (configurable with your own API key).
- Optimized prompt for **DSA / coding interview** style problems.
- Understands **screenshots of coding questions** and returns:
  - Explanation in plain English.
  - Clean code in your chosen language.
  - Time & space complexity.

### 💬 Natural Interaction
- Floating **overlay bar**:
  - Screenshot capture button.
  - Mic button (when speech is configured).
  - Skill selector (DSA by default).
  - Language selector (C++, C, Java, Python, JavaScript).
- **Answer window**:
  - Split view (text + code) with syntax highlighting.
  - Draggable, resizable, always on top.
- **Chat window** for longer back‑and‑forth conversations.

### 🎛️ Global Shortcuts (Default)

> All shortcuts work even when InterGuide windows are in click‑through mode.

| Action                  | Shortcut                      |
|-------------------------|-------------------------------|
| Screenshot & Analyze    | `Ctrl/Cmd + Shift + S`        |
| Toggle Visibility       | `Ctrl/Cmd + Shift + V`        |
| Toggle Interaction      | `Ctrl/Cmd + Shift + I` or `Alt + A` |
| Open Chat               | `Ctrl/Cmd + Shift + C`        |
| Toggle Speech (if set)  | `Alt + R`                     |
| Open Settings           | `Ctrl/Cmd + ,`                |

---

## 🚀 1‑Command Setup

InterGuide is designed so you can go from **zero to running** with a single command.

```bash
./setup.sh
```

That script will:

1. **Check Environment**
   - Validate Node.js & npm.
   - Detect your OS (Windows / macOS / Linux).
2. **Prepare Config**
   - Create a `.env` file (or reuse existing).
   - Guide you to paste your **Gemini API key**.
3. **Install Dependencies**
   - Run `npm install` or optionally `npm ci`.
4. **Launch InterGuide**
   - Start the Electron app ready for use.

> If the script detects that your API key is missing or placeholder, it will **stop with a clear message** and show you exactly what to do.

### 🔑 Getting Your Gemini API Key

1. Go to **[Google AI Studio](https://aistudio.google.com/)**.
2. Create a new API key.
3. When `setup.sh` pauses and asks, open `.env` and set:

```env
GEMINI_API_KEY=your_real_gemini_api_key_here
```

Then re‑run:

```bash
./setup.sh
```

---

## ⚙️ Advanced Setup Options

You can customize behavior with flags:

```bash
./setup.sh --help
```

Common flows:

```bash
# Install deps, configure, then build a distributable for this OS
./setup.sh --build

# Install deps and configure only, do NOT auto‑run the app
./setup.sh --no-run

# Use npm ci when package-lock.json exists (CI‑style clean install)
./setup.sh --ci

# Best‑effort install of audio/system deps (e.g., sox for mic capture)
./setup.sh --install-system-deps
```

Under the hood, the script will select the right build target:

- macOS → `npm run build:mac`
- Windows → `npm run build:win`
- Linux → `npm run build:linux`

and fall back to `npm run build` when needed.

---

## 💡 Day‑to‑Day Usage

1. **Start InterGuide**
   - Either via `npm start` or simply re‑run `./setup.sh` and let it launch.

2. **Position the Overlay**
   - Drag the main bar to the top or side of your screen.
   - Use `Alt + A` to switch between **interactive** and **click‑through**.

3. **Capture a Question**
   - Hit `Ctrl/Cmd + Shift + S` to take a screenshot.
   - InterGuide sends the image to Gemini with your DSA prompt.

4. **Read & Act**
   - Answer window will pop up with explanation and code.
   - Copy code and paste into your IDE/editor.

5. **Refine via Chat**
   - `Ctrl/Cmd + Shift + C` to open chat.
   - Ask follow‑ups, change constraints, request optimizations, etc.

---

## 🛠️ Tech Stack

- **Electron** for cross‑platform desktop app.
- **Node.js** for backend logic and window management.
- **Google Gemini API** for LLM reasoning & image understanding.
- **Custom overlay windows** with content protection and always‑on‑top logic.

---

## 🧪 Troubleshooting Checklist

**Setup doesnt run:**
- Ensure `node -v` shows Node **18+**.
- On Windows, run in **Git Bash / WSL / any bash shell**.

**App starts but API fails:**
- Double‑check `GEMINI_API_KEY` in `.env`.
- Make sure the key still works in Google AI Studio.

**Screenshot capture issues (macOS):**
- System Settings → Privacy & Security → **Screen Recording**.
- Enable permissions for your terminal/app launching InterGuide.

**Voice / mic not working:**
- Voice support is optional and depends on `sox` + Azure Speech keys.
- You can ignore mic warnings if you only want screenshot/chat.

---

## ⚖️ Responsible Use

InterGuide includes features designed for minimal visual footprint and rapid screenshot analysis. These capabilities can be misused. Use InterGuide responsibly and ensure you comply with all applicable laws, employer policies, and platform terms of service. Do not use the tool to deceive, invade privacy, or violate security or interview processes.

If you distribute or deploy this software, include a clear notice to end users about intended, lawful uses and obtain any required permissions (for screen recording, audio capture, or system-level integrations).

---

## 📦 Build & Distribution

Once you are confident with your config:

```bash
# Build for your current OS
./setup.sh --build

# or directly
npm run build:win    # Windows
npm run build:mac    # macOS
npm run build:linux  # Linux
```

The packaged app will be created under `dist/` using **electron-builder**.

---

## ✅ Status & Roadmap (High‑Level)

- [x] Stealth floating overlay bar.
- [x] Screenshot → Gemini → Answer flow.
- [x] Split answer window (text + code) with markdown and syntax highlighting.
- [x] Chat window with session history.
- [x] Basic stealth modes (name/icon disguise, taskbar hiding, content protection).
- [ ] Auto‑hide when screen sharing is detected.
- [ ] Multiple AI backends (OpenAI, Anthropic, local models).
- [ ] Export sessions as Markdown/PDF.
- [ ] Advanced stealth modes and behavioral profiles.

---

<div align="center">

If InterGuide helps you in practice rounds or real interviews,
**consider starring your fork or sharing it with a friend.**

**Made with ❤️ for candidates who want a silent safety net.**

**Created by Nouman Shafique (@NoumanS-20)**

</div>
