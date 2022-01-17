from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

Richard = {
    "student_id": "1007",
    "first_name": "Richard",
    "last_name": "Grayson",
}
Jason = {
    "student_id": "1008",
    "first_name": "Jason",
    "last_name": "Todd",
}
Tim = {
    "student_id": "1009",
    "first_name": "Tim",
    "last_name": "Drake",
}

Students = db.Students

print("\n  -- INSERT STATEMENTS --")
Richard_student_id = Students.insert_one(Richard).inserted_id
print("  Inserted student record Richard Graysons into the students collection with document_id " + str(Richard_student_id))

Jason_student_id = Students.insert_one(Jason).inserted_id
print("  Inserted student record Jason Todd into the students collection with document_id " + str(Jason_student_id))

Tim_student_id = Students.insert_one(Tim).inserted_id
print("  Inserted student record Tim Drake into the students collection with document_id " + str(Tim_student_id))

input("\n\n Press any key to Terminate ")