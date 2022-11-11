from flask import request
from flask_restx import Resource, Namespace

from project.container import movie_service
from project.dao.models.movie import MovieSchema
from project.utils import auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        status = request.args.get('status')
        page_number = request.args.get('page')

        filters = {
            "status": status,
            "page": page_number
        }

        movies = movie_service.get_all(filters)
        movies_list = MovieSchema(many=True).dump(movies)
        return movies_list, 200


@movie_ns.route('/<int:bid>/')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        certain_movie = movie_service.get_one(bid)
        movie_dict = MovieSchema().dump(certain_movie)
        return movie_dict, 200