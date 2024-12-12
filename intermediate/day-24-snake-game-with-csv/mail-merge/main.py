PLACEHOLDER = "[name]"

with open("./input/letters/email-template.txt") as file: #Gets the email template
    messageTemplate = file.read()

with open("./input/names/names-list.txt") as file : #Gets the name list and formats it in a list type.
    namesList = file.readlines()

for name in namesList : #Access each name in the list and per list :
    formattedName = name.strip() #removes any whitespaces in the name
    messageWithName = messageTemplate.replace(PLACEHOLDER, formattedName) #Replaces the placeholder [name] in the email template with the name

    with open(f"./output/ready-to-send/for-{formattedName}.txt", mode="w") as file: #Writes the .txt file in the output folder
        file.write(messageWithName)

print("Templates has been successfully created!")
