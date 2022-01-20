from re import search
from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students
student_id = input("Type student ID  ")
get = Students.find_one({"student_id": student_id})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print("  Student ID: " + get["student_id"] + "\n  First Name: " + get["first_name"] + "\n  Last Name: " + get["last_name"] + "\n")
    
input("\n\n  Press any key to Terminate")