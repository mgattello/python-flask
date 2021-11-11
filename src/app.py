from flask import Flask, request, render_template, g
from abc import *
import os

from db.models.article import db, ArticleModel
from db.schemas.article import ma, ArticleSchema

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
sqldir = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'db.sqlite')
# Silence the FSADeprecationWarning and save resource
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'

# Database
db.init_app(app)
ma.init_app(app)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# TODO: this interface created confusion (name mangling). Not sure I want to keep it.
# class IDB(ABC):    
#     @abstractmethod
#     def add(self):
#         pass
    
#     @abstractmethod
#     def delete(self):
#         pass
    
#     @abstractmethod
#     def commit(self):
#         pass

#     @abstractmethod
#     def query(self):
#         pass

class SQLAlchemyDB():
    def __init__(self, db):
        self.database = db

    # TODO: change title, body to single arg
    def _commit(self, type, title, body):
        if not type:
            return 'fail'
        if(type == 'add'):
            # TODO: decouple ArticleModel from SQLAlchemyDB: this might not be possible because of how SQLAlchemy works.
            data = ArticleModel(title, body)
            db.session.add(data)
        # TODO: WIP not yet tested with new design.
        # if(type == 'delete'):
        #     self.database.session.delete(data)
        try:
            db.session.commit()
            return 'success'
        except:
            return 'fail'
    # TODO: WIP not yet tested with new design.
    # def _query(self, model, schema, id):
    #     if(id):
    #         result = model.query.filter_by(id=id).first()
    #         return schema.dumps(result)
        
    #     results = model.query.all()
    #     return schema.dumps(results)

    # TODO: WIP not yet tested with new design.
    # def get(self, model, schema, by_id = ''):
    #     return self._query(model, schema, by_id)

    def post(self, title, body):
        # TODO: change title, body to single arg
        self._commit('add', title, body)
        return self.posted(title, body)
    
    # TODO: WIP not yet tested with new design.
    # def delete(self, model, schema, by_id):
    #     data = self._query(model, schema, by_id)
    #     self._commit('delete', data)
    #     return data
    
    # TODO: this function might change or be deleted.
    def posted(self, title, body):
        model = ArticleModel(title, body)
        # TODO: article_schema should be passed as arg if possible.
        return article_schema.dumps(model)

class HelloWorld():
    def get(self):
        return 'Hello World!'

class Article(SQLAlchemyDB):
    def __init__(self, db = []):
        super(Article, self).__init__(db)

    # TODO: WIP not yet tested with new design.
    # def read(self, article_id):
    #     try:
    #         return self.get(article_id)
    #     except IndexError:
    #         return self.errorMessage()
    def create(self, title, body):
        try:
            # TODO: change title, body to single arg
            return self.post(title, body, article_schema)
        except Exception as err:
            print(err)

    # TODO: WIP not yet tested with new design.
    # def cancel(self, article_id):
    #     return self.delete(ArticleModel, article_schema, article_id)

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
    return g.table.post(title, body)

@app.route('/articles', methods=['GET'])
def get_articles():
    return g.table.read()

@app.route('/article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    return g.table.read(article_id)
    
@app.route('/article', methods=['DELETE'])
def delete_article():
    article_id = request.json['id']
    return g.table.cancel(article_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('src/templates/error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)