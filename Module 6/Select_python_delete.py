from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students
student_list = Students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
student_id = input("Type student ID  ")
Students.delete_one({"student_id": student_id})
print("\n  -- Entry has been removed --")
input("\n\n -- Press any key to Terminate --")