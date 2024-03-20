from bson import json_util
from mongoengine import connect, BooleanField, Document, StringField, ReferenceField, ListField, CASCADE

connect(host="mongodb+srv://afrodita69:12345@cluster0.dlq3iss.mongodb.net/test?retryWrites=true&w=majority", ssl=True)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=15))
    quote = StringField()
    meta = {"collection": "quotes"}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    message_sent = BooleanField(default=False)
