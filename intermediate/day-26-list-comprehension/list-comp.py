# newList = [newItem for item in list]  # List Comprehesion
#
# Equivalent (if we're using for-loop)
# numbers = [1, 2, 3]
# newList = []
# for n in numbers:
#     add = n + 1
#
# newList.append(add)
#
# newList = [n + 1 for n in numbers]

newRange = [n * 2 for n in range(1,5)]
print(newRange)

#---- CONDITIONAL LIST COMPREHENSION

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

longNames = [name.upper() for name in names if len(name) > 5]
print(names)
print(longNames)