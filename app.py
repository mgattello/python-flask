from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'db.sqlite')
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

class HelloWorld():
    def get(self):
        return 'Hello World!'

class Article():
    def __init__(self, db = []):
        self.db = db

    def get(self, article_id = 'all'):
        if article_id == 'all':
            return self.getAll()
        try:
            return self.db[article_id]
        except IndexError:
            return self.errorMessage()
    
    def getAll(self, limit = 10):   
        if len(self.db) > limit:
            split_result = self.db[:limit]
            return split_result
        return self.db

    def post(self, article_title, article_body):
        # TODO: exe. article id taken 409
        new_article = {
            'title': article_title,
            'body': article_body
        }

        return new_article

    def errorMessage(self):
        return {'error': 'not found'}

@app.route('/', methods=['GET'])
def hello_world():
    res = {"hello": "world"}
    return res

@app.route('/article', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    new_article = ArticleModel(title, body)
    
    db.session.add(new_article)
    db.session.commit()

    return article_schema.dumps(new_article)

if __name__ == '__main__':
    app.run(debug=True)