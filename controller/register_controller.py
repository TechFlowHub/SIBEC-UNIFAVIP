from database.models import create_user
from utils.password import hash_password
from utils.components.error_dialog import ErrorDialog
from view.home_admin_view import AdminView
from view.home_secretary_view import SecretaryView
from view.home_coordinator_view import CoordinatorView

class RegisterController:
    @staticmethod
    def register(name, email, password, role, master):
        if not name or not email or not password or not role:
            ErrorDialog(master, title="Erro de Registro", message="Todos os campos são obrigatórios.")
            return

        hashed_password = hash_password(password)
        try:
            create_user(name, email, hashed_password, role)

            if role == "secretary":
                SecretaryView(master)
            elif role == "admin":
                AdminView(master)
            elif role == "coordinator":
                CoordinatorView(master)
            
        except Exception as e:
            ErrorDialog(master, title="Erro de Registro", message=str(e))