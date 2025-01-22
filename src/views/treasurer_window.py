""" This is the TreasurerView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView

class TreasurerView(ttk.Frame):
    """The View for the Treasurer"""

    def __init__(self, parent):
        """Initilize the TreasurerView"""
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        label = ttk.Label(self, text="Treasurer Window")
        label.pack()
