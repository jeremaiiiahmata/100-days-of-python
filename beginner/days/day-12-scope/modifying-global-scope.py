enemies = 1

def increaseEnemies() :
    global enemies

    print(f"Enemies inside function : {enemies}")

    return enemies + 1

increaseEnemies()
print(f"Enemies outside function : {enemies}")
print(f"Enemies after calling increaseEnemies function : {increaseEnemies()}")

#BEST WAY TO MODIFY GLOBAL SCOPE

print("*******************************************************************")

def addEnemies(enemy):

    print(f"Enemies inside the addEnemies function : {enemy}")

    return enemy + 1

enemies = addEnemies(enemies)
print(f"Enemies after calling the addEnemies function : {enemies}")