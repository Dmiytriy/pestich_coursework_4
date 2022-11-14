import base64
import hashlib
import hmac


from project.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from project.dao.user import UserDAO



class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_name(self, username):
        return self.dao.get_by_name(username)

    def delete_user(self, uid):
        self.dao.delete_user(uid)

    def update_user(self, data):

        self.dao.update_user(data)

    def update_password(self, data):

        self.dao.update_password(data)

    def get_all(self):
        return self.dao.get_all()

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def create_user(self, data):
        password = data.get('password')
        hashed_password = self.get_hash(password)
        data['password'] = hashed_password

        return self.dao.create_user(data)

    def get_hash(self, password):
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hashed_password)




