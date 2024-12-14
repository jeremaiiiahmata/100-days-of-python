import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

#---- Creating new dictionary from a list
studentsScores = {student:random.randint(1,100) for student in names} #Gives each student a random grade
print(f"Student scores :{studentsScores}")

#Loops through each row of the studentsScore and creates a new dictionary for those whose grades are greater than 75
passedStudents = {student : score for (student, score) in studentsScores.items() if score > 75}
print(passedStudents)

studentDict = {
    "student" : ["Angela","James","Lily"],
    "score" : [56,76,98]
}

passedStudentsDF = pandas.DataFrame(studentDict)
print(passedStudentsDF)

for(index, row) in passedStudentsDF.iterrows():
    print(row.student) #Prints the list of students
    print(row.score) #Prints the list of scores