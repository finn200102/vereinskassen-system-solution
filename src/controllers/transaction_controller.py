"""This is the TransactionController Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"


class TransactionController:
    """This is the TransactionController Class."""
    def __init__(self, data_handler):
        """Initialize the TransactionController"""
        self.data_handler = data_handler

    def get_balance(self, account):
        """Return the balance of an account."""
        return account.balance

    def transaction(self, account, target_account):
        """Handle transacton."""
        account.transaction(target_account)

    def get_accounts(self):
        """Return list of all accounts."""
        return self.data_handler.accounts

    def get_account_detail(self, account):
        """Return account details."""
        return account.department, account.balance, account.user

    
