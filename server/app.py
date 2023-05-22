from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# app.json_encoder.compact_json = not app.config['JSONIFY_PRETTYPRINT_REGULAR']

from models import *
from routes import *

if __name__ == '__main__':
    app.run()
