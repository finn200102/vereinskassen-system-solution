"""This is the AuthController Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"
from src.models.user_role import UserRole


class AuthController():
    """This is the AuthController Class."""
    def __init__(self, data_handler):
        """This initializes the AuthController Class."""
        self.data_handler = data_handler

    def check_password(self, username, password):
        """Return true if password is right"""
        user = self.data_handler.load_data("user", username)
        if user:
            if user.authenticate(password):
                return True
        else:
            print(f"The user {username} does not exist!")
            return None

    def login(self, username, password):
        """Log into the user"""
        if self.check_password(username, password):
            user = self.data_handler.load_data("user", username)
            return user.role
        else:
            return False

    def get_user_roles():
        """Return list of userroles"""
        user_role = UserRole()
        return [user_role.admin, user_role.treasurer, user_role.referee]
        
        
        
        
        
