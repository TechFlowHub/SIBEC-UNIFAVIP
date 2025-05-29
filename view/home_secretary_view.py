import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD
from tkcalendar import DateEntry
import re
from datetime import datetime

from utils.components.error_dialog import ErrorDialog

class SecretaryView:
    def __init__(self, parent, controller):
        self.root = parent
        self.controller = controller

        parent.title("Painel do Secretário")
        parent.configure(bg=FRAME_COLOR)

        for widget in parent.winfo_children():
            widget.destroy()

        paned = tk.PanedWindow(parent, orient=tk.VERTICAL, sashrelief="raised", bg=FRAME_COLOR)
        paned.pack(fill=tk.BOTH, expand=1)

        # Formulário
        form_container = tk.Frame(paned, bg=FRAME_COLOR, pady=20, padx=20)
        form_container.pack_propagate(False)
        form_container.configure(height=350)  # Ajustado para melhor centramento

        # Wrapper centralizador
        form_wrapper = tk.Frame(form_container, bg=FRAME_COLOR)
        form_wrapper.place(relx=0.5, rely=0.0, anchor="n")# Alinhado no topo

        form_frame = tk.LabelFrame(form_wrapper, text="Cadastro de Bolsa", bg=FRAME_COLOR, fg=TEXT_COLOR,
                                padx=10, pady=10, font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))
        form_frame.pack()


        labels = [
            "Ano da concessão", "Código da IES", "Nome da IES", "Município",
            "Campus", "Tipo de bolsa", "Modalidade de ensino", "Curso",
            "Turno", "CPF do beneficiário", "Sexo", "Raça",
            "Data de nascimento", "Pessoa com deficiência", "Região", "UF", "Município do beneficiário"
        ]

        self.entries = {}
        num_columns = 5
        for i, label in enumerate(labels):
            row = i // num_columns
            col = i % num_columns

            field_frame = tk.Frame(form_frame, bg=FRAME_COLOR)
            field_frame.grid(row=row, column=col, padx=10, pady=10, sticky="w")

            tk.Label(field_frame, text=label + " *", bg=FRAME_COLOR, fg=TEXT_COLOR,
                     anchor="w", font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD)).pack(anchor="w")

            if label == "Pessoa com deficiência":
                var = tk.StringVar()
                entry = ttk.Combobox(field_frame, textvariable=var, values=["Sim", "Não"], state="readonly", width=21)
                entry.set("Não")
                entry.pack()
            elif label == "Data de nascimento":
                entry = DateEntry(field_frame, date_pattern="yyyy-mm-dd", width=18,
                                background='darkblue', foreground='white', borderwidth=2,
                                font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD))
                entry.pack()
            else:
                entry = tk.Entry(field_frame, width=20, relief="flat", bg=TEXT_COLOR, 
                                 fg="#000000", font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD))
                entry.pack()

            self.entries[label] = entry

        # Botões
        button_frame = tk.Frame(form_frame, bg=FRAME_COLOR)
        button_frame.grid(row=10, column=0, columnspan=num_columns, pady=20)

        insert_btn = tk.Button(button_frame, text="Inserir", bg="#3fb68b", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.insert_data)
        insert_btn.grid(row=0, column=0, padx=10)

        update_btn = tk.Button(button_frame, text="Atualizar", bg="#ffa500", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.update_data)
        update_btn.grid(row=0, column=1, padx=10)

        delete_btn = tk.Button(button_frame, text="Deletar", bg="#d9534f", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.delete_data)
        delete_btn.grid(row=0, column=2, padx=10)

        clear_btn = tk.Button(button_frame, text="Limpar", bg="#6c757d", fg="white", width=12,
                      font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.clear_form)
        clear_btn.grid(row=0, column=3, padx=10)

        paned.add(form_container, pady=20)
        

       # Tabela
        table_frame = tk.Frame(paned, bg="white", padx=38, pady=20)
        self.tree = ttk.Treeview(table_frame, columns=[
            "Ano da Concessão", "Código da IES", "Nome da IES", "Tipo de Bolsa", "Curso", "CPF do Beneficiário", "Raça", "Sexo"
        ], show="headings", height=25)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.replace("_", " ").capitalize())
            self.tree.column(col, width=150, anchor="center", stretch=False)


        scroll_x = tk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        scroll_y = tk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<Double-1>", self.on_row_double_click)

        paned.add(table_frame)

        self.refresh_table()

    def clear_form(self):
        for label, widget in self.entries.items():
            if isinstance(widget, ttk.Combobox):
                widget.set("Não")
            elif isinstance(widget, DateEntry):
                widget.set_date(datetime.today())
            else:
                widget.delete(0, tk.END)


    def get_form_data(self):
        data = {}
        for label, widget in self.entries.items():
            value = widget.get()
            if label == "Pessoa com deficiência":
                data["has_disability"] = True if value == "Sim" else False
            else:
                key = self.normalize_label(label)
                data[key] = value
        return data

    def normalize_label(self, label):
        mapping = {
            "Ano da concessão": "concession_year",
            "Código da IES": "ies_code",
            "Nome da IES": "ies_name",
            "Município": "city",
            "Campus": "campus",
            "Tipo de bolsa": "scholarship_type",
            "Modalidade de ensino": "education_mode",
            "Curso": "course",
            "Turno": "shift",
            "CPF do beneficiário": "beneficiary_cpf",
            "Sexo": "gender",
            "Raça": "race",
            "Data de nascimento": "birth_date",
            "Região": "region",
            "UF": "state",
            "Município do beneficiário": "beneficiary_city"
        }
        return mapping.get(label, label.lower().replace(" ", "_"))

    def validate_data(self, data):
        required_fields = ["concession_year", "ies_code", "ies_name", "city", "campus",
                        "scholarship_type", "education_mode", "course", "shift",
                        "beneficiary_cpf", "gender", "race", "birth_date",
                        "region", "state", "beneficiary_city"]

        for field in required_fields:
            if not data.get(field):
                raise ValueError(f"O campo '{field}' é obrigatório.")

        # Ano como número
        if not data["concession_year"].isdigit():
            raise ValueError("O ano da concessão deve ser numérico.")

        # CPF simples
        if not re.match(r"^\d{11}$", data["beneficiary_cpf"]):
            raise ValueError("CPF inválido. Use apenas números (11 dígitos).")

        # Data de nascimento válida
        try:
            datetime.strptime(data["birth_date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato AAAA-MM-DD.")

        # UF com 2 letras
        if len(data["state"]) != 2 or not data["state"].isalpha():
            raise ValueError("UF deve conter apenas 2 letras.")


    def insert_data(self):
        try:
            data = self.get_form_data()
            self.validate_data(data)
            self.controller.insert_scholarship(data)
            self.refresh_table()
            self.clear_form()
            messagebox.showinfo("Sucesso", "Bolsa inserida com sucesso!")
        except ValueError as ve:
            ErrorDialog(self.root, message=str(ve))
        except Exception as e:
            ErrorDialog(self.root, message="Erro ao inserir: " + str(e))


    def on_row_double_click(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        scholarship_id = selected[0]
        try:
            full_data = self.controller.get_scholarship_by_id(scholarship_id)
            if not full_data:
                raise Exception("Registro não encontrado.")

            self.fill_form_with_data(full_data)
        except Exception as e:
            ErrorDialog(self.root, message="Erro ao carregar dados: " + str(e))


    def fill_form_with_data(self, data):
    # data é um dicionário ou tupla com todas as colunas do banco
        db_to_form = {
            "concession_year": "Ano da concessão",
            "ies_code": "Código da IES",
            "ies_name": "Nome da IES",
            "city": "Município",
            "campus": "Campus",
            "scholarship_type": "Tipo de bolsa",
            "education_mode": "Modalidade de ensino",
            "course": "Curso",
            "shift": "Turno",
            "beneficiary_cpf": "CPF do beneficiário",
            "gender": "Sexo",
            "race": "Raça",
            "birth_date": "Data de nascimento",
            "has_disability": "Pessoa com deficiência",
            "region": "Região",
            "state": "UF",
            "beneficiary_city": "Município do beneficiário"
        }

        for db_field, form_label in db_to_form.items():
            value = data.get(db_field) if isinstance(data, dict) else getattr(data, db_field, "")
            widget = self.entries[form_label]

            if isinstance(widget, ttk.Combobox):
                widget.set("Sim" if value else "Não")
            elif isinstance(widget, DateEntry):
                try:
                    widget.set_date(datetime.strptime(value, "%Y-%m-%d"))
                except:
                    pass
            else:
                widget.delete(0, tk.END)
                widget.insert(0, str(value))


    def update_data(self):
        selected = self.tree.selection()
        if not selected:
            ErrorDialog(self.root, message="Selecione um registro para atualizar.")
            return

        try:
            scholarship_id = int(selected[0]) 

            data = self.get_form_data()
            self.validate_data(data)

            sucesso = self.controller.update_scholarship(scholarship_id, data)
            if sucesso:
                self.refresh_table()
                self.clear_form()
                messagebox.showinfo("Sucesso", "Bolsa atualizada com sucesso!")
            else:
                ErrorDialog(self.root, message="Erro ao atualizar a bolsa.")
        except ValueError as ve:
            ErrorDialog(self.root, message=str(ve))
        except Exception as e:
            ErrorDialog(self.root, message="Erro ao atualizar: " + str(e))

    def delete_data(self):
        selected = self.tree.selection()
        if not selected:
            ErrorDialog(self.root, message="Selecione um registro para deletar.")
            return

        confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar esta bolsa?")
        if not confirm:
            return

        scholarship_id = selected[0]
        self.controller.delete_scholarship(scholarship_id)
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Sucesso", "Bolsa deletada com sucesso!")


    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = self.controller.get_all_scholarships()
        for row in rows:
            scholarship_id = row[0]    

            visible_values = row[1:]     
            self.tree.insert("", tk.END, iid=scholarship_id, values=visible_values)


    def clear_form(self):
        for label, widget in self.entries.items():
            if isinstance(widget, ttk.Combobox):
                widget.set("Não")
            elif isinstance(widget, DateEntry):
                widget.set_date(datetime.today())
            else:
                widget.delete(0, tk.END)

        # Remove qualquer seleção na tabela
        selected = self.tree.selection()
        for item in selected:
            self.tree.selection_remove(item)