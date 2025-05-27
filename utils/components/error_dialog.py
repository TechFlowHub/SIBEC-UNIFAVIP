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

        container = tk.Frame(self, bg=FRAME_COLOR)
        container.pack(expand=True)

        label = tk.Label(container, text=message, bg=FRAME_COLOR, fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD))
        label.pack(pady=(0, 15), padx=10)

        button = tk.Button(
            container,
            text="OK",
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD),
            relief="flat",
            command=self.destroy
        )
        button.pack(ipadx=10)

        button.bind("<Enter>", lambda e: button.config(bg=BUTTON_HOVER_COLOR))
        button.bind("<Leave>", lambda e: button.config(bg=BUTTON_COLOR))
