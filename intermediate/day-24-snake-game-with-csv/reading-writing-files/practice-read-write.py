from Tools.demo.mcast import receiver

username = input("Hello! Enter your name : ")
message = input("Enter your message: \n")
recipient = input("To whom you want to send this message to : ")

with open(f"To {recipient}.txt", mode="a") as file:

    file.write(f"{message}\n\nFrom: {username}")
