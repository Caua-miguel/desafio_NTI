from flask import Flask
from database.models.branches import db
from project.config.setup import setup
from flask_migrate import Migrate

app_flask = Flask(__name__)

load_config = setup()
app_flask.config.from_object(load_config)
db.init_app(app_flask)

migrate = Migrate(app_flask, db)

from project.controllers.branches_controller import branches_blueprint

app_flask.register_blueprint(branches_blueprint)
