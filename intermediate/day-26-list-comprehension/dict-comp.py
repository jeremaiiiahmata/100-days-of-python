import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

#---- Creating new dictionary from a list
studentsScores = {student:random.randint(1,100) for student in names}
print(studentsScores)

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