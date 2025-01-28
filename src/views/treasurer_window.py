""" This is the TreasurerView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class TreasurerView(ttk.Frame):
    """The View for the Treasurer"""

    def __init__(self, parent, setup_login, account):
        """Initilize the TreasurerView"""
        self.logout = None
        self.setup_login = setup_login
        self.account = account
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def log_out(self):
        """Logout."""
        self.setup_login()

    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self, text="Treasurer Window")
        current_balance_label = ttk.Label(label, text="Current Balance:")
        current_balance = ttk.Label(label, text=f"{self.account.balance}")
        transaction_amount_label = ttk.Label(label, text="Enter your transfer amount:")
        transaction_amount = ttk.Entry(label)
        deposit_button = ttk.Button(label, text="deposit")
        withdraw_button = ttk.Button(label, text="withdraw")
        transfer_button = ttk.Button(label, text="transfer")
        transaction_history_label = ttk.Label(label, text="Transaction History:")
        transaction_history = ttk.Treeview(label)
        self.logout = ttk.Button(label, text="Logout", command=self.log_out)

        current_balance_label.pack()
        current_balance.pack()
        transaction_amount_label.pack()
        transaction_amount.pack()
        deposit_button.pack()
        withdraw_button.pack()
        transfer_button.pack()
        transaction_history_label.pack()
        transaction_history.pack() 

        label.pack()
        self.logout.pack()
