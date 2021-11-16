from flask import Flask
from abc import *
import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
sqldir = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']=sqldir
# Silence the FSADeprecationWarning and save resource
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'


db = SQLAlchemy(app)
ma = Marshmallow(app)


class ArticleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)   
    body = db.Column(db.String)

    def __init__(self, title, body):
        self.title = title
        self.body = body

class ArticleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ArticleModel
        fields = ("id", "title", "body")

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# Note: db.create_all() uses the same instance of db that is being used to define the models.
# do not try to separate the schemas and models in other modules. 
# Otherwise SQLAlchemy would return: sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table
db.create_all()
