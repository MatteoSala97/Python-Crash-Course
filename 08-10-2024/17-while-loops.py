def stai_fermo_lì_non_runnare():
    number = 1
    while number <= 20: 
        print(f"{number}")
        number += 1
        
    # uso di un flag per semplificare il while loop facendogli controllare solo il flag e non tutte le condizioni

    prompt = "\nTell me something, and I will repeat it back to you:" 
    prompt += "\nEnter 'quit' to end the program. "
    message = "The program is still running...  "
    message2 = "The program stopped running."
    active = True

    while active:
        message = input(prompt)
        if message. lower() == 'quit': 
            active = False
            print(message2)
        else: 
            print(message)
            
    prompt = "\nEnter your toppings (type 'done' when you're done): "
    toppings = []

    while True: 
        topping = input(prompt).lower()
        if topping != 'done':
            toppings.append(topping)
        else: 
            break
        
    print("You have chosen the following toppings:", toppings)
                

    # Verify each user until there are no more unconfirmed users. 
    #  Move each verified user into the list of confirmed users.
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []

    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
        
    # Display all confirmed users.
    print("\nThe following users have been confirmed:") 
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

# filling a dictionary with user input ( fatto anche nel file precedente ma con una lista)
responses = {}
active_polling= True

while active_polling:
    name = input("\nWhat's your full name?")
    res = input("\nWould you like to climb someday?")
    #salva lo user input
    responses[name] = res
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no': 
        active_polling = False
        
print("\n--- Poll Results ---")
print("\nResponses collected:")
for name, reponse in responses.items():
    print(f"{name}: {reponse}")
