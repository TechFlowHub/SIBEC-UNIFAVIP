from tkinter import Tk

from view.login_view import LoginView
from view.register_view import RegisterView
from utils.window_utils import center_window
from view.home_secretary_view import SecretaryView

from utils.styles import BACKGROUND_COLOR

if __name__ == "__main__":
    root = Tk()

    center_window(root, 1280, 720)

    root.configure(bg=BACKGROUND_COLOR)

    # app = RegisterView(root)
    # app = LoginView(root)

    app = SecretaryView(root)
    
    root.mainloop()
