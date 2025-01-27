""" This is the MainView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView
from src.views.login_window import LoginView
from src.views.treasurer_window import TreasurerView
from src.views.admin_window import AdministratorView
from src.views.finance_window import FinanceView

class MainView(ttk.Frame):
    """The View for the Mainwindow"""
    def __init__(self, master):
        """Initialize the MainView"""
        super().__init__(master)
        self.master = master
        self.current_view = None
        self.role = 1 # for testing 0 is treasurer
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        self.show_login()

    def show_login(self):
        """Show the login View."""
        self.current_view = LoginView(self, self.on_login_success)
        self.current_view.pack()

    def on_login_success(self):
        """Shows the dashboard on login"""
        if self.current_view:
            self.current_view.destroy()
        if self.role == 0:
            self.current_view = TreasurerView(self)
            self.current_view.pack()
        if self.role == 1:
            self.current_view = AdministratorView(self)
            self.current_view.pack()
        if self.role == 2:
            self.current_view = FinanceView(self)
            self.current_view.pack()
        
        
