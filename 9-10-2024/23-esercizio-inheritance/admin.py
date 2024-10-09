from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)     
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()
    
admin1 = Admin('mario', 'rossi')       

admin1.describe_user()
admin1.show_privileges()