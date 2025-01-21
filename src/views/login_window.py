""" This is the LoginView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class LoginView(BaseView):
    """The View for the Loginwindow"""

    def setup_ui(self):
        """Setup the ui."""
        username_label = ttk.Label(self, text="Username:")
        username_entry = ttk.Entry(self)
        password_label = ttk.Label(self, text="Password:")
        password_entry = ttk.Entry(self)

        # pack the widgets
        username_label.pack()
        username_entry.pack()
        password_label.pack()
        password_entry.pack()

        
        
if __name__ == "__main__":
    main()
