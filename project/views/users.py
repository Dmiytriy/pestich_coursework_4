from flask import request, abort
from flask_restx import Resource, Namespace

from project.container import user_service
from project.dao.models.user import UserSchema
from project.services.authentification import get_email_from_header, change_the_password
from project.utils import auth_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/<username>")
class UserViews(Resource):
    @auth_required
    def get(self):
        req_header = request.headers['Authorization']

        email = get_email_from_header(req_header)

        if not email:
            abort(401)

        certain_user = user_service.get_user_by_email(email)

        return user_schema.dump(certain_user), 200

    @auth_required
    def delete(self, username):
        user_service.delete_user(username)
        return ' ', 200

    @auth_required
    def patch(self):
        req_header = request.headers['Authorization']

        email = get_email_from_header(req_header)

        if not email:
            abort(401)

        req_data = request.json

        if not req_data:
            abort(401)

        req_data['email'] = email

        user_service.update_user(req_data)

        return ' ', 201


@user_ns.route("/password/")
class UserPassViews(Resource):
    @auth_required
    def put(self):
        password_1 = request.json.get('password_1')
        password_2 = request.json.get('password_2')
        header = request.headers['Authorization']
        email = get_email_from_header(header)

        return change_the_password(email, password_1, password_2)

