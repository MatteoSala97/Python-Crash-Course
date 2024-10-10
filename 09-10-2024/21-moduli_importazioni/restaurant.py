class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.tables =  0

    def describe_restaurant(self):
        print(f"This is the {self.restaurant_name.title()} restaurant and they serve {self.cuisine_type}.")
        
    def open_restaurant(self):
        print("The restaurant is open.")
        
    # argomento e metodo messi per poter asssegnare un valore a add tables direttamente come numero da al richiamo della funzione
    def get_tables(self, number):
        self.tables += number 
        print(f"This restaurant currently has {self.tables} tables.")
    
    
    
   
restaurant= Restaurant('da mario', 'meat')

restaurant.describe_restaurant()
restaurant.open_restaurant()

# restaurant1= Restaurant('Leaf', 'vegan')
# restaurant2= Restaurant('Boat', 'fish')

restaurant.describe_restaurant()

restaurant.get_tables(10)



#- ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~
