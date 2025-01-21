"""This is the main of a treasury managmetn system"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from src.views.login_window import LoginView


def main():
    """Main function of the treasury system."""
    # set up root of the application
    root = tk.Tk()
    root.title("Treasury management system")
    root.geometry('500x500')
    login_view = LoginView(root)
    login_view.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
