import tkinter as tk
from tkinter import ttk
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD

class SecretaryView:
    def __init__(self, parent):
        parent.title("Painel do Secretário")
        parent.configure(bg=FRAME_COLOR)

        for widget in parent.winfo_children():
            widget.destroy()

        # Estrutura do layout principal com PanedWindow
        paned = tk.PanedWindow(parent, orient=tk.VERTICAL, sashrelief="raised", bg=FRAME_COLOR)
        paned.pack(fill=tk.BOTH, expand=1)

        # Frame do formulário (esquerda)
        form_container = tk.Frame(paned, bg=FRAME_COLOR, pady=20, padx=20)  
        form_frame = tk.LabelFrame(form_container, text="Cadastro de Bolsa", bg=FRAME_COLOR, fg=TEXT_COLOR,
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
                     anchor="w", font=(FONT_FAMILY, FONT_SIZE - 1, FONT_BOLD))\
                .pack(anchor="w")

            entry = tk.Entry(field_frame, width=20, relief="flat", bg=TEXT_COLOR,
                             fg=TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD))
            entry.pack()

            self.entries[label] = entry


        # Botões
        button_frame = tk.Frame(form_frame, bg=FRAME_COLOR)
        button_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)

        insert_btn = tk.Button(button_frame, text="Inserir", bg="#3fb68b", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.insert_data)
        insert_btn.grid(row=0, column=0, padx=10)

        update_btn = tk.Button(button_frame, text="Atualizar", bg="#ffa500", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.update_data)
        update_btn.grid(row=0, column=1, padx=10)

        delete_btn = tk.Button(button_frame, text="Deletar", bg="#d9534f", fg="white", width=12,
                               font=(FONT_FAMILY, FONT_SIZE, FONT_BOLD), command=self.delete_data)
        delete_btn.grid(row=0, column=2, padx=10)

        paned.add(form_container)


        # Frame da tabela (direita)
        table_frame = tk.Frame(paned, bg="white", padx=5, pady=5)
        self.tree = ttk.Treeview(table_frame, columns=[
            "ano_concessao", "codigo_emec", "nome_ies", "municipio", "campus", "tipo_bolsa",
            "modalidade_ensino", "curso", "turno", "cpf_beneficiario", "sexo", "raca",
            "data_nascimento", "pessoa_com_deficiencia", "regiao", "uf", "municipio_beneficiario"
        ], show="headings", height=25)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.replace("_", " ").capitalize())
            self.tree.column(col, width=130, anchor="center", stretch=False)

        scroll_x = tk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        scroll_y = tk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        paned.add(table_frame)

    # Métodos de ação dos botões (placeholders)
    def insert_data(self):
        print("Inserir clicado")

    def update_data(self):
        print("Atualizar clicado")

    def delete_data(self):
        print("Deletar clicado")
