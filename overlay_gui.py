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
        self.window_height = Config.WINDOW_HEIGHT
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
        
        self._create_widgets()
        self.is_visible = True
        
    def _create_widgets(self):
        """Create UI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title label
        title_label = ttk.Label(
            main_frame,
            text="InterGuide - Interview Assistant",
            font=('Arial', 12, 'bold')
        )
        title_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # Status label
        self.status_label = ttk.Label(
            main_frame,
            text="Status: Ready (Ctrl+Shift+L to start)",
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
        
        # Buttons
        self.clear_button = ttk.Button(
            button_frame,
            text="Clear (Ctrl+Shift+C)",
            command=self.clear_display
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.hide_button = ttk.Button(
            button_frame,
            text="Hide (Ctrl+Shift+H)",
            command=self.toggle_visibility
        )
        self.hide_button.pack(side=tk.LEFT, padx=5)
        
        self.opacity_scale = ttk.Scale(
            button_frame,
            from_=0.3,
            to=1.0,
            orient=tk.HORIZONTAL,
            command=self.change_opacity,
            length=150
        )
        self.opacity_scale.set(self.opacity)
        self.opacity_scale.pack(side=tk.RIGHT, padx=5)
        
        ttk.Label(button_frame, text="Opacity:").pack(side=tk.RIGHT)
        
    def update_status(self, status_text):
        """Update status label"""
        self.status_label.config(text=f"Status: {status_text}")
        
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
