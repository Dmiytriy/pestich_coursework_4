from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.dao.movie import MovieDAO
from project.services.director import DirectorService
from project.services.genre import GenreService
from project.services.movie import MovieService
from setup_db import db
from dao.user import UserDAO
from services.user import UserService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

