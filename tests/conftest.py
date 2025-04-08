import pytest
from project import app_flask, load_config
from database.models.branches import db

@pytest.fixture(scope="module")
def app():
    "Instance of Main flask app"
    app_flask.config.from_object(load_config)

    with app_flask.app_context():
        db.create_all() 
    
    yield app_flask
    
    with app_flask.app_context():
        db.drop_all()

    return app_flask