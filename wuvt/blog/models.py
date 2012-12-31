import datetime

from wuvt import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    slug = db.Column(db.Unicode, nullable=False)

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    slug = db.Column(db.Unicode, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('category', lazy='dynamic'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('author', lazy='dynamic'))
    datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    content = db.Column(db.UnicodeText)

    def __init__(self, title, slug, category_id, author_id, content):
        self.title = title
        self.slug = slug
        self.category_id = category_id
        self.author_id = author_id
        self.content = content