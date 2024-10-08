def stai_fermo_li_non_runnare():
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
        
