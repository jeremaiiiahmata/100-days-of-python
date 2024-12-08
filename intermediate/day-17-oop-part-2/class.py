class User :
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 #points to user2, passes the object with these properties  (id, username, followers, following)
        self.following += 1 #points to who owns this method (object 1 - user1)

user1 = User("001", "jeremaiiiah")
user2 = User("002", "asianaathena")
#Currently, we have 2 objects created

print(f"ID: {user1.id}, Name: {user1.username}") #Object 1
print(f"ID : {user2.id}, Name: {user2.username}") #Object 2
# print(f"Followers:  {user1.followers}")

print("\n\n")

print(f"{user1.username} following : {user1.following}, followers : {user1.followers}")
print(f"{user2.username} following : {user2.following}, followers : {user2.followers}")

print("\n\n")

user1.follow(user2) #Calls the follow method in user1 object, passing the parameter of the user2 object
print(f"{user1.username} has followed {user2.username}!")

print("\n\n")

print(f"{user1.username} following : {user1.following}, followers : {user1.followers}")
print(f"{user2.username} following : {user2.following}, followers : {user2.followers}")