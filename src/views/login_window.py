""" This is the LoginView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class LoginView(BaseView):
    """The View for the Loginwindow"""

    def __init__(self, parent, on_login_callback, auth_controller):
        self.on_login_callback = on_login_callback
        self.auth_controller = auth_controller
        self.username_entry = None
        self.password_entry = None
        super().__init__(parent)
        self.parent = parent
        
    def setup_ui(self):
        """Setup the ui."""
        # clear ui
        for widget in self.winfo_children():
            widget.destroy()
            
        # create login frame
        login_frame = ttk.Frame(self)
        username_label = ttk.Label(login_frame, text="Username:")
        self.username_entry = ttk.Entry(login_frame)
        password_label = ttk.Label(login_frame, text="Password:")
        self.password_entry = ttk.Entry(login_frame)
        login_button = ttk.Button(login_frame, text="Login", command=self.login)

        # pack the widgets
        username_label.pack()
        self.username_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        login_button.pack()

        login_frame.pack()

    def login_valid(self):
        """Checks if login is valid"""
        log = self.auth_controller.login(self.username_entry.get(), self.password_entry.get())
        if log:
            return log
        else:
            return False


    def login(self):
        """Login into the MainView"""
        if self.login_valid():
            self.on_login_callback(self.login_valid())
            
            
        

        
        
if __name__ == "__main__":
    main()
