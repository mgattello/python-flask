# import requests

# BASE = "http://127.0.0.1:5000/"
# data = {
#     'id': 1,
#     'title': 'Test',
#     'body': 'this is my article'
# }

# response = requests.put(BASE + "articles/" + str(data))
# print(response.json)

# input()
# response = requests.get(BASE + "articles/")
# print(response.json)

def test_get_article_from_db(self):
    db_connect = Article(ArticleModel.query.all())
    self.assertEqual(len(db_connect.get()), 3)

    expected = {"id": 1}
    self.assertEqual(json.loads(db_connect.get(0)), expected)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username