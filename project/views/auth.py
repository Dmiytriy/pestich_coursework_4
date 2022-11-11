from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.services.authentification import generate_tokens, examination_refresh_token

auth_ns = Namespace('auth')


@auth_ns.route("/register/")
class RegisterView(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            return ' ', 400

        user_service.create_user(data)

        return '', 201


@auth_ns.route("/login/")
class LoginView(Resource):
    def post(self):
        data = request.json

        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            return ' ', 400

        tokens = generate_tokens(email, password)

        if not tokens:
            return ' ', 401

        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')

        tokens = examination_refresh_token(refresh_token)

        return tokens, 201
