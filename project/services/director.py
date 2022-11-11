from project.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, pk):
        return self.dao.get_by_id(pk)

    def get_all(self, page_number):
        if page_number is None:
            return self.dao.get_all()

        return self.dao.get_by_page(int(page_number))
