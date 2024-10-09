# input = input("Enter your name:")
# print(f"Hello {input}, how are you today?")

prompt = "Do you like programming? I really hope you like it because you embarked on a very very very looooooooooooooong journey: " 
prompt += "\n(yes/no)"

question = input(prompt)

print(f"{question}")

if question == "yes" or question == "yes" or question == "y":
    print("That's awesome! I'm sure it's going to be fun and rewarding.")
else:
    print("I'm sorry to hear that. But don't worry, there are many great programming languages out there.")
    
# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like . Print a message about that car, such as “Let me see if I can find you a Subaru .”
# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group . If the answer is more than eight, print a message say-ing they’ll have to wait for a table. Otherwise, report that their table is ready . 
# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .

car_input = input("What kind of rental car would you like? ")
print(f"Let me see if I can find a {car_input.title()} that suits your expectations.")


table_input = input("How many people are in your group?")
if int(table_input) > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
    
    
number_input = input("Enter a number: ")
if int(number_input) % 10: 
    print("The number is not a multiple of 10.")
else:
    print("The number is a multiple of 10.")
    
