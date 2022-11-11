from project.dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, pk):

        return self.dao.get_by_id(pk)

    def get_all(self, filters):
        if filters.get('status') is None and filters.get('page') is None:
            return self.dao.get_all()

        return self.dao.get_with_filters(filters)
