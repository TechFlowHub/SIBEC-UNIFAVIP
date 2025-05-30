import tkinter as tk
from tkinter import ttk, messagebox
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from utils.window_utils import center_window
from controller.register_controller import RegisterController 

class RegisterUserView(tk.Toplevel):
    def __init__(self, parent, conn):
        super().__init__(parent)
        self.controller = RegisterController(conn, root=self)
        self.title("Cadastrar Usuário")
        self.configure(bg=FRAME_COLOR)
        self.resizable(False, False)

        center_window(self, width=500, height=300)

        # Título da janela
        title = tk.Label(self, text="Cadastro de Usuário", bg=FRAME_COLOR, fg=TEXT_COLOR,
                         font=(FONT_FAMILY, FONT_SIZE + 4, FONT_BOLD))
        title.pack(pady=(20, 10))

        # Frame com borda e padding
        form_frame = tk.Frame(self, bg="#ecf0f1", bd=2, relief="groove", padx=20, pady=20)
        form_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Nome de usuário
        tk.Label(form_frame, text="Usuário (antes do @1775.com):", bg="#ecf0f1", fg="#2c3e50",
                 font=(FONT_FAMILY, FONT_SIZE)).grid(row=0, column=0, sticky="w", pady=5)
        self.username_entry = tk.Entry(form_frame, font=(FONT_FAMILY, FONT_SIZE), bd=2, relief="groove")
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)

        # Senha
        tk.Label(form_frame, text="Senha:", bg="#ecf0f1", fg="#2c3e50",
                 font=(FONT_FAMILY, FONT_SIZE)).grid(row=1, column=0, sticky="w", pady=5)
        self.password_entry = tk.Entry(form_frame, font=(FONT_FAMILY, FONT_SIZE), bd=2, relief="groove")
        self.password_entry.insert(0, "1234")
        self.password_entry.config(state="disabled")
        self.password_entry.grid(row=1, column=1, pady=5, padx=5)

        # Função (Role)
        tk.Label(form_frame, text="Função:", bg="#ecf0f1", fg="#2c3e50",
                 font=(FONT_FAMILY, FONT_SIZE)).grid(row=2, column=0, sticky="w", pady=5)
        self.role_combobox = ttk.Combobox(form_frame, font=(FONT_FAMILY, FONT_SIZE),
                                          values=["Coordenador", "Secretário"], state="readonly")
        self.role_combobox.grid(row=2, column=1, pady=5, padx=5)
        self.role_combobox.set("Selecione")

        # Botão de cadastro
        submit_btn = tk.Button(self, text="Cadastrar", bg="#27ae60", fg="white",
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), padx=20, pady=10,
                               activebackground="#2ecc71", activeforeground="white",
                               command=self.register_user)
        submit_btn.pack(pady=15)

    def register_user(self):
        username = self.username_entry.get().strip()
        email = f"{username}@1775.com"
        password = "1234"
        role_pt = self.role_combobox.get()

        role_map = {
            "Coordenador": "coordinator",
            "Secretário": "secretary"
        }
        role = role_map.get(role_pt)

        if not username or role_pt == "Selecione":
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        self.controller.register_user_controller(email=email, password=password, role=role)