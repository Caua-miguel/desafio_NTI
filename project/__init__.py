from flask import Flask
from database.models.branches import db
from database.config.conn import AplicationConfig
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(AplicationConfig)
db.init_app(app)

migrate = Migrate(app, db)

from project.controllers.branches_controller import branches_blueprint

app.register_blueprint(branches_blueprint)
