""" This is the MainView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView
from src.views.login_window import LoginView
from src.views.treasurer_window import TreasurerView
from src.views.admin_window import AdministratorView
from src.views.finance_window import FinanceView
from src.controllers.auth_controller import AuthController
from src.utils.data_handler import DataHandler
from src.models.user import User
from src.models.account import Account

class MainView(ttk.Frame):
    """The View for the Mainwindow"""
    def __init__(self, master):
        """Initialize the MainView"""
        super().__init__(master)
        self.master = master
        users_file = "data/files/users.csv"
        accounts_file = "data/files/accounts.csv"
        transactions_file = "data/files/transactions.csv"
        self.data_handler = DataHandler(users_file, accounts_file, transactions_file)
        self.data_handler.save_data(User("admin", "1234", "admin", "sport"))
        self.data_handler.import_from_csv()
        self.auth_controller = AuthController(self.data_handler)
        self.current_view = None
        self.role = 0 # for testing 0 is treasurer
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        self.show_login()

    def create_user(self, username, password, department, role):
        """Create User"""
        self.data_handler.save_data(User(username, password, role, department))
        print(f"Created new user {username}")

    def create_account(self, account_id, department, treasurer):
        """Create Account."""
        treasurer = self.data_handler.load_data("user", treasurer)
        self.data_handler.save_data(Account(account_id, department, 0.0, treasurer))
        print(f"Created new account {account_id}")


    def show_login(self):
        """Show the login View."""
        if self.current_view:
            self.current_view.destroy()
        self.current_view = LoginView(self, self.on_login_success, self.auth_controller)
        self.current_view.pack()

    def on_login_success(self, user_role, username):
        """Shows the dashboard on login"""
        self.role = user_role
        if self.current_view:
            self.current_view.destroy()
        if self.role == "admin":
            self.current_view = AdministratorView(self, self.show_login, self.create_user,
                                                  self.create_account, self.data_handler)
            self.current_view.pack()
        if self.role == "treasurer":
            account = self.data_handler.get_account_by_user(username)
            self.current_view = TreasurerView(self, self.show_login, account)
            self.current_view.pack()
        if self.role == "referee":
            self.current_view = FinanceView(self)
            self.current_view.pack()
        
        
