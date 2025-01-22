"""This is the Test for the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.utils.data_handler import DataHandler
from src.models.user import User
from src.models.account import Account
from src.models.transaction import Transaction
from src.models.user_role import UserRole
from datetime import datetime


def test_add_user(data_handler: DataHandler):
    """
    Test save_data with a user.

    Args:
        data_handler(DataHandler): The data handler
    """
    user = User("hanz", "1234", UserRole.admin, "sport")
    data_handler.save_data(user)
    assert data_handler.users[0] == user
    print("Test add_user has passed")


def test_add_account(data_handler: DataHandler):
    """
    Test save_data with a account.

    Args:
        data_handler(DataHandler): The data handler
    """
    user = data_handler.load_data("user", "franz")
    account = Account("abc", "sport", 0.4, user)
    data_handler.save_data(account)
    assert data_handler.accounts[0] == account
    print("Test add_account has passed")

def test_add_transaction(data_handler: DataHandler):
    """
    Test save_data with a transaction.

    Args:
        data_handler(DataHandler): The data handler
    """
    user1 = data_handler.load_data("user", "franz")
    user2 = data_handler.load_data("user", "hanz")
    account1 = Account("abc1", "sport", 20.0, user1)
    account2 = Account("abc2", "running", 30.0, user2)
    transaction = Transaction("ab", datetime.now(), 5.0, "move",
                              account1, account2, "asdf")
    data_handler.save_data(transaction)
    assert data_handler.transactions[0] == transaction
    print("Test add_transaction has passed")


def test_load_user(data_handler: DataHandler):
    """
    Test load_data with a user.

    Args:
        data_handler(DataHandler): The data handler
    """
    user = User("franz", "1234", UserRole.admin, "running")
    data_handler.save_data(user)
    assert data_handler.load_data("user", "franz") == user
    print("Test load_user has passed")

    
def test_load_account(data_handler: DataHandler):
    """
    Test load_data with a account.

    Args:
        data_handler(DataHandler): The data handler
    """
    assert data_handler.load_data("account", "abc").account_id == "abc"
    print("Test load_account has passed")


def test_load_transaction(data_handler: DataHandler):
    """
    Test load_data with a transaction.

    Args:
        data_handler(DataHandler): The data handler
    """
    assert data_handler.load_data("transaction", "ab").transaction_id == "ab"
    print("Test load_transaction has passed")



def test_export_import(data_handler: DataHandler, users_file, accounts_file, transactions_file):
    """
    Test export_to_csv and import_from_csv

    Args:
        data_handler(DataHandler): The data handler
    """
    # clean the files
    with open(users_file, 'w') as file:
        file.write('')
    with open(accounts_file, 'w') as file:
        file.write('')
    with open(transactions_file, 'w') as file:
        file.write('')
        
    data_handler.export_to_csv()
    data_handler.users = []
    data_handler.accounts = []
    data_handler.transactions = []
    data_handler.import_from_csv()


    assert data_handler.load_data("user", "franz").username == "franz"
    assert data_handler.load_data("account", "abc").account_id == "abc"
    assert data_handler.load_data("transaction", "ab").transaction_id == "ab"


    print("Test import and export passed")

    # clean the files
    with open(users_file, 'w') as file:
        file.write('')
    with open(accounts_file, 'w') as file:
        file.write('')
    with open(transactions_file, 'w') as file:
        file.write('')



def main():
    """Main Function."""
    users_file = "tests/files/users_file.csv"
    accounts_file = "tests/files/accounts_file.csv"
    transactions_file = "tests/files/transactions_file.csv"
    data_handler = DataHandler(users_file, accounts_file, transactions_file)
    test_add_user(data_handler)
    test_load_user(data_handler)

    # test account
    test_add_account(data_handler)
    test_load_account(data_handler)

    # test transaction
    test_add_transaction(data_handler)
    test_load_transaction(data_handler)
    
    test_export_import(data_handler, users_file, accounts_file, transactions_file)
    
   

    
    

if __name__ == "__main__":
    main()

