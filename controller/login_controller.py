from database.models import get_user_by_email
from utils.password import check_password
from tkinter import messagebox
from utils.components.error_dialog import ErrorDialog

class LoginController:
    @staticmethod
    def login(email, password, master):
        user = get_user_by_email(email)
        if user is None:
            ErrorDialog(master, title="Erro de Login", message="Email incorreto.")
            return

        if not check_password(password, user["password_hash"]):
            ErrorDialog(master, title="Erro de Login", message="Senha incorreta.")
            return

        # Login bem-sucedido
        messagebox.showinfo("Sucesso", f"Bem-vindo, {user['role'].capitalize()}!")
        # Aqui você pode redirecionar para a próxima tela com base no tipo de usuário
