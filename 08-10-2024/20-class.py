import datetime
class Cat():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def meow(self):
        print(f"{self.name.title()} is {self.breed.title()} and it's now meowing.")
        
    def grooming(self):
        now = datetime.datetime.now()
        
        groom_day = now.strftime('%A')
        groom_time = now.strftime('%H:%M')
        print(f"{self.name.title()} is a {self.breed.title()} and it's cleaning its paws on {groom_day} at {groom_time}")
    
my_cat1 = Cat('Rupert', '4', 'persian')
my_cat2= Cat('Esper', '9', 'maine coon')

          
my_cat1.meow()
my_cat2.grooming()
