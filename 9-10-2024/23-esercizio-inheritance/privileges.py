class Privileges():
    def __init__(self):
        self.privileges = [
            'can add post '
            'can delete post '
            'can ban user '
        ]

    def show_privileges(self):
        print("Admin privileges: ")
        for item in self.privileges:
            print(f"The admin {item}")