# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website . Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for log-ging in again.

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed .

# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username .

# username_list = ['giovanni', 'maria', 'luigi', 'anna', 'francesca', 'admin']
username_list = []

if username_list != []:
    for user in username_list:
        if user.lower() == 'admin':
            print('Hello ' + user.title() + ', would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for loggin in again.')
else:
    print('Please register a new user!')
        