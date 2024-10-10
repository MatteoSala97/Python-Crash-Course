from car import Car, Battery

class ElectricCar(Car):
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)
        self.battery_size = 80
        self.batt = Battery()
    
    def get_battery_info(self):
        print(f"This car has a battery capacity of {self.battery_size} kWh.")    
       
    def fill_tank(self):
        print("This car doesnt have a tank bruh.")
        
my_tesla = ElectricCar('tesla', 'model s', '2023')
print(my_tesla.get_descriptive_name())
my_tesla.get_battery_info()
my_tesla.fill_tank()


battery = Battery('Duracell')

print(battery.name)

