from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://joshuahawke:R74RGtdiCDBbcqIa0B9oIukNWMulWM3T@dpg-chnno0m4dad1d57938d0-a.ohio-postgres.render.com/esports_rw32"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
app.json.compact = False
db = SQLAlchemy(metadata=MetaData())
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)