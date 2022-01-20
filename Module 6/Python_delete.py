from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students

student_list = Students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

new_entry = {
    "student_id": "1010",
    "first_name": "Stephen",
    "last_name": "Brown"
}
new_entry_id = Students.insert_one(new_entry).inserted_id
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_entry_id))
student_new_entry = Students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT NEW ENTRY -- ")
print("  Student ID: " + student_new_entry["student_id"] + "\n  First Name: " + student_new_entry["first_name"] + "\n  Last Name: " + student_new_entry["last_name"] + "\n")
deleted_student_new_entry = Students.delete_one({"student_id": "1010"})
new_student_list = Students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  Press any key to Terminate")
