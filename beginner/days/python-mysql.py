import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="students"
)

print("Database running...")

cursor = mydb.cursor()
print("\nCursor initialized.")

cursor.execute("SELECT * FROM students_table")
print("\nSelecting all students from the students_table")

students = cursor.fetchall() #Fetches all the data in students

print("[1]. Insert a student")
print("[2]. View all students")

choice = int(input("\nEnter your choice."))

if choice == 1 :
    name
print("\n-----------------------STUDENTS-----------------------")
for student in students :
    print(student)
print("--------------------------------------------------------")


