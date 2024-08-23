import tkinter as tk
from gui.main_window import MainWindow
from database.db_connection import engine
from database.models import Base
from utils.localization import setup_localization

def main():
    Base.metadata.create_all(bind=engine)
    setup_localization()
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()