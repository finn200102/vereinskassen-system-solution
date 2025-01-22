"""This is the Model for the Account class"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.user import User

class Account():
    """The Account class."""
    def __init__(self, account_id: str, department: str, balance: float, treasurer: User):
        """
        Initializes the Account Class.

        Args:
            account_id(str): The account_id
            department(str): The department of the account
            balance(float): The balance of the account
            treasurer(User): The treasurer/user of the account
        """
        self.account_id = account_id
        self.department = department
        self.balance = balance
        self.treasurer = treasurer


    def get_balance(self) -> float:
        """Return balance"""
        return self.balance

    def add_transaction(transaction) -> bool:
        """
        Implement the transaction.

        Args: transaction(Transaction)
        """
        if transaction.source_account == self:
            self.balance -= transaction.amount
        else:
            self.balance += transaction.amount
