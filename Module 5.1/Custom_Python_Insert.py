from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students

student_id = input("Type student ID  ")
first_name = input("Type students first name  ")
last_name = input("Type students last name  ")
new_student = {
    "student_id": student_id,
    "first_name": first_name,
    "last_name": last_name,
}
print (new_student)
new_student_id = Students.insert_one(new_student).inserted_id
print("Inserted student record for "  +str(first_name)) 
print("into the students collection with document_id " +str(new_student_id))

input("\n\n Press any key to Terminate ")