"""This is the Test for the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.utils.data_handler import DataHandler
from src.models.user import User
from src.models.account import Account
from src.models.user_role import UserRole


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
    user = data_handler.load_data("user", "franz")
    assert data_handler.load_data("user", "franz") == user
    print("Test load_account has passed")



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
    data_handler.import_from_csv()


    assert data_handler.load_data("user", "franz").username == "franz"
    user = data_handler.load_data("user", "franz")
    assert data_handler.load_data("user", "franz") == user


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

    test_export_import(data_handler, users_file, accounts_file, transactions_file)
    
   

    
    

if __name__ == "__main__":
    main()

