import tkinter as tk
from tkinter import ttk, messagebox
from utils.localization import _
from services.user_service import update_user_profile, get_user_profile

class ProfileFrame(ttk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=_("User Profile"), font=("Helvetica", 16)).pack(pady=10)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()

        ttk.Label(self, text=_("Name:")).pack(pady=5)
        ttk.Entry(self, textvariable=self.name_var).pack(pady=5)

        ttk.Label(self, text=_("Age:")).pack(pady=5)
        ttk.Entry(self, textvariable=self.age_var).pack(pady=5)

        ttk.Label(self, text=_("Height (cm):")).pack(pady=5)
        ttk.Entry(self, textvariable=self.height_var).pack(pady=5)

        ttk.Label(self, text=_("Weight (kg):")).pack(pady=5)
        ttk.Entry(self, textvariable=self.weight_var).pack(pady=5)

        ttk.Button(self, text=_("Update Profile"), command=self.update_profile).pack(pady=10)

        self.load_profile()

    def load_profile(self):
        profile = get_user_profile(self.user.id)
        if profile:
            self.name_var.set(profile.name)
            self.age_var.set(profile.age)
            self.height_var.set(profile.height)
            self.weight_var.set(profile.weight)

    def update_profile(self):
        try:
            profile_data = {
                'name': self.name_var.get(),
                'age': int(self.age_var.get()),
                'height': float(self.height_var.get()),
                'weight': float(self.weight_var.get())
            }
            update_user_profile(self.user.id, profile_data)
            messagebox.showinfo(_("Success"), _("Profile updated successfully"))
        except Exception as e:
            messagebox.showerror(_("Error"), _("Failed to update profile: {}").format(str(e)))