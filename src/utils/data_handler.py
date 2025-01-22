"""This is the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.user import User
from src.models.account import Account
from src.models.transaction import Transaction
from datetime import datetime
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

    def import_from_csv(self):
        """
        Load the full data from the csvs
        """
        try:
            # Import users from csv
            with open(self.users_file, 'r', newline='') as f:
                user_dicts = list(csv.DictReader(f))
                self.users = [self.convert_dict_to_user(user_dict) for user_dict in user_dicts]
            # Import accounts from csv
            with open(self.accounts_file, 'r', newline='') as f:
                account_dicts = list(csv.DictReader(f))
                self.accounts = [self.convert_dict_to_account(account_dict) for account_dict in account_dicts]
            # Import accounts from csv
            with open(self.transactions_file, 'r', newline='') as f:
                transaction_dicts = list(csv.DictReader(f))
                self.transactions = [self.convert_dict_to_transaction(transaction_dict) for transaction_dict in transaction_dicts]
                
        except FileNotFoundError:
            print("Files not found")

    def convert_user_to_dict(self, user):
        """Convert user to dict"""

        user_dict = {
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "department": user.department
        }
        return user_dict

    def convert_account_to_dict(self, account):
        """Convert account to dict"""
        # convert to dict user to username
        account_dict = {
            "account_id": account.account_id,
            "department": account.department,
            "balance": account.balance,
            "treasurer": account.treasurer.username
        }
        return account_dict

    def convert_transaction_to_dict(self, transaction):
        """Convert transaction to dict"""
        # convert to dict account as account_id
        transaction_dict = {
            "transaction_id": transaction.transaction_id,
            "time_stamp": transaction.time_stamp.strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "source_account": transaction.source_account.account_id,
            "target_account": transaction.target_account.account_id,
            "description": transaction.description
        }
        return transaction_dict

    def convert_dict_to_user(self, user_dict):
        """Convert user_dict to user"""
        user = User(user_dict["username"],
                    user_dict["password"],
                    user_dict["role"],
                    user_dict["department"])
        return user

    def convert_dict_to_account(self, account_dict):
        """Convert account_dict to account"""
        account = Account(account_dict["account_id"],
                    account_dict["department"],
                    account_dict["balance"],
                    self.load_data("user", account_dict["treasurer"]))
        return account

    def convert_dict_to_transaction(self, transaction_dict):
        """Convert transaction_dict to transaction"""
        transaction = Transaction(transaction_dict["transaction_id"],
                                  datetime.strptime(transaction_dict["time_stamp"], "%d-%b-%Y (%H:%M:%S.%f)"),
                                  transaction_dict["amount"],
                                  transaction_dict["transaction_type"],
                                  self.load_data("account", transaction_dict["source_account"]),
                                  self.load_data("account", transaction_dict["target_account"]),
                                  transaction_dict["description"])
        return transaction
        

    def convert_to_dict(self):
        """Convert to dict"""
        save_users = [self.convert_user_to_dict(user) for user in self.users]
        save_accounts = [self.convert_account_to_dict(account) for account in self.accounts]
        save_transactions = [self.convert_transaction_to_dict(transaction) for transaction in self.transactions]
        return save_users, save_accounts, save_transactions
    
    def export_to_csv(self):
        """
        Export the full data to the csvs
        """
        save_users, save_accounts, save_transactions = self.convert_to_dict()
        # Export the Users to csv
        if self.users:
            with open(self.users_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = list(save_users[0].keys()))
                writer.writeheader()
                writer.writerows(save_users)
        # Export the Accounts to csv
        if self.accounts:
            with open(self.accounts_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = list(save_accounts[0].keys()))
                writer.writeheader()
                writer.writerows(save_accounts)
        # Export the Transactions to csv
        if self.transactions:
            with open(self.transactions_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames = list(save_transactions[0].keys()))
                writer.writeheader()
                writer.writerows(save_transactions)
            

        
