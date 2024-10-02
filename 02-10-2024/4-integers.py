age= 27 
msg="I am " + str(age) + " years old."

print(msg)

#Store your favorite number in a variable . Then, using that variable, create a message that reveals your favorite number . Print that message .
fav=str(42)

#print(fav)

# chiedere all'utente di indovinare un numero 
user_input=input("What number are you thinking about?")

print("Your are thinking about the number " + user_input)

if user_input == fav:
    print("This is the correct answer to the Ultimate Question of Life, the Universe, and Everything")
elif user_input > str(70):
    print("You're way too far")
elif user_input > str(45):
    print("Getting closer...")
elif user_input < str(40):
    print("Nah, too low")