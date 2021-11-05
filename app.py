from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hello World!'

class Article(Resource):
    def __init__(self, db = []):
        self.db = db

    def get(self, article_id = 'all'):
        if article_id == 'all':
            return self.getAll(self.db)
        try:
            return self.db[article_id]
        except IndexError:
            return self.errorMessage()
    
    def getAll(self, db_articles = [], limit = 10):
        self.db_articles = db_articles
        self.limit = limit

        if len(self.db_articles) > limit:
            split_result = self.db_articles[:limit]
            return split_result

        return self.db_articles

    # def limit_get_result(self):

    def errorMessage(self):
        return {'error': 'not found'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()  # run our Flask app