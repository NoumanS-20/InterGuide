import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
from config import Config

class OverlayWindow:
    """Creates an always-on-top overlay window to display answers"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("InterGuide - Interview Assistant")
        
        # Window configuration
        self.window_width = Config.WINDOW_WIDTH
        self.window_height = Config.WINDOW_HEIGHT + 30  # Extra space for recording bar
        self.opacity = Config.WINDOW_OPACITY
        
        # Position window in top-right corner
        screen_width = self.root.winfo_screenwidth()
        x_position = screen_width - self.window_width - 20
        y_position = 20
        
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x_position}+{y_position}")
        
        # Make window always on top and semi-transparent
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', self.opacity)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.is_visible = True
        self.is_recording = False
        self.screen_reading = False
        
        self._create_widgets()
        
    def _create_widgets(self):
        """Create UI widgets"""
        # Recording indicator bar (at the very top)
        self.recording_bar = tk.Frame(self.root, bg='#444444', height=30)
        self.recording_bar.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        self.recording_label = tk.Label(
            self.recording_bar,
            text="⚫ IDLE",
            fg="white",
            bg="#444444",
            font=('Arial', 10, 'bold'),
            pady=5
        )
        self.recording_label.pack()
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title label
        title_label = ttk.Label(
            main_frame,
            text="InterGuide - Interview Assistant",
            font=('Arial', 12, 'bold')
        )
        title_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # Status label with screen reading indicator
        self.status_label = ttk.Label(
            main_frame,
            text="Status: Ready (Ctrl+Shift+L to start) | Screen Reading: OFF",
            font=('Arial', 9)
        )
        self.status_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        
        # Question display
        question_frame = ttk.LabelFrame(main_frame, text="Question Detected", padding="5")
        question_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        question_frame.columnconfigure(0, weight=1)
        question_frame.rowconfigure(0, weight=1)
        
        self.question_text = scrolledtext.ScrolledText(
            question_frame,
            wrap=tk.WORD,
            width=60,
            height=3,
            font=('Arial', 10),
            bg='#f0f0f0'
        )
        self.question_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Answer display
        answer_frame = ttk.LabelFrame(main_frame, text="Suggested Answer", padding="5")
        answer_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        answer_frame.columnconfigure(0, weight=1)
        answer_frame.rowconfigure(0, weight=1)
        
        self.answer_text = scrolledtext.ScrolledText(
            answer_frame,
            wrap=tk.WORD,
            width=60,
            height=12,
            font=('Arial', 10),
            bg='#e8f4f8'
        )
        self.answer_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Listening control button
        self.listen_button = ttk.Button(
            button_frame,
            text="▶ Start Listening (Ctrl+Shift+L)",
            command=self.on_listen_button_click
        )
        self.listen_button.pack(side=tk.LEFT, padx=5)
        
        # Buttons
        self.clear_button = ttk.Button(
            button_frame,
            text="Clear (Ctrl+Shift+C)",
            command=self.clear_display
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.screen_button = ttk.Button(
            button_frame,
            text="Screen: OFF (Ctrl+Shift+S)",
            command=self.on_screen_button_click
        )
        self.screen_button.pack(side=tk.LEFT, padx=5)
        
        self.opacity_scale = ttk.Scale(
            button_frame,
            from_=0.3,
            to=1.0,
            orient=tk.HORIZONTAL,
            command=self.change_opacity,
            length=120
        )
        self.opacity_scale.set(self.opacity)
        self.opacity_scale.pack(side=tk.RIGHT, padx=5)
        
        ttk.Label(button_frame, text="Opacity:").pack(side=tk.RIGHT)
    
    def set_recording_status(self, is_recording):
        """Update the recording indicator bar"""
        self.is_recording = is_recording
        if is_recording:
            self.recording_bar.config(bg='#ff4444')
            self.recording_label.config(
                text="🔴 RECORDING",
                bg='#ff4444'
            )
            self.listen_button.config(text="⏸ Stop Listening (Ctrl+Shift+L)")
            self.update_status_text()
        else:
            self.recording_bar.config(bg='#444444')
            self.recording_label.config(
                text="⚫ IDLE",
                bg='#444444'
            )
            self.listen_button.config(text="▶ Start Listening (Ctrl+Shift+L)")
            self.update_status_text()
    
    def set_screen_reading(self, enabled):
        """Update screen reading status"""
        self.screen_reading = enabled
        button_text = f"Screen: {'ON' if enabled else 'OFF'} (Ctrl+Shift+S)"
        self.screen_button.config(text=button_text)
        self.update_status_text()
    
    def update_status_text(self):
        """Update the status label"""
        if self.is_recording:
            status = "Listening for questions..."
        else:
            status = "Ready (Ctrl+Shift+L to start)"
        
        screen_status = "ON" if self.screen_reading else "OFF"
        self.status_label.config(text=f"Status: {status} | Screen Reading: {screen_status}")
        
    def update_status(self, status_text):
        """Update status label with custom text"""
        screen_status = "ON" if self.screen_reading else "OFF"
        self.status_label.config(text=f"Status: {status_text} | Screen Reading: {screen_status}")
        
    def display_question(self, question):
        """Display the detected question"""
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(tk.END, question)
        
    def display_answer(self, answer):
        """Display the generated answer"""
        self.answer_text.delete(1.0, tk.END)
        self.answer_text.insert(tk.END, answer)
        
    def clear_display(self):
        """Clear both question and answer displays"""
        self.question_text.delete(1.0, tk.END)
        self.answer_text.delete(1.0, tk.END)
        self.update_status("Cleared")
        
    def change_opacity(self, value):
        """Change window opacity"""
        self.root.attributes('-alpha', float(value))
        
    def toggle_visibility(self):
        """Hide or show the window"""
        if self.is_visible:
            self.root.withdraw()
            self.is_visible = False
        else:
            self.root.deiconify()
            self.is_visible = True
    
    def on_screen_button_click(self):
        # Directly call the connected callback if set
        if hasattr(self, '_screen_callback') and self._screen_callback:
            self._screen_callback()
    def set_screen_callback(self, callback):
        self._screen_callback = callback
    def on_listen_button_click(self):
        # Directly call the connected callback if set
        if hasattr(self, '_listen_callback') and self._listen_callback:
            self._listen_callback()
    def set_listen_callback(self, callback):
        self._listen_callback = callback
            
    def show(self):
        """Show the window"""
        if not self.is_visible:
            self.root.deiconify()
            self.is_visible = True
            
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()
        
    def update(self):
        """Update the GUI (for thread-safe updates)"""
        self.root.update()
