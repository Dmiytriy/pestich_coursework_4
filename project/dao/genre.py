from project.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(Genre).get(pk)

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_page(self, page_numbs):
        pages = self.session.query(Genre).paginate(page=page_numbs, per_page=12).items
        return pages
