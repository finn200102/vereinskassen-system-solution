""" This is the MainView Class """
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from tkinter import ttk
from src.views.base_view import BaseView
from src.views.login_window import LoginView

class MainView(ttk.Frame):
    """The View for the Basewindow"""
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.current_view = None
        self.setup_ui()

    def setup_ui(self):
        """Setup the ui."""
        self.show_login()

    def show_login(self):
        """Show the login View."""
        self.current_view = LoginView(self)
        self.current_view.pack()
        
        
