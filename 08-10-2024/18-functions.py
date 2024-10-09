#passare un'informazione alla funzione come argomento

def greet(username):
    print(f"Hi there, {username.title()}!")
    
# greet('Robert')

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~
 
def fav_book(book):
    print("Whats your fav book? ")
    print(f"Oh I love {book.title()}")

# fav_book("Eragon")

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ 

def dog(dog_breed, dog_fur, dog_name):
    print(f"\nI have a {dog_breed.title()}, it has {dog_fur.lower()} hair and its name is {dog_name.title()}!")
    
# dog(dog_breed = 'golden retriever', dog_name = 'maggie', dog_fur = 'curly')
# dog(dog_breed = 'golden retriever', dog_fur =  'straight', dog_name ='alex')
# dog(dog_breed = 'doberman', dog_fur =  'short', dog_name ='asteroid destroyer')

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ 

def formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    return f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"

# user = formatted_name('matteo', 'sala')
# print(user)
# user = formatted_name( 'marco', 'rossi', 'john')
# print(user)

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ 

table = ['paper', 'empty bottle', 'broken pencil', 'tissue', 'myself']
bin = []


def clean_table():
    while table:    
        moving_trash = table.pop()
        bin.append(moving_trash)
        print(f"Moving {moving_trash} to the bin...")

# clean_table()
# print("\nEverything clean.")
# print("Items in the bin:", bin)

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ 

def pizza_builder(*toppings):
    topping_set = set(toppings)
    print('\nMaking a pizza with these toppings:')
    for topping in topping_set:
        print("- " + topping.title())
    
# pizza_builder('mozz', 'pom', 'salam', 'salsicc', 'mozz', 'pom', 'salam', 'salsicc', 'mozz', 'pom', 'salam', 'salsicc')
# pizza_builder('salam', 'salsicc', 'mozz')

# - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ 

def sandwich(*ingredients):
    print(f"\n Preparing a sandwich with these ingredients: ")
    unique_ingredients = set(ingredients)
    for ingr in unique_ingredients:
        print("- " + ingr.title())
    print("\n" + "- ~ " *4)
    print("- ~  Enjoy! ~ -")
    print("- ~ " * 4)
        
sandwich('ham', 'cheese', 'lettuce')    
    