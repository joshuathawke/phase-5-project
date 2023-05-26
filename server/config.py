from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///esports.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
app.json.compact = False
db = SQLAlchemy(metadata=MetaData())
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)