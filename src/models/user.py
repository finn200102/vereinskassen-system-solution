"""This is the Model for the User class"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.user_role import UserRole

class User():
    """The User class."""
    def __init__(self, username: str, password: str, role: str, department: str):
        """
        Initializes the User Class.

        Args:
            username(str): The username
            password(str): The unhashed password
            role(str): The UserRole
            department(str): The department of the user
        """
        self.username = username
        self.password = password
        self.role = role
        self.department = department

    def authenticate(self, password: str) -> bool:
        """
        Authenicte the user, no hash.

        Args:
            password(str): The password string
        """
        return password == self.password

    def has_permission(action: str) -> bool:
        """
        Check if user has permissionf or action.

        Args:
            action(str): The action
        """
        pass
