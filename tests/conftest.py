import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.breakfast import Breakfast

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_breakfasts(app):
    breakfast1 = Breakfast(name="Pancakes", rating=3.5, prep_time=20)
    breakfast2 = Breakfast(name="Oatmeal", rating=3, prep_time=15)
    db.session.add_all([breakfast1,breakfast2])










