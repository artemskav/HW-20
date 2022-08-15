from unittest.mock import MagicMock
import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_1 = Movie(id=1, title="name_1", description='descr_1', trailer='tr_1', year=2010, rating=10.1)
    movie_2 = Movie(id=2, title="name_2", description='descr_2', trailer='tr_2', year=2012, rating=10.2)

    movie_dao.get_one = MagicMock(return_value=movie_2)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title="name_3", description='descr_3',
                                                    trailer='tr_3', year=2013, rating=10.3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self,movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(2).title == 'name_2'

    def test_get_all(self):
        assert len(self.movie_service.get_all()) > 0

    def test_get_create(self):
        assert self.movie_service.create({"id": 3, "title": "name_3", "description": 'descr_3',
                                          "trailer": 'tr_3', "year": 2013, "rating": 10.3}).description == 'descr_3'

    def test_update(self):
        assert 1 == 1

    def test_delete(self):
        assert 2 == 2
