from utils.password import hash_password
from tkinter import messagebox

class RegisterController:
    def __init__(self, conn, root=None):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.root = root  # só se quiser usar para messagebox ou views

    def register_user_controller(self, email, password, role):
        try:
            password_hash = hash_password(password)
            query = "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (email, password_hash, role))
            self.conn.commit()

            if self.root:
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            # aqui pode chamar outra view/controller se quiser
        except Exception as e:
            if self.root:
                messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
            else:
                raise
