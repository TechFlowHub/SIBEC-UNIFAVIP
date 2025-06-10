import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from utils.styles import FRAME_COLOR, TEXT_COLOR, FONT_FAMILY, FONT_SIZE, FONT_BOLD

class CoordinatorView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        parent.title("Painel Coordenação - SIBEC")

        # Clear existing widgets
        for widget in parent.winfo_children():
            widget.destroy()

        parent.configure(bg=FRAME_COLOR)

        # Create main container
        self.main_frame = tk.Frame(parent, bg=FRAME_COLOR)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Header
        header = tk.Label(
            self.main_frame,
            text="Painel Coordenação - Análise de Bolsas",
            bg=FRAME_COLOR,
            fg=TEXT_COLOR,
            font=(FONT_FAMILY, FONT_SIZE + 4, FONT_BOLD)
        )
        header.pack(pady=(0, 20))

        # Create tabs for different visualizations
        self.tab_control = ttk.Notebook(self.main_frame)
        
        # Tab 1: Distribution by scholarship type
        self.tab1 = tk.Frame(self.tab_control, bg=FRAME_COLOR)
        self.tab_control.add(self.tab1, text='Tipos de Bolsa')
        
        # Tab 2: Distribution by course 
        self.tab2 = tk.Frame(self.tab_control, bg=FRAME_COLOR)
        self.tab_control.add(self.tab2, text='Cursos')
        
        # Tab 3: Distribution by gender and race
        self.tab3 = tk.Frame(self.tab_control, bg=FRAME_COLOR)
        self.tab_control.add(self.tab3, text='Demografia')
        
        self.tab_control.pack(expand=1, fill="both")
        
        # Create charts
        self.create_scholarship_type_chart()
        self.create_course_chart()
        self.create_demographic_charts()
        
        # Add refresh button
        refresh_btn = tk.Button(
            self.main_frame, 
            text="Atualizar Dados", 
            command=self.refresh_charts,
            bg="#4CAF50",
            fg="white",
            font=(FONT_FAMILY, FONT_SIZE - 2),
            padx=10,
            pady=5
        )
        refresh_btn.pack(pady=10)

    def create_scholarship_type_chart(self):
        # Get data from controller
        data = self.controller.get_scholarship_by_type()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor(FRAME_COLOR)
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            data['count'], 
            labels=data['scholarship_type'],
            autopct='%1.1f%%',
            startangle=90,
            shadow=True,
        )
        
        # Style the chart
        for text in texts:
            text.set_color(TEXT_COLOR)
        for autotext in autotexts:
            autotext.set_color('white')
            
        ax.set_title('Distribuição por Tipo de Bolsa', color=TEXT_COLOR, fontsize=14)
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.tab1)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_course_chart(self):
        # Get data from controller
        data = self.controller.get_scholarship_by_course()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 7))
        fig.patch.set_facecolor(FRAME_COLOR)
        
        # Create horizontal bar chart (for better text readability with many courses)
        bars = ax.barh(data['course'], data['count'], color='#3498db')
        
        # Add count labels
        for bar in bars:
            width = bar.get_width()
            ax.text(
                width + 0.5, 
                bar.get_y() + bar.get_height()/2, 
                f'{width}',
                ha='left', va='center', color=TEXT_COLOR
            )
        
        # Style the chart
        ax.set_title('Distribuição de Bolsas por Curso', color=TEXT_COLOR, fontsize=14)
        ax.set_xlabel('Número de Bolsistas', color=TEXT_COLOR)
        ax.set_ylabel('Curso', color=TEXT_COLOR)
        ax.tick_params(axis='x', colors=TEXT_COLOR)
        ax.tick_params(axis='y', colors=TEXT_COLOR)
        
        # Adjust layout to ensure course names are visible
        plt.tight_layout()
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, self.tab2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_demographic_charts(self):
        # Create frame for two charts side by side
        charts_frame = tk.Frame(self.tab3, bg=FRAME_COLOR)
        charts_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left chart - Gender distribution
        left_frame = tk.Frame(charts_frame, bg=FRAME_COLOR)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Right chart - Race distribution
        right_frame = tk.Frame(charts_frame, bg=FRAME_COLOR)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Get gender data
        gender_data = self.controller.get_scholarship_by_gender()
        
        # Create gender pie chart
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        fig1.patch.set_facecolor(FRAME_COLOR)
        
        wedges, texts, autotexts = ax1.pie(
            gender_data['count'], 
            labels=gender_data['gender'],
            autopct='%1.1f%%',
            startangle=90,
            colors=['#FF9999', '#66B2FF'],
        )
        
        for text in texts:
            text.set_color(TEXT_COLOR)
        for autotext in autotexts:
            autotext.set_color('white')
            
        ax1.set_title('Distribuição por Gênero', color=TEXT_COLOR, fontsize=14)
        
        # Embed gender chart
        canvas1 = FigureCanvasTkAgg(fig1, left_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Get race data
        race_data = self.controller.get_scholarship_by_race()
        
        # Create race pie chart
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        fig2.patch.set_facecolor(FRAME_COLOR)
        
        wedges, texts, autotexts = ax2.pie(
            race_data['count'], 
            labels=race_data['race'],
            autopct='%1.1f%%',
            startangle=90,
        )
        
        for text in texts:
            text.set_color(TEXT_COLOR)
        for autotext in autotexts:
            autotext.set_color('white')
            
        ax2.set_title('Distribuição por Raça/Etnia', color=TEXT_COLOR, fontsize=14)
        
        # Embed race chart
        canvas2 = FigureCanvasTkAgg(fig2, right_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def refresh_charts(self):
        # Clear and redraw all charts
        for widget in self.tab1.winfo_children():
            widget.destroy()
        for widget in self.tab2.winfo_children():
            widget.destroy()
        for widget in self.tab3.winfo_children():
            widget.destroy()
            
        self.create_scholarship_type_chart()
        self.create_course_chart()
        self.create_demographic_charts()
