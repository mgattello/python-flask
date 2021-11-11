from flask_marshmallow import Marshmallow
import db.models.article

ma = Marshmallow()

class ArticleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = db.models.article
        fields = ("id", "title", "body")