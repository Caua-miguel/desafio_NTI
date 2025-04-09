import pytest
from project import app_flask

@pytest.fixture(scope="module")
def app():
    "Instance of Main flask app"
    return app_flask