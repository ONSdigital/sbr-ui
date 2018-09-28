from flask_login import UserMixin


users = []  # This is temporary


class User(UserMixin):

    def __init__(self, user_id, token, role):
        self.id = user_id
        self.token = token
        self.role = role
