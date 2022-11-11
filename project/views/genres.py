from flask import request
from flask_restx import Resource, Namespace

from project.container import genre_service
from project.dao.models.genre import GenreSchema
from project.utils import auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        page_number = request.args.get('page')
        genres = genre_service.get_all(page_number)
        genres_list = GenreSchema(many=True).dump(genres)
        return genres_list, 200


@genre_ns.route('/<int:rid>/')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        certain_genre = genre_service.get_one(rid)
        genre_dict = GenreSchema().dump(certain_genre)
        return genre_dict, 200
