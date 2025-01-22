"""This is the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"

class DataHandler:
    """DataHandler Class that manages the loading and saving to csv"""
    def __init__(self, users_file, accounts_file, transactions_file):
        """This initializes the DataHandler Class"""
        # load file paths
        self.users_file = users_file
        self.accounts_file = accounts_file
        self.transactions_file = transactions_file
        # create lists for objects
        self.users = []
        self.accounts = []
        self.transactions = []

    def save_data(self, data_type, data):
        """
        Save an specific data object with data_type

        Args:
            data_type(string): The data_type
            data(object): User, Accounts, Transactions
        """
        pass

    def load_data(self, data_type, key):
        """
        Load an specific data object with data_type with key

        Args:
            data_type(string): The data_type 
            key(string/int): The primary key of the data_type
        """
        pass

    def import_from_csv():
        """
        Load the full data from the csvs
        """
        pass
    def export_to_csv():
        """
        Export the full data to the csvs
        """
        pass
