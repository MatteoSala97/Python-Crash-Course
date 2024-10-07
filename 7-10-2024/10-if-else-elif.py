auto = ["Toyota", "Ford", "Volkswagen", "BMW", "Mercedes-Benz", "Honda", "Nissan", "Audi", "Hyundai", "Chevrolet"]

for item in auto:
    if item.lower().startswith('h'):   #.lower() method converte tutto in minscolo per evitare problemi legati al case sensitive
        print(item.upper())
    elif item.lower().startswith('a'):
        print("Questa è l'unica marca che inizia per a ed è: " + item)
    else: 
        print(item.lower())


# color = 'red'

# if color != 'green':
#     print('Questo è un bel colore')


a = 15
b = 42 
if a > 10 or b == 50:
    print('Almeno una è vera')
else:
    print('Nessuna è vera') 


age = 88

if age <= 5:
    price = 5
    print('Sei molto giovane')
    print('Il biglietto costerà ' + str(price) + "€.") 
elif age < 18:
    price = 10
    print("Ormai sei adolescente quindi il biglietto costerà " + str(price) + "€.")
elif age > 80:
    price = 5
    print('Condizione scontata per gli over 80')
    print('Il biglietto costerà ' + str(price) + "€.") 
else: 
    price = 15
    print('Ormai sei adulto quindi il biglietto costerà ' + str(price) + '€.')
    
    
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings: 
    if requested_topping == 'green peppers':
        print("Sorry, we are out of " + requested_topping + " right now.") 
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

