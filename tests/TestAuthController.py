"""This is the TestAuthController Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.controllers.auth_controller import AuthController
from src.utils.data_handler import DataHandler
from src.models.user_role import UserRole
from src.models.user import User

def test_check_password():
    """Test the check password method."""
    users_file = "tests/files/users_file.csv"
    accounts_file = "tests/files/accounts_file.csv"
    transactions_file = "tests/files/transactions_file.csv"
    data_handler = DataHandler(users_file, accounts_file, transactions_file)
    user = User("hanz", "1234", UserRole.admin, "sport")
    data_handler.save_data(user)
    auth_controller = AuthController(data_handler)
    log = auth_controller.check_password("hanz", "1234")
    assert log == True
    print("Check password test has passed.")


def test_login():
    """Test the login method"""
    users_file = "tests/files/users_file.csv"
    accounts_file = "tests/files/accounts_file.csv"
    transactions_file = "tests/files/transactions_file.csv"
    data_handler = DataHandler(users_file, accounts_file, transactions_file)
    user = User("hanz", "1234", UserRole.admin, "sport")
    data_handler.save_data(user)
    auth_controller = AuthController(data_handler)
    log = auth_controller.login("hanz", "1234")
    assert log == user.role
    print("Login test has passed.")
    

def main():
    """This is the main function."""
    test_check_password()
    test_login()

if __name__ == "__main__":
    main()
