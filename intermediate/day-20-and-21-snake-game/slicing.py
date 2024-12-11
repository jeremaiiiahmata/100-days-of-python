piano_list = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]

print("-------LIST")
print(piano_list[2:5]) #Range is from index 2-5 (element in index 5 is not included)
print(piano_list[2:]) #Range is from index 2 to the end
print(piano_list[:5]) #Range is from beginning to index 5 (element in index 5 is not included)
print(piano_list[2:5:2]) #Range from 2-5, but for every 2nd element for each slice.
print(piano_list[::-1]) #Reverses the slice, starts from the end

#Tuple
print("\n-------TUPLE")
print(piano_tuple[2:5]) #Range is from index 2-5 (element in index 5 is not included)
print(piano_tuple[2:]) #Range is from index 2 to the end
print(piano_tuple[:5]) #Range is from beginning to index 5 (element in index 5 is not included)
print(piano_tuple[2:5:2]) #Range from 2-5, but for every 2nd element for each slice.
print(piano_tuple[::-1]) #Reverses the slice, starts from the end