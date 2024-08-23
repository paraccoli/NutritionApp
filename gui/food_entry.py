import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from utils.localization import _
from services.food_service import get_food_list, add_food
from services.meal_service import add_meal, get_user_meals
import locale

class FoodEntryFrame(ttk.Frame):
    def __init__(self, parent, user, update_callback):
        super().__init__(parent)
        self.user = user
        self.update_callback = update_callback
        self.food_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.meal_time_var = tk.StringVar(value="breakfast")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=_("Add Meal"), font=("Helvetica", 16)).pack(pady=10)

        food_frame = ttk.Frame(self)
        food_frame.pack(pady=5, fill='x')
        ttk.Label(food_frame, text=_("Food:")).pack(side='left', padx=5)
        self.food_combobox = ttk.Combobox(food_frame, textvariable=self.food_var, values=get_food_list())
        self.food_combobox.pack(side='left', expand=True, fill='x', padx=5)
        ttk.Button(food_frame, text=_("Add New Food"), command=self.open_add_food_dialog).pack(side='left', padx=5)

        amount_frame = ttk.Frame(self)
        amount_frame.pack(pady=5, fill='x')
        ttk.Label(amount_frame, text=_("Amount (g):")).pack(side='left', padx=5)
        ttk.Entry(amount_frame, textvariable=self.amount_var).pack(side='left', expand=True, fill='x', padx=5)

        meal_time_frame = ttk.Frame(self)
        meal_time_frame.pack(pady=5, fill='x')
        ttk.Label(meal_time_frame, text=_("Meal Time:")).pack(side='left', padx=5)
        ttk.Radiobutton(meal_time_frame, text=_("Breakfast"), variable=self.meal_time_var, value="breakfast").pack(side='left')
        ttk.Radiobutton(meal_time_frame, text=_("Lunch"), variable=self.meal_time_var, value="lunch").pack(side='left')
        ttk.Radiobutton(meal_time_frame, text=_("Dinner"), variable=self.meal_time_var, value="dinner").pack(side='left')

        ttk.Button(self, text=_("Add Meal"), command=self.add_meal).pack(pady=10)

        self.meal_list = ttk.Treeview(self, columns=("food", "amount", "time"), show="headings")
        self.meal_list.heading("food", text=_("Food"))
        self.meal_list.heading("amount", text=_("Amount (g)"))
        self.meal_list.heading("time", text=_("Meal Time"))
        self.meal_list.pack(pady=10, fill='both', expand=True)

        self.update_meal_list()

    def open_add_food_dialog(self):
        class AddFoodDialog(simpledialog.Dialog):
            def body(self, master):
                ttk.Label(master, text=_("Food Name:")).grid(row=0, column=0)
                ttk.Label(master, text=_("Calories:")).grid(row=1, column=0)
                ttk.Label(master, text=_("Protein (g):")).grid(row=2, column=0)
                ttk.Label(master, text=_("Carbs (g):")).grid(row=3, column=0)
                ttk.Label(master, text=_("Fat (g):")).grid(row=4, column=0)
                ttk.Label(master, text=_("Category:")).grid(row=5, column=0)  # 新しい行を追加

                self.e1 = ttk.Entry(master)
                self.e2 = ttk.Entry(master)
                self.e3 = ttk.Entry(master)
                self.e4 = ttk.Entry(master)
                self.e5 = ttk.Entry(master)
                self.e6 = ttk.Entry(master)  # カテゴリー用の新しいエントリー

                self.e1.grid(row=0, column=1)
                self.e2.grid(row=1, column=1)
                self.e3.grid(row=2, column=1)
                self.e4.grid(row=3, column=1)
                self.e5.grid(row=4, column=1)
                self.e6.grid(row=5, column=1)  # カテゴリー用のエントリーを配置
                return self.e1  # initial focus

            def apply(self):
                name = self.e1.get()
                calories = float(self.e2.get())
                protein = float(self.e3.get())
                carbs = float(self.e4.get())
                fat = float(self.e5.get())
                category = self.e6.get()  # カテゴリーを取得
                add_food(name, calories, protein, carbs, fat, category)  # カテゴリーを追加
                self.result = name

        dialog = AddFoodDialog(self)
        if dialog.result:
            self.food_combobox['values'] = get_food_list()
            self.food_var.set(dialog.result)

    def add_meal(self):
        food = self.food_var.get()
        amount_str = self.amount_var.get()
        meal_time = self.meal_time_var.get()

        if not food or not amount_str:
            messagebox.showerror(_("Error"), _("Please enter both food and amount"))
            return

        try:
            amount = locale.atof(amount_str)
            add_meal(self.user.id, food, amount, meal_time)
            messagebox.showinfo(_("Success"), _("Meal added successfully"))
            self.food_var.set("")
            self.amount_var.set("")
            self.update_meal_list()
            self.update_callback()
        except ValueError:
            messagebox.showerror(_("Error"), _("Invalid amount. Please enter a number"))
        except Exception as e:
            messagebox.showerror(_("Error"), str(e))

    def update_meal_list(self):
        for item in self.meal_list.get_children():
            self.meal_list.delete(item)
        meals = get_user_meals(self.user.id)
        for meal in meals:
            self.meal_list.insert("", "end", values=(meal.food.name, f"{meal.amount:.1f}", _(meal.meal_time.capitalize())))

# メイン関数の前に以下を追加
locale.setlocale(locale.LC_ALL, '')