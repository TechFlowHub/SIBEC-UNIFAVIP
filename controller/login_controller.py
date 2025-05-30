from database.models import get_user_by_email
from utils.password import check_password
from utils.components.error_dialog import ErrorDialog
from view.home_admin_view import AdminView
from view.home_secretary_view import SecretaryView
from controller.home_secretary_controller import SecretaryController
from database.connection import get_connection 

from view.home_coordinator_view import CoordinatorView

class LoginController:
    @staticmethod
    def login(email, password, master):
        user = get_user_by_email(email)
        conn = get_connection()
        secretary_controller = SecretaryController(master, conn)
        
        if user is None:
            ErrorDialog(master, title="Erro de Login", message="Email incorreto.")
            return

        if not check_password(password, user["password_hash"]):
            ErrorDialog(master, title="Erro de Login", message="Senha incorreta.")
            return
  
        if user["role"] == "admin":
            AdminView(master)
        elif user["role"] == "secretary":
            SecretaryView(master, secretary_controller)
        elif user["role"] == "coordinator":
            CoordinatorView(master)
