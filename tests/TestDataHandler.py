"""This is the Test for the DataHandler Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.utils.data_handler import DataHandler

def main():
    """Main Function"""
    users_file = "tests/files/users_file.csv"
    accounts_file = "tests/files/accounts_file.csv"
    transactions_file = "tests/files/transactions_file.csv"
    data_handler = DataHandler(users_file, accounts_file, transactions_file)
    

if __name__ == "__main__":
    main()

