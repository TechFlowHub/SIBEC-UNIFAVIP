import tkinter as tk
from utils.styles import FRAME_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from controller.register_controller import RegisterController

class RegisterView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg=FRAME_COLOR)
        self.frame.pack(padx=10, pady=10)

        self.title_label = tk.Label(self.frame, text="Registro de Usuário", bg=FRAME_COLOR, fg=TEXT_COLOR,
                                     font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD))
        self.title_label.pack()

        self.name_label = tk.Label(self.frame, text="Nome:", bg=FRAME_COLOR, fg=TEXT_COLOR)
        self.name_label.pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        self.email_label = tk.Label(self.frame, text="Email:", bg=FRAME_COLOR, fg=TEXT_COLOR)
        self.email_label.pack()
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack()

        self.password_label = tk.Label(self.frame, text="Senha:", bg=FRAME_COLOR, fg=TEXT_COLOR)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.role_label = tk.Label(self.frame, text="Cargo:", bg=FRAME_COLOR, fg=TEXT_COLOR)
        self.role_label.pack()
        self.role_var = tk.StringVar(value="secretary")
        self.role_menu = tk.OptionMenu(self.frame, self.role_var, "admin", "secretary", "coordinator")
        self.role_menu.pack()

        self.register_button = tk.Button(self.frame, text="Registrar", bg=BUTTON_COLOR, fg=TEXT_COLOR,
                                          command=self.register_user)
        self.register_button.pack(pady=10)

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        RegisterController.register(name, email, password, role, self.master)

    def show_success_message(self, message):
        tk.messagebox.showinfo("Sucesso", message)
