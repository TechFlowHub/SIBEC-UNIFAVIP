import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD

# Set the TEXT_COLOR to white for all charts
CHART_TEXT_COLOR = 'white'

class CoordinatorView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        parent.title("Painel Coordenação - SIBEC")
        parent.configure(bg=FRAME_COLOR)

        for widget in parent.winfo_children():
            widget.destroy()

        # --- Filter Frame ---
        filter_frame = tk.Frame(parent, bg=FRAME_COLOR)
        filter_frame.pack(fill="x", padx=10, pady=10)
        
        # Row 1 of filters
        filter_row1 = tk.Frame(filter_frame, bg=FRAME_COLOR)
        filter_row1.pack(fill="x", pady=(0, 5))

        # Filter by Year
        tk.Label(filter_row1, text="Ano:", bg=FRAME_COLOR, fg=CHART_TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE-1)).pack(side="left", padx=(5,2))
        self.year_filter_var = tk.StringVar()
        year_options = ["Todos"] + self.controller.get_distinct_values('concession_year')
        year_filter_menu = ttk.Combobox(filter_row1, textvariable=self.year_filter_var, values=year_options, state="readonly", width=8)
        self.year_filter_var.set("Todos")
        year_filter_menu.pack(side="left", padx=5)

        # Filter by Scholarship Type
        tk.Label(filter_row1, text="Tipo de Bolsa:", bg=FRAME_COLOR, fg=CHART_TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE-1)).pack(side="left", padx=(10,2))
        self.type_filter_var = tk.StringVar()
        type_options = ["Todos"] + self.controller.get_distinct_values('scholarship_type') #
        type_filter_menu = ttk.Combobox(filter_row1, textvariable=self.type_filter_var, values=type_options, state="readonly", width=12)
        self.type_filter_var.set("Todos")
        type_filter_menu.pack(side="left", padx=5)

        # Filter by State (UF)
        tk.Label(filter_row1, text="UF:", bg=FRAME_COLOR, fg=CHART_TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE-1)).pack(side="left", padx=(10,2))
        self.state_filter_var = tk.StringVar()
        state_options = ["Todos"] + self.controller.get_distinct_values('state')
        state_filter_menu = ttk.Combobox(filter_row1, textvariable=self.state_filter_var, values=state_options, state="readonly", width=5)
        self.state_filter_var.set("Todos")
        state_filter_menu.pack(side="left", padx=5)

        # Row 2 of filters
        filter_row2 = tk.Frame(filter_frame, bg=FRAME_COLOR)
        filter_row2.pack(fill="x", pady=(5, 5))
        
        # Filter by Education Mode
        tk.Label(filter_row2, text="Modalidade:", bg=FRAME_COLOR, fg=CHART_TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE-1)).pack(side="left", padx=(5,2))
        self.mode_filter_var = tk.StringVar()
        mode_options = ["Todos"] + self.controller.get_distinct_values('education_mode')
        mode_filter_menu = ttk.Combobox(filter_row2, textvariable=self.mode_filter_var, values=mode_options, state="readonly", width=12)
        self.mode_filter_var.set("Todos")
        mode_filter_menu.pack(side="left", padx=5)

        # Filter by Shift
        tk.Label(filter_row2, text="Turno:", bg=FRAME_COLOR, fg=CHART_TEXT_COLOR, font=(FONT_FAMILY, FONT_SIZE-1)).pack(side="left", padx=(10,2))
        self.shift_filter_var = tk.StringVar()
        shift_options = ["Todos"] + self.controller.get_distinct_values('shift')
        shift_filter_menu = ttk.Combobox(filter_row2, textvariable=self.shift_filter_var, values=shift_options, state="readonly", width=12)
        self.shift_filter_var.set("Todos")
        shift_filter_menu.pack(side="left", padx=5)

        # Refresh Button
        refresh_btn = tk.Button(filter_row2, text="🔍 Aplicar Filtros", command=self.refresh_charts, bg="#007BFF", fg="white", font=(FONT_FAMILY, FONT_SIZE-2))
        refresh_btn.pack(side="left", padx=20)
        
        # --- Main Content Frame ---
        self.main_frame = tk.Frame(parent, bg=FRAME_COLOR)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # --- Tabs ---
        self.tab_control = ttk.Notebook(self.main_frame)
        self.tab1 = tk.Frame(self.tab_control, bg=FRAME_COLOR) #
        self.tab2 = tk.Frame(self.tab_control, bg=FRAME_COLOR) #
        self.tab3 = tk.Frame(self.tab_control, bg=FRAME_COLOR) #
        self.tab_control.add(self.tab1, text='Tipos de Bolsa') #
        self.tab_control.add(self.tab2, text='Cursos') #
        self.tab_control.add(self.tab3, text='Demografia') #
        self.tab_control.pack(expand=1, fill="both") #
        
        # --- Initialize Chart Canvases ---
        self.fig1, self.ax1 = plt.subplots(facecolor=FRAME_COLOR)
        self.canvas1 = FigureCanvasTkAgg(self.fig1, self.tab1)
        self.canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.fig2, self.ax2 = plt.subplots(facecolor=FRAME_COLOR)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, self.tab2)
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.fig3, (self.ax3_gender, self.ax3_race) = plt.subplots(1, 2, figsize=(10, 5), facecolor=FRAME_COLOR)
        self.canvas3 = FigureCanvasTkAgg(self.fig3, self.tab3)
        self.canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.refresh_charts()

    def get_selected_filters(self):
        """Gathers all active filter values from the UI."""
        filters = {}
        if self.year_filter_var.get() != "Todos":
            filters['concession_year'] = self.year_filter_var.get()
        if self.type_filter_var.get() != "Todos":
            filters['scholarship_type'] = self.type_filter_var.get()
        if self.state_filter_var.get() != "Todos":
            filters['state'] = self.state_filter_var.get()
        if self.mode_filter_var.get() != "Todos":
            filters['education_mode'] = self.mode_filter_var.get()
        if self.shift_filter_var.get() != "Todos":
            filters['shift'] = self.shift_filter_var.get()
        return filters

    def refresh_charts(self):
        """Refreshes all charts with data based on the selected filters."""
        filters = self.get_selected_filters()
        
        self.update_scholarship_type_chart(filters)
        self.update_course_chart(filters)
        self.update_demographic_charts(filters)

    def update_scholarship_type_chart(self, filters):
        data = self.controller.get_aggregated_data('scholarship_type', filters) #
        self.ax1.clear() 
        
        if not data.empty:
            wedges, texts, autotexts = self.ax1.pie(
                data['count'], 
                labels=data['scholarship_type'], 
                autopct='%1.1f%%', 
                startangle=90
            )
            for text in texts:
                text.set_color(CHART_TEXT_COLOR)
            for autotext in autotexts:
                autotext.set_color('black') # Black text on wedges is often more readable
            self.ax1.set_title('Distribuição por Tipo de Bolsa', color=CHART_TEXT_COLOR) #
        else:
            self.ax1.text(0.5, 0.5, "Sem dados para exibir", ha='center', va='center', color=CHART_TEXT_COLOR)
        
        self.ax1.axis('equal')
        self.canvas1.draw()

    def update_course_chart(self, filters):
        data = self.controller.get_aggregated_data('course', filters, limit=15) #
        self.ax2.clear()

        if not data.empty:
            bars = self.ax2.barh(data['course'], data['count'], color='#3498db')
            self.ax2.set_title('Top 15 Cursos', color=CHART_TEXT_COLOR)
            self.ax2.set_xlabel('Número de Bolsistas', color=CHART_TEXT_COLOR)
            self.ax2.tick_params(axis='x', colors=CHART_TEXT_COLOR)
            self.ax2.tick_params(axis='y', colors=CHART_TEXT_COLOR)
            self.ax2.invert_yaxis()
        else:
            self.ax2.text(0.5, 0.5, "Sem dados para exibir", ha='center', va='center', color=CHART_TEXT_COLOR)

        self.fig2.tight_layout()
        self.canvas2.draw()

    def update_demographic_charts(self, filters):
        # Gender Data
        gender_data = self.controller.get_aggregated_data('gender', filters) #
        self.ax3_gender.clear()
        if not gender_data.empty:
            wedges, texts, autotexts = self.ax3_gender.pie(
                gender_data['count'], 
                labels=gender_data['gender'], 
                autopct='%1.1f%%', 
                startangle=90
            )
            for text in texts:
                text.set_color(CHART_TEXT_COLOR)
            for autotext in autotexts:
                autotext.set_color('black')
            self.ax3_gender.set_title('Distribuição por Gênero', color=CHART_TEXT_COLOR) #
        else:
            self.ax3_gender.text(0.5, 0.5, "Sem dados", ha='center', va='center', color=CHART_TEXT_COLOR)

        # Race Data - Bar Chart
        race_data = self.controller.get_aggregated_data('race', filters) #
        self.ax3_race.clear()
        if not race_data.empty:
            self.ax3_race.bar(race_data['race'], race_data['count'], color='#5cb85c')
            self.ax3_race.set_title('Distribuição por Raça/Etnia', color=CHART_TEXT_COLOR) #
            self.ax3_race.tick_params(axis='x', labelrotation=45, colors=CHART_TEXT_COLOR)
            self.ax3_race.tick_params(axis='y', colors=CHART_TEXT_COLOR)
            self.ax3_race.set_ylabel('Número de Bolsistas', color=CHART_TEXT_COLOR)
        else:
            self.ax3_race.text(0.5, 0.5, "Sem dados", ha='center', va='center', color=CHART_TEXT_COLOR)

        self.fig3.tight_layout()
        self.canvas3.draw()