class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"This is {self.first_name.title()} {self.last_name.title()}")
        
    def greet(self):
        print(f"Hi there, {self.first_name.title()}!")
        

user1 = User('matteo', 'sala')
# user1.describe_user()
# user1.greet()

