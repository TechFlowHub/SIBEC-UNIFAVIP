import mysql.connector
from view.home_secretary_view import SecretaryView
from view.register_view import RegisterUserView

class SecretaryController:
    def __init__(self, root, connection):
        self.root = root
        self.conn = connection
        self.cursor = self.conn.cursor()

    def show_secretary_view(self):
        SecretaryView(self.root, self)

    def show_register_user_view(self):
        RegisterUserView(self.root, self.conn)


    def insert_scholarship(self, data):
        try:
            query = """
                INSERT INTO scholarship (
                    concession_year, ies_code, ies_name, city, campus,
                    scholarship_type, education_mode, course, shift,
                    beneficiary_cpf, gender, race, birth_date, has_disability,
                    region, state, beneficiary_city
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = list(data.values())
            self.cursor.execute(query, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Erro no banco de dados: {err}")

    def update_scholarship(self, scholarship_id, data):

        query = """
            UPDATE scholarship SET
                concession_year=%s, ies_code=%s, ies_name=%s, city=%s, campus=%s, scholarship_type=%s,
                education_mode=%s, course=%s, shift=%s, beneficiary_cpf=%s, gender=%s, race=%s,
                birth_date=%s, has_disability=%s, region=%s, state=%s, beneficiary_city=%s
            WHERE id=%s
        """
        values = list(data.values())

        try:
            if isinstance(values[13], str):
                values[13] = True if values[13].strip().lower() == "sim" else False
            elif isinstance(values[13], bool):
                pass
            else:
                raise ValueError("Valor inválido para has_disability: deve ser 'Sim' ou 'Não'.")

            values.append(scholarship_id)

            self.cursor.execute(query, values)
            self.conn.commit()

            return self.cursor.rowcount > 0
        except Exception as e:
            return False

    def get_scholarship_by_id(self, scholarship_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM scholarship WHERE id = %s", (scholarship_id,))
        row = cursor.fetchone()
        if not row:
            return None

        columns = [desc[0] for desc in cursor.description]
        return dict(zip(columns, row))


    def delete_scholarship(self, scholarship_id):
        self.cursor.execute("DELETE FROM scholarship WHERE id=%s", (scholarship_id,))
        self.conn.commit()

    def get_all_scholarships(self):
        query = """
            SELECT id, concession_year, ies_code, ies_name, campus, course, beneficiary_cpf, race, gender
            FROM scholarship
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def logout(self):
        # Import LoginView here to avoid circular imports
        from view.login_view import LoginView
        
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.update_idletasks()
        self.login_view = LoginView(self.root)