"""This is the AuthController Module"""
__author__ = "7157747, Gellien, 8425470, Heidusch"


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
        
        
        
        
        
