import tkinter as tk
from tkinter import ttk
from utils.localization import _
from .graphs import NutritionGraphFrame
from services.meal_service import get_daily_nutrition

class DashboardFrame(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=_("Welcome, {}!").format(self.user.username), font=("Helvetica", 16)).pack(pady=10)

        self.summary_frame = ttk.Frame(self)
        self.summary_frame.pack(pady=10, fill='x')

        self.graph_frame = NutritionGraphFrame(self)
        self.graph_frame.pack(expand=True, fill='both', pady=10)

        self.update_summary()

    def update_summary(self):
        nutrition = get_daily_nutrition(self.user.id)
        for widget in self.summary_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.summary_frame, text=_("Daily Summary:")).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self.summary_frame, text=_("Calories:")).grid(row=1, column=0, sticky='w', padx=5)
        ttk.Label(self.summary_frame, text=f"{nutrition['calories']:.2f} kcal").grid(row=1, column=1, sticky='e', padx=5)
        ttk.Label(self.summary_frame, text=_("Protein:")).grid(row=2, column=0, sticky='w', padx=5)
        ttk.Label(self.summary_frame, text=f"{nutrition['protein']:.2f} g").grid(row=2, column=1, sticky='e', padx=5)
        ttk.Label(self.summary_frame, text=_("Carbs:")).grid(row=3, column=0, sticky='w', padx=5)
        ttk.Label(self.summary_frame, text=f"{nutrition['carbs']:.2f} g").grid(row=3, column=1, sticky='e', padx=5)
        ttk.Label(self.summary_frame, text=_("Fat:")).grid(row=4, column=0, sticky='w', padx=5)
        ttk.Label(self.summary_frame, text=f"{nutrition['fat']:.2f} g").grid(row=4, column=1, sticky='e', padx=5)

        self.graph_frame.update_graph(nutrition)