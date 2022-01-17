from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print("\n -- pytech collection List --")
print(db.list_collection_names())
input("\n\n  Press any key to Terminate")
