from mongoengine import connect, Document, StringField, \
    ReferenceField, ListField, CASCADE
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
db = client.hw9


connect(
    db="hw9",
    host="mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/")


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    quote = StringField()
    meta = {"collection": "quotes"}
