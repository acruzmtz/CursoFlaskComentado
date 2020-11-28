from flask_login import UserMixin
from .firebase_service import get_user

class UserData():

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserLogin(UserMixin):

    def __init__(self, data_user):
        self.id = data_user.username
        self.password = data_user.password

    @staticmethod
    def query(user_id):

        user_doc = get_user(user_id)
        user_data = UserData(
            username = user_doc.id,
            password = user_doc.to_dict()['password']
        )

        return UserLogin(user_data)
