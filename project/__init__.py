from flask import Flask
from database.models.branches import db
from project.config.setup import setup
from flask_migrate import Migrate

app = Flask(__name__)

load_config = setup()
app.config.from_object(load_config)
db.init_app(app)

migrate = Migrate(app, db)

from project.controllers.branches_controller import branches_blueprint

app.register_blueprint(branches_blueprint)
