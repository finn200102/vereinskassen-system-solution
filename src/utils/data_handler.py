"""This is the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.user import User
from src.models.account import Account
from src.models.transaction import Transaction
import csv

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

    def save_data(self, data):
        """
        Save an specific data object

        Args:
            data(object): User, Accounts, Transactions
        """
        if type(data) == User:
            self.users.append(data)
        if type(data) == Account:
            self.accounts.append(data)
        if type(data) == Transaction:
            self.transactions.append(data)
        

    def load_data(self, data_type, key):
        """
        Load an specific data object with data_type with key

        Args:
            data_type(string): The data_type 
            key(string/int): The primary key of the data_type
        """
        if data_type == "user":
            matches = list(filter(lambda user: user.username == key, self.users))
            return matches[0] if matches else None
            
        if data_type == "account":
            matches = list(filter(lambda account: account.account_id == key, self.accounts))
            return matches[0] if matches else None
        if data_type == "transaction":
            matches = list(filter(lambda transaction: transaction.transaction_id == key, self.transactions))
            return matches[0] if matches else None

    def import_from_csv():
        """
        Load the full data from the csvs
        """
        pass

    def convert_user_to_dict(self, user):
        """Convert user to dict"""

        user_dict = {
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "department": user.department
        }
        return user_dict

    def convert_to_dict(self):
        """Convert to dict"""
        save_users = [self.convert_user_to_dict(user) for user in self.users]
        return save_users
    
    def export_to_csv(self):
        """
        Export the full data to the csvs
        """
        save_users = self.convert_to_dict()
        with open(self.users_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames = list(save_users[0].keys()))
            writer.writeheader()
            writer.writerows(save_users)
            

        
