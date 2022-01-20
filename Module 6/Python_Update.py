from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students

student_list = Students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

result = Students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Wayen"}})

Richard = Students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("  Student ID: " + Richard["student_id"] + "\n  First Name: " + Richard["first_name"] + "\n  Last Name: " + Richard["last_name"] + "\n")

input("\n\n  -- Press any key to Terminate --")
