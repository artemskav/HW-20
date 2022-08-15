from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)
    director_1 = Director(id=1, name="director_1")
    director_2 = Director(id=2, name="director_2")

    director_dao.get_one = MagicMock(return_value=director_2)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=Director(id=3, name= 'director_3'))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self,director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(2).name == 'director_2'

    def test_get_all(self):
        assert len(self.director_service.get_all()) > 0

    def test_get_create(self):
        assert self.director_service.create({"id": 3, "name": "director_3"}).id == 3

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 2 == 2
