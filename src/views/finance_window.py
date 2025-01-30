""" This is the Finance Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class FinanceView(ttk.Frame):
    """The View for the Finance"""

    def __init__(self, parent, data_handler):
        """Initilize the FinanceView"""
        self.data_handler = data_handler
        self.account = None
        self.status = None
        self.total_ammount = None
        self.total_overview = None
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()


    def sel_account(self):
        """Select account."""
        account = self.account.get()
        if account:

            for idx, transaction in enumerate(self.data_handler.get_transaction_by_account(self.data_handler.load_data("account", account))):
                self.status.insert('', 'end', f'transaction {transaction.transaction_id}',
                                   text=f'transaction {transaction.transaction_id}',
                                   values=(f"target account {transaction.target_account.account_id}",transaction.amount))


            


    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self, text="FinanceView")
        account_label = ttk.Label(self, text="Account:")
        self.account = ttk.Combobox(self, values = [account.account_id for account in self.data_handler.accounts])
        
        status_label = ttk.Label(self, text="Status:")
        self.status = ttk.Treeview(self)
        self.status['columns'] = ('target', 'amount')
        self.status.column('#0', width=150)  # Main column
        self.status.column('target', width=100)
        self.status.column('amount', width=150)
        select_account = ttk.Button(self, text="Select Account", command=self.sel_account)
        total_ammount_label = ttk.Label(self, text="Total Ammount:")

        total_overview_label = ttk.Label(self, text="Total Overview:")
        self.total_overview = ttk.Treeview(self)
        self.total_overview['columns'] = ('department', 'balance')
        self.total_overview.column('#0', width=150)  # Main column
        self.total_overview.column('department', width=100)
        self.total_overview.column('balance', width=150)
        total = 0
        for idx, account in enumerate(self.data_handler.accounts):
            self.total_overview.insert('', 'end', f'account {account.account_id}', text=f'account {account.account_id}',
                                       values=(account.department, account.balance))
            total += account.balance
        self.total_ammount = ttk.Label(self, text=f"{total}")
        
        label.pack()
        account_label.pack()
        self.account.pack()
        select_account.pack()
        status_label.pack()
        self.status.pack()


        total_overview_label.pack()
        self.total_overview.pack()
        total_ammount_label.pack()
        self.total_ammount.pack()

