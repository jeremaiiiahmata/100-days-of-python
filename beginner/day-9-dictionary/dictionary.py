dictionary = {
    "Name" : "Jerem",
    "Age" : 12,
    "Gender" : "Male"
}

print(f"My name is {dictionary['Name'] } and I'm {dictionary['Age']} years old")

#Adding a new entry in the dictionary
dictionary["Hobbies"] = "Dogs, Basketball, Video Games"


#Editing an existing entry in the dictionary
dictionary["Age"] = 21

#Loop through a dictionary
for thing in dictionary:
    print("\n")
    print(thing) # Just returns the key
    print(dictionary[thing]) # Returns the value

print("\n\nResetting dictionary...")
#Resets a dictionary
dictionary = {}

print(f"Dictionary : {dictionary}")

