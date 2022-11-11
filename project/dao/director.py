from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(Director).get(pk)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_page(self, page_numbs):
        pages = self.session.query(Director).paginate(page=page_numbs, per_page=12).items
        return pages
