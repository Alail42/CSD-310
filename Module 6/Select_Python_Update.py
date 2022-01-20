from ast import And
from tkinter.messagebox import YES
from xmlrpc.client import boolean
from pymongo import MongoClient

url = "mongodb+srv://admin:ADMIN123@cluster0.jklpw.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
Students = db.Students
student_id = input("Type student ID  ")
get = Students.find_one({"student_id": student_id})
tracker = get ["_id"]
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print("  Student ID: " + get["student_id"] + "\n  First Name: " + get["first_name"] + "\n  Last Name: " + get["last_name"] + "\n")

bool = input("Would you like to change student ID?  ")
if  bool==YES:new_student_id = input("Type new student ID  ");Students.update_one({"_id": tracker}, {"$set": {"student_id": new_student_id}})
pass
bool = input("Would you like to change first name?  ")
if  bool==YES:new_first_name = input("Type new first name?  ");Students.update_one({"_id": tracker}, {"$set": {"first_name": new_first_name}})
pass
bool = input("Would you like to change last name?  ")
if  bool==YES:new_last_name = input("Type new last name  ");Students.update_one({"_id": tracker}, {"$set": {"last_name": new_last_name}})   
pass

get = Students.find_one({"_id": tracker})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print("  Student ID: " + get["student_id"] + "\n  First Name: " + get["first_name"] + "\n  Last Name: " + get["last_name"] + "\n")

input("\n\n  -- Press any key to Terminate --")