from logging import error
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hello World!'

db_articles = ['article_1', 'article_2', 'article_3']

class Article(Resource):

    def get(self, article_id = 'all'):
        if article_id == 'all':
            return db_articles
        try:
            return db_articles[article_id]
        except IndexError:
            return self.errorMessage()

    def errorMessage(self):
        return {'error': 'not found'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()  # run our Flask app