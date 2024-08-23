import tkinter as tk
from tkinter import ttk, messagebox
from utils.localization import _
from services.auth_service import authenticate_user, create_user

class LoginFrame(ttk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=_("Login"), font=("Helvetica", 16)).pack(pady=10)

        ttk.Label(self, text=_("Username:")).pack(pady=5)
        ttk.Entry(self, textvariable=self.username_var).pack(pady=5)

        ttk.Label(self, text=_("Password:")).pack(pady=5)
        ttk.Entry(self, textvariable=self.password_var, show="*").pack(pady=5)

        ttk.Button(self, text=_("Login"), command=self.login).pack(pady=10)
        ttk.Button(self, text=_("Register"), command=self.register).pack(pady=5)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        user = authenticate_user(username, password)
        if user:
            self.on_login_success(user)
        else:
            messagebox.showerror(_("Login Failed"), _("Invalid username or password"))

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        if create_user(username, password):
            messagebox.showinfo(_("Registration Successful"), _("You can now login with your new account"))
        else:
            messagebox.showerror(_("Registration Failed"), _("Username already exists or invalid input"))