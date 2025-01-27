""" This is the Administrator Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class AdministratorView(ttk.Frame):
    """The View for the Administrator"""

    def __init__(self, parent):
        """Initilize the AdministratorView"""
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self)
        admin_label = ttk.Label(label, text="AdministratorView")
        username_label = ttk.Label(label, text="Create Username:")
        create_username = ttk.Entry(label)
        password_label = ttk.Label(label, text="Create Password:")
        create_password = ttk.Entry(label)
        role_label = ttk.Label(label, text="Role Selection:")
        role_selection = ttk.Combobox(label, values = ["admin", "user"])
        user_label = ttk.Label(label, text="User:")
        user_view = ttk.Treeview(label)
        create_user_button = ttk.Button(label, text="Create User")
        account_id_label = ttk.Label(label, text="AccountID:")
        account_id = ttk.Entry(label)
        department_label = ttk.Label(label, text="Department:")
        department = ttk.Entry(label)
        user_select_label = ttk.Label(label, text="Select User:")
        user_select = ttk.Combobox(label, values = ["1","2"])
        create_acc = ttk.Button(label, text="Create Account")

        admin_label.pack()
        username_label.pack()
        create_username.pack()
        password_label.pack()
        create_password.pack()
        role_label.pack()
        role_selection.pack()
        user_label.pack()
        user_view.pack(pady=10)
        create_user_button.pack()

        account_id_label.pack()
        account_id.pack()
        department_label.pack()
        department.pack()
        user_select_label.pack()
        user_select.pack()
        create_acc.pack(pady=10)

        label.pack()
