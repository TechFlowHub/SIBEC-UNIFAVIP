from tkinter import Tk

from view.login_view import LoginView
from utils.window_utils import center_window

from utils.styles import BACKGROUND_COLOR

if __name__ == "__main__":
    root = Tk()

    center_window(root, 800, 600)
    root.configure(bg=BACKGROUND_COLOR)

    app = LoginView(root)
    root.mainloop()
