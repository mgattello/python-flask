from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('task')

class HelloWorld(Resource):
    def get(self):
        return 'Hello World!'

class Article(Resource):
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

    def errorMessage(self):
        return {'error': 'not found'}

api.add_resource(HelloWorld, '/')
api.add_resource(Article, '/articles')

if __name__ == '__main__':
    app.run(debug=True)