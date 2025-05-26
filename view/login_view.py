import tkinter as tk
from utils.styles import FRAME_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from controller.login_controller import LoginController

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        self.frame = tk.Frame(master, bg=FRAME_COLOR, padx=50, pady=45)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label_email = tk.Label(self.frame, text="Email ( institucional do sistema )", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                    font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_email.pack(anchor="w", pady=(0,5))

        self.email_entry = tk.Entry(self.frame, font=(FONT_FAMILY, FONT_SIZE - 1), width=45)
        self.email_entry.pack(pady=(0 , 15), ipady=4)

        self.label_senha = tk.Label(self.frame, text="Senha", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                    font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_senha.pack(anchor="w", pady=(0,5))

        self.senha_entry = tk.Entry(self.frame, show="*", font=(FONT_FAMILY, FONT_SIZE - 1), width=45)
        self.senha_entry.pack(pady=(0,  15), ipady=4)

        self.btn_entrar = tk.Button(
            self.frame, 
            text="Entrar", 
            bg=BUTTON_COLOR, 
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), 
            relief="flat",
            command=self.login)
        self.btn_entrar.pack(fill="x")

        self.btn_entrar.bind("<Enter>", lambda e: self.btn_entrar.config(bg=BUTTON_HOVER_COLOR))
        self.btn_entrar.bind("<Leave>", lambda e: self.btn_entrar.config(bg=BUTTON_COLOR))

    def login(self):
        email = self.email_entry.get()
        password = self.senha_entry.get()
        LoginController.login(email, password, self.master)
