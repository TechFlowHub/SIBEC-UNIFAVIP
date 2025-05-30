import mysql.connector
from tkinter import Tk

from config import Config
from database.connection import get_connection  # Certifique-se de que get_connection está em um arquivo chamado db.py
from view.login_view import LoginView
from view.home_secretary_view import SecretaryView
from controller.home_secretary_controller import SecretaryController
from utils.window_utils import center_window
from utils.styles import BACKGROUND_COLOR

if __name__ == "__main__":
    # Conecta ao banco
    conn = get_connection()

    # Cria a janela principal
    root = Tk()
    root.resizable(False, False)
    center_window(root, 1280, 720)
    root.configure(bg=BACKGROUND_COLOR)

    # Instancia o controller com a conexão
    secretary_controller = SecretaryController(root, conn)

    # Exibe a tela desejada
    app = LoginView(root)
    # app = SecretaryView(root, secretary_controller)

    # Inicia o loop da interface
    root.mainloop()
