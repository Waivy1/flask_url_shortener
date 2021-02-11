from ..main import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class URLShortner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    shorted_url = db.Column(db.String(200), nullable=False)

    @classmethod
    def save_shorted_url(cls, url):
        table = cls(url=url, shorted_url=url)

        db.session.add(table)
        db.session.commit()

    @classmethod
    def get_url(cls, shorted_url):
        table = cls.query.filter_by(shorted_url=shorted_url).first()

        return table