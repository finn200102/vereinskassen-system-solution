"""This is the main of a treasury managmetn system"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
import tkinter as tk
from src.views.main_view import MainView

class TreasuryApp:
    """Treasury App"""
    def __init__(self):
        """Initialize treasurey app"""
        self.root = tk.Tk()
        self.root.title("Treasury management system")
        self.root.geometry('1000x800')
        self.main_view = MainView(self.root)
        self.main_view.pack()

    def run(self):
        """Run mainloop"""
        self.root.mainloop()
        


def main():
    """Main function of the treasury system."""
    # set up root of the application
    app = TreasuryApp()
    app.run()
    
if __name__ == "__main__":
    main()
