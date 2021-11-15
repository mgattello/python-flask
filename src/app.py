from flask import Flask, request, render_template, g
import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
sqldir = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']=sqldir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False' # Silence the FSADeprecationWarning and save resource

# Database
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ArticleModel(db.Model):
    __tablename__ = 'article_model'
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

class SQLAlchemyDB():
    def __init__(self, db):
        self.database = db

    def _commit(self, type, model):
        if not type:
            return 'fail'
        if(type == 'add'):
            self.database.session.add(model)
        if(type == 'delete'):
            self.database.session.delete(model)
        try:
            self.database.session.commit()
            return 'success'
        except:
            return 'fail'

    def _query(self, model, schema, id = ''):
        if(id):
            query = model.query.filter_by(id=id).first()
            return self.serialised(query, schema)
        
        query = model.query.all()
        return self.serialised(query, schema)

    def post(self, model, schema):
        self._commit('add', model)
        return self.serialised(model, schema)
    
    def delete(self, model):
        self._commit('delete', model)
        return self.serialised(model, article_schema)
        
    def serialised(self, model, schema):
        return schema.dumps(model)

class HelloWorld():
    def get(self):
        return 'Hello World!'

class Article(SQLAlchemyDB):
    def __init__(self, db = []):
        super(Article, self).__init__(db)

    def read(self, article_id = ''):
        try:
            if(article_id):
                return self._query(ArticleModel, article_schema, article_id)
            return self._query(ArticleModel, articles_schema)
        except IndexError:
            return self.errorMessage()

    def create(self, title, body):
            model = ArticleModel(title, body)
            return self.post(model, article_schema)

    def cancel(self, article_id):
        # query = self._query(ArticleModel, article_schema, article_id)
        query = ArticleModel.query.filter_by(id=article_id).first()
        return self.delete(query)

    def errorMessage(self):
        return {'error': 'not found'}
            
@app.before_first_request
def setup():
    if 'table' not in g:
        g.table = Article(db)
    return g.table

@app.route('/', methods=['GET'])
def hello_world():
    res = {"hello": "world"}
    return res

@app.route('/article', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    return g.table.create(title, body)

@app.route('/articles', methods=['GET'])
def get_articles():
    return g.table.read()

@app.route('/article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    return g.table.read(article_id)
    
@app.route('/article/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    return g.table.cancel(article_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('/src/templates/error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)