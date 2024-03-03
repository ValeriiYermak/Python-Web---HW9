import argparse
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.hw9

parser = argparse.ArgumentParser(description='Server Authors-Quotes database')
parser.add_argument('--action', help="create, read, update, delete") #CRUD action
parser.add_argument('--id')
parser.add_argument('--quote_text')
parser.add_argument('--author_id')  # ObjectID of the author

args = vars(parser.parse_args())

action = args.get('action')
pk = args.get('id')
quote_text = args.get('quote_text')
author_id = args.get('author_id')

def find():
    return db.quotes.find()

def create(quote_text, author_id):
    r = db.quotes.insert_one({
            'quote_text': quote_text,
            'author_id': ObjectId(author_id),
        })
    return r

def update(pk, quote_text, author_id):
    r = db.quotes.update_one({"_id": ObjectId(pk)}, {
        "$set": {
            'quote_text': quote_text,
            'author_id': ObjectId(author_id),
        }
    })
    return r

def delete(pk):
    r = db.quotes.delete_one({"_id": ObjectId(pk)})
    return r

def main():
    match action:
        case 'create':
            r = create(quote_text, author_id)
            print(r)
        case 'read':
            r = find()
            print([e for e in r])
        case 'update':
            r = update(pk, quote_text, author_id)
            print(r)
        case 'delete':
            r = delete(pk)
            print(r)
        case _:
            print('Unknown action')

if __name__ == '__main__':
    main()
