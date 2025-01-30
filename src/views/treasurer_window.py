""" This is the TreasurerView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class TreasurerView(ttk.Frame):
    """The View for the Treasurer"""

    def __init__(self, parent, setup_login, account, transaction_controller, data_handler):
        """Initilize the TreasurerView"""
        self.logout = None
        self.setup_login = setup_login
        self.account = account
        self.transaction_controller = transaction_controller
        self.data_handler = data_handler
        self.transaction_amount = None
        self.account_select = None
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def log_out(self):
        """Logout."""
        self.setup_login()

    def transfer(self):
        """Transfer."""
        try:
            target_account = self.account_select.get()
            amount = float(self.transaction_amount.get())
            self.transaction_controller.transaction(self.account, target_account, amount, "")
        except ValueError:
            print("Not a valid input")

    def deposit(self):
        """Deposit amount."""
        try:
            amount = float(self.transaction_amount.get())
            self.account.add(amount)
        except ValueError:
            print("Not a valid input")
            

    def withdraw(self):
        """Withdraw amount."""
        try:
            amount = float(self.transaction_amount.get())
            self.account.remove(amount)
        except ValueError:
            print("Not a valid input")
            

    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self, text="Treasurer Window")
        current_balance_label = ttk.Label(label, text="Current Balance:")
        current_balance = ttk.Label(label, text=f"{self.account.balance}")
        transaction_amount_label = ttk.Label(label, text="Enter your transfer amount:")
        self.transaction_amount = ttk.Entry(label)
        self.account_select = ttk.Combobox(label, values = [account.account_id for account in self.data_handler.accounts])
        deposit_button = ttk.Button(label, text="deposit", command=self.deposit)
        withdraw_button = ttk.Button(label, text="withdraw", command=self.withdraw)
        transfer_button = ttk.Button(label, text="transfer", command=self.transfer)
        transaction_history_label = ttk.Label(label, text="Transaction History:")
        # set up treeview
        transaction_history = ttk.Treeview(label)
        transaction_history['columns'] = ('ID', 'amount')
        transaction_history.column('#0', width=150)  # Main column
        transaction_history.column('ID', width=100)
        transaction_history.column('amount', width=150)
        for transaction in self.data_handler.get_transaction_by_account(self.account):
            transaction_history.insert('', 'end', 'item1', text='Item 1', values=(transaction.transaction_id, transaction.amount))

        
        self.logout = ttk.Button(label, text="Logout", command=self.log_out)

        current_balance_label.pack()
        current_balance.pack()
        transaction_amount_label.pack()
        self.transaction_amount.pack()
        self.account_select.pack()
        deposit_button.pack()
        withdraw_button.pack()
        transfer_button.pack()
        transaction_history_label.pack()
        transaction_history.pack() 

        label.pack()
        self.logout.pack()
