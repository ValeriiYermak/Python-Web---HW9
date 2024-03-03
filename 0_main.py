from pymongo import MongoClient
from mongoengine import connect
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
db = client.hw9

# Load data from authors.json
with open("authors.json", 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

# Load data from quotes.json
with open("quotes.json", 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)

try:
    # Insert data into authors collection
    db.authors.insert_many(authors_data)
except Exception as e:
    print(f"Error inserting authors data: {e}")

try:
    # Insert data into quotes collection
    db.quotes.insert_many(quotes_data)
except Exception as e:
    print(f"Error inserting quotes data: {e}")
