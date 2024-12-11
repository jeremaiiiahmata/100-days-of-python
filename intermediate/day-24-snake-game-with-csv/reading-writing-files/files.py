# ----- Reading File
# with open("text-file.txt") as file :
# print(file)
#
# content = file.read() # Returns the content of the file as a string
# print(content)
#
# file.close() #Closes the file, we need to close it because it takes up resources in the computer.

# ----- Writing File
with open("text-file.txt", mode="w") as file : #the 'file' will be the variable
    print(file)

    file.write("Hello, this is a text! ")

# ----- Appending a File
with open("text-file.txt", mode="a") as file : #the 'file' will be the variable, mode is append (a)
    print(file)

    file.write("I have appended this text.")