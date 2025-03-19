from flask import Flask
from database.config.db import db
from database.config.conn import AplicationConfig
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(AplicationConfig)
db.init_app(app)

# with app.app_context():
#     db.create_all()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)