import tkinter as tk
from tkinter import ttk, font, simpledialog, messagebox
from .dashboard import DashboardFrame
from .food_entry import FoodEntryFrame
from .nutrition_summary import NutritionSummaryFrame
from .login import LoginFrame
from .profile import ProfileFrame
from utils.localization import _, setup_localization
import utils.config as config

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title(_("Nutrition Tracker"))
        self.master.geometry("800x600")
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # 日本語対応フォントの設定
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Meiryo UI")
        self.style.configure('.', font=("Meiryo UI", 10))

        self.current_user = None
        self.show_login()

    def show_login(self):
        self.login_frame = LoginFrame(self.master, self.on_login_success)
        self.login_frame.pack(expand=True, fill='both')

    def on_login_success(self, user):
        self.current_user = user
        self.login_frame.destroy()
        self.show_main_interface()

    def show_main_interface(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        self.dashboard = DashboardFrame(self.notebook, self.current_user)
        self.food_entry = FoodEntryFrame(self.notebook, self.current_user, self.update_all)
        self.nutrition_summary = NutritionSummaryFrame(self.notebook, self.current_user)
        self.profile = ProfileFrame(self.notebook, self.current_user)

        self.notebook.add(self.dashboard, text=_("Dashboard"))
        self.notebook.add(self.food_entry, text=_("Add Meal"))
        self.notebook.add(self.nutrition_summary, text=_("Nutrition Summary"))
        self.notebook.add(self.profile, text=_("Profile"))

        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=_("File"), menu=file_menu)
        file_menu.add_command(label=_("Settings"), command=self.open_settings)
        file_menu.add_command(label=_("Logout"), command=self.logout)
        file_menu.add_command(label=_("Exit"), command=self.master.quit)

        language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=_("Language"), menu=language_menu)
        language_menu.add_command(label="English", command=lambda: self.change_language('en'))
        language_menu.add_command(label="日本語", command=lambda: self.change_language('ja'))

    def update_all(self):
        self.dashboard.update_summary()
        self.nutrition_summary.update_summary()

    def open_settings(self):
        def on_language_change(new_language):
            config.CURRENT_LANGUAGE = new_language
            setup_localization(new_language)
            self.master.destroy()
            new_root = tk.Tk()
            MainWindow(new_root)
            new_root.mainloop()

        SettingsDialog(self.master, _("Settings"), config.CURRENT_LANGUAGE, on_language_change)

    def logout(self):
        if messagebox.askyesno(_("Logout"), _("Are you sure you want to logout?")):
            self.current_user = None
            self.notebook.destroy()
            self.master.config(menu="")
            self.show_login()

    def change_language(self, lang):
        config.CURRENT_LANGUAGE = lang
        setup_localization(lang)
        self.master.destroy()
        new_root = tk.Tk()
        MainWindow(new_root)
        new_root.mainloop()

class SettingsDialog(simpledialog.Dialog):
    def __init__(self, parent, title, current_language, on_language_change):
        self.current_language = current_language
        self.on_language_change = on_language_change
        super().__init__(parent, title)

    def body(self, master):
        ttk.Label(master, text=_("Language:")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.language_var = tk.StringVar(value=self.current_language)
        self.language_combo = ttk.Combobox(master, textvariable=self.language_var, values=["en", "ja"])
        self.language_combo.grid(row=0, column=1, padx=5, pady=5)

        return self.language_combo