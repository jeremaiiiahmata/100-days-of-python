alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 26
isStillUsing = True



def encode(shift, message) :
    encodedMessage = ""

    for letter in list(message) :
        newPosition = alphabet.index(letter) + shift#index holds the current position of the letter in alphabet list

        if newPosition > 25 :
            newPosition = newPosition - 26

        encodedMessage += alphabet[newPosition] #letter will be replaced by whatever the position of the new index is in the alphabet list.

    print(f"Encoded Message : {encodedMessage}") #Prints the full message, encoded.



def decode(shift, message) :
    decodedMessage = ""

    for letter in list(message) :
        newPosition = alphabet.index(letter) - shift #index holds the current position of the letter in alphabet list

        if newIndex < 0 :
            newIndex = newIndex + 26

        decodedMessage += alphabet[newIndex] #letter will be replaced by whatever the position of the new index is in the alphabet list.

    print(decodedMessage)


while isStillUsing :
    print("Welcome to Caesar Cipher")
    choice = str(input("Encode or Decode?\nTo exit type 'exit'\nEnter choice : "))

    if choice.lower() == "exit":
        isStillUsing = False

    message = input("Enter your message : ")
    shift = int(input("How many shift?"))

    if choice.lower() == "encode":
        encode(shift, message)
    elif choice.lower() == "decode" :
        decode(shift, message)

