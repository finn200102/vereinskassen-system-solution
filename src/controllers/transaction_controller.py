"""This is the TransactionController Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.transaction import Transaction
from datetime import datetime


class TransactionController:
    """This is the TransactionController Class."""
    def __init__(self, data_handler):
        """Initialize the TransactionController"""
        self.data_handler = data_handler

    def get_balance(self, account):
        """Return the balance of an account."""
        return account.balance

    def transaction(self, account, target_account, amount, description):
        """Handle transacton."""
        target_account = self.data_handler.load_data("account", target_account)
        transaction = Transaction(str(len(self.data_handler.transactions)), datetime.now(), amount, "",
                    account, target_account, description)
        self.data_handler.save_data(transaction)
        account.add_transaction(transaction)
        target_account.add_transaction(transaction)
        

    def get_accounts(self):
        """Return list of all accounts."""
        return self.data_handler.accounts

    def get_account_detail(self, account):
        """Return account details."""
        return account.department, account.balance, account.user

    
