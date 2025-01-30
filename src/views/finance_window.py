""" This is the Finance Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class FinanceView(ttk.Frame):
    """The View for the Finance"""

    def __init__(self, parent):
        """Initilize the FinanceView"""
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self, text="FinanceView")
        account_label = ttk.Label(self, text="Account:")
        account = ttk.Combobox(self)
        status_label = ttk.Label(self, text="Status:")
        status = ttk.Treeview(self)
        select_account = ttk.Button(self, text="Select Account")
        total_ammount_label = ttk.Label(self, text="Total Ammount:")
        total_ammount = ttk.Label(self)
        total_overview_label = ttk.Label(self, text="Total Overview:")
        total_overview = ttk.Treeview(self)
        
        label.pack()
        account_label.pack()
        account.pack()
        select_account.pack()
        status_label.pack()
        status.pack()
        total_ammount_label.pack()
        total_ammount.pack()
        total_overview_label.pack()
        total_overview.pack()

