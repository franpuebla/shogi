import flask
import flask_sqlalchemy
from datetime import datetime
from api import app


db = flask_sqlalchemy.SQLAlchemy()

class Model(object):
    """
    Model
    **Overview**

    Used to generalize attributes and methods for all models package.
    Also create sqlalchemy object and then initiated from create_app().
    """
    id = db.Column(db.Integer, primary_key=True)
