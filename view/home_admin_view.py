import tkinter as tk
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD

class AdminView:
    def __init__(self, parent):
        parent.title("Bem-vindo à Administração")

        for widget in parent.winfo_children():
            widget.destroy()

        parent.configure(bg=FRAME_COLOR)

        label = tk.Label(
            parent,
            text="Bem-vindo à tela de Administração!",
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD)
        )
        label.pack(expand=True)
