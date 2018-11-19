import datetime

from peewee import *

db = SqliteDatabase('posts.db')

class Post(Model):
    uid = CharField(unique=True)
    title = TextField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Review(Model):
    post = ForeignKeyField(Post, related_name='review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta():
        database = db

def initialize():
    db.connect()
    db.create_tables([Post, Review], safe=True)
    db.close()