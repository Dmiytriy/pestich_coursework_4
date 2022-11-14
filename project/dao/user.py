from project.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):

        return self.session.query(User).get(pk)

    def get_all(self):

        return self.session.query(User).all()

    def create_user(self, data):
        user_new = User(**data)

        self.session.add(user_new)
        self.session.commit()

        return user_new

    def delete_user(self, user_id):
        user = self.get_one(user_id)

        self.session.delete(user)
        self.session.commit()

    def get_user_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).one_or_none()

        return user

    def get_by_name(self, username):
        user = self.session.query(User).filter(User.username == username).first()

        return user

    def update_user(self, data):
        user = self.get_user_by_email(data.get('email'))

        user.name = data.get('name')
        user.surname = data.get('surname')
        user.favorite_genre_id = data.get('favorite_genre_id')

        self.session.add(user)
        self.session.commit()

    def update_password(self, user):


        self.session.add(user)
        self.session.commit()
