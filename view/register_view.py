import tkinter as tk
from utils.styles import FRAME_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from controller.register_controller import RegisterController

class RegisterView:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de Usuário")
        
        self.frame = tk.Frame(master, bg=FRAME_COLOR, padx=50, pady=45)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.label_name = tk.Label(self.frame, text="Nome Completo", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                    font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_name.pack(anchor="w", pady=(0,5))
        
        self.name_entry = tk.Entry(self.frame, font=(FONT_FAMILY, FONT_SIZE - 1), width=45)
        self.name_entry.pack(pady=(0, 15), ipady=4)
        
        self.label_email = tk.Label(self.frame, text="Email ( institucional do sistema )", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                    font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_email.pack(anchor="w", pady=(0,5))
        
        self.email_entry = tk.Entry(self.frame, font=(FONT_FAMILY, FONT_SIZE - 1), width=45)
        self.email_entry.pack(pady=(0, 15), ipady=4)
        
        self.label_password = tk.Label(self.frame, text="Senha", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                        font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_password.pack(anchor="w", pady=(0,5))
        
        self.password_entry = tk.Entry(self.frame, show="*", font=(FONT_FAMILY, FONT_SIZE - 1), width=45)
        self.password_entry.pack(pady=(0, 15), ipady=4)
        
        self.label_role = tk.Label(self.frame, text="Função", fg=TEXT_COLOR, bg=FRAME_COLOR,
                                    font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        self.label_role.pack(anchor="w", pady=(0,5))
        
        self.role_var = tk.StringVar(value="Selecione uma função")
        self.role_options = ["secretary", "coordinator", "admin"]
        self.role_menu = tk.OptionMenu(self.frame, self.role_var, *self.role_options)
        
        self.role_menu.config(bg=FRAME_COLOR, fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE - 1))
        self.role_menu.pack(pady=(0, 15), ipady=4)
        
        self.btn_register = tk.Button(
            self.frame, 
            text="Registrar", 
            bg=BUTTON_COLOR, 
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), 
            relief="flat",
            command=self.register_user)
        self.btn_register.pack(fill="x")
        
        self.btn_register = tk.Button(
            self.frame, 
            text="Limpar Campos", 
            bg="#7f8c8d",
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), 
            relief="flat",
            command=self.clear_fields)
        self.btn_register.pack(fill="x", pady=(10, 0))
        
        self.btn_register.bind("<Enter>", lambda e: self.btn_register.config(bg=BUTTON_HOVER_COLOR))
        self.btn_register.bind("<Leave>", lambda e: self.btn_register.config(bg=BUTTON_COLOR))
        
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.role_var.set("secretary")

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        RegisterController.register(name, email, password, role, self.master)

    def show_success_message(self, message):
        tk.messagebox.showinfo("Sucesso", message)
