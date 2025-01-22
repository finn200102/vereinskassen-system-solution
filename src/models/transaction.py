"""This is the Model for the Transaction class"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from datatime import datetime
from src.models.account import Account

class Transaction():
    """The Transaction class."""
    def __init__(self, transaction_id: str, time_stamp: date_time, amount: float, type: str,
                 source_account: Account, target_account: Account, description: str):
        """
        Initializes the Transaction Class.

        Args:
            transaction_id(str): The transaction_id unique
            time_stamp(date_time): The time of the transaction
            amount(float): The amount of the transaction
            source_account(Account): The source account of the transaction
            target_account(Account): The target account of the transaction
            description(str): The description of the transaction
        """
        self.transaction_id = transaction_id
        self.time_stamp = time_stamp
        self.amount = amount
        self.source_account = source_account
        self.target_account = target_account
        self.description = description

    def is_valid() -> bool:
        """Check if transaction is valid"""
        return source_account.balance > self.amount
