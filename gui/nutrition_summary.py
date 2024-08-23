import tkinter as tk
from tkinter import ttk
from utils.localization import _
from services.meal_service import get_daily_nutrition, get_weekly_nutrition

class NutritionSummaryFrame(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=_("Nutrition Summary"), font=("Helvetica", 16)).pack(pady=10)

        self.summary_notebook = ttk.Notebook(self)
        self.summary_notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.daily_summary = ttk.Frame(self.summary_notebook)
        self.weekly_summary = ttk.Frame(self.summary_notebook)

        self.summary_notebook.add(self.daily_summary, text=_("Daily"))
        self.summary_notebook.add(self.weekly_summary, text=_("Weekly"))

        self.update_summary()

    def update_summary(self):
        self.update_daily_summary()
        self.update_weekly_summary()

    def update_daily_summary(self):
        nutrition = get_daily_nutrition(self.user.id)
        for widget in self.daily_summary.winfo_children():
            widget.destroy()

        ttk.Label(self.daily_summary, text=_("Daily Nutrition:")).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self.daily_summary, text=_("Calories:")).grid(row=1, column=0, sticky='w', padx=5)
        ttk.Label(self.daily_summary, text=f"{nutrition['calories']:.2f} kcal").grid(row=1, column=1, sticky='e', padx=5)
        ttk.Label(self.daily_summary, text=_("Protein:")).grid(row=2, column=0, sticky='w', padx=5)
        ttk.Label(self.daily_summary, text=f"{nutrition['protein']:.2f} g").grid(row=2, column=1, sticky='e', padx=5)
        ttk.Label(self.daily_summary, text=_("Carbs:")).grid(row=3, column=0, sticky='w', padx=5)
        ttk.Label(self.daily_summary, text=f"{nutrition['carbs']:.2f} g").grid(row=3, column=1, sticky='e', padx=5)
        ttk.Label(self.daily_summary, text=_("Fat:")).grid(row=4, column=0, sticky='w', padx=5)
        ttk.Label(self.daily_summary, text=f"{nutrition['fat']:.2f} g").grid(row=4, column=1, sticky='e', padx=5)

    def update_weekly_summary(self):
        nutrition = get_weekly_nutrition(self.user.id)
        for widget in self.weekly_summary.winfo_children():
            widget.destroy()

        ttk.Label(self.weekly_summary, text=_("Weekly Average:")).grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(self.weekly_summary, text=_("Calories:")).grid(row=1, column=0, sticky='w', padx=5)
        ttk.Label(self.weekly_summary, text=f"{nutrition['calories']:.2f} kcal").grid(row=1, column=1, sticky='e', padx=5)
        ttk.Label(self.weekly_summary, text=_("Protein:")).grid(row=2, column=0, sticky='w', padx=5)
        ttk.Label(self.weekly_summary, text=f"{nutrition['protein']:.2f} g").grid(row=2, column=1, sticky='e', padx=5)
        ttk.Label(self.weekly_summary, text=_("Carbs:")).grid(row=3, column=0, sticky='w', padx=5)
        ttk.Label(self.weekly_summary, text=f"{nutrition['carbs']:.2f} g").grid(row=3, column=1, sticky='e', padx=5)
        ttk.Label(self.weekly_summary, text=_("Fat:")).grid(row=4, column=0, sticky='w', padx=5)
        ttk.Label(self.weekly_summary, text=f"{nutrition['fat']:.2f} g").grid(row=4, column=1, sticky='e', padx=5)