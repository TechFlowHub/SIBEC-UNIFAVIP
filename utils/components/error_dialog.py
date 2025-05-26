import tkinter as tk
from utils.styles import FRAME_COLOR, TEXT_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from ..window_utils import center_window

class ErrorDialog(tk.Toplevel):
    def __init__(self, master, title="Erro", message="Algo deu errado."):
        super().__init__(master)

        self.title(title)
        self.configure(bg=FRAME_COLOR)
        self.resizable(False, False)

        center_window(self, 300, 150) 
        self.grab_set()

        label = tk.Label(self, text=message, bg=FRAME_COLOR, fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE))
        label.pack(pady=20, padx=10)

        button = tk.Button(
            self,
            text="OK",
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD),
            relief="flat",
            command=self.destroy
        )
        button.pack(pady=(0, 20), ipadx=10)

        button.bind("<Enter>", lambda e: button.config(bg=BUTTON_HOVER_COLOR))
        button.bind("<Leave>", lambda e: button.config(bg=BUTTON_COLOR))
