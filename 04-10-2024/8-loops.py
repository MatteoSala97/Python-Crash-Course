# Pizzas: Think of at least three kinds of your favorite pizza . Store these pizza names in a list, and then use a for loop to print the name of each pizza .
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza . For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza .
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza . The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizza=['diavola', 'capricciosa', 'margherita', 'boscaiola']

for item in pizza:
    print("Mi piace molto la " + item)

print("\t Mi piace molto la pizza.")

#range
for value in range(1,10):
    print(value)
    
odd_numbers = list(range(1,30,2))
print(odd_numbers)

squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)


#pizza loops

my_pizzas = ["Margherita", "Pepperoni", "Quattro Stagioni", "Diavola", "Funghi e Prosciutto", "Capricciosa", "Ortolana", "Hawaiiana"] #"Bianca", "Napoli"
friends_pizzas = []

my_pizzas.append("Bianca")
friends_pizzas.append("Hawaiiana")

print("Le mie pizze sono:")
for mypiz in my_pizzas:
    print('- ' + mypiz)

