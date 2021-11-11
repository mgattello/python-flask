from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ArticleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)   
    body = db.Column(db.String)

    def __init__(self, title, body):
        self.title = title
        self.body = body