#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner . Then use your list to print a message to each person, inviting them to dinner .

authors=[
    "William Shakespeare",
    "Leo Tolstoj",
    "F. Scott Fitzgerald",
    "Virginia Woolf",
    "Gabriel García Márquez",
    "Ernest Hemingway",
]

additional_authors=[
    "George Orwell",
    "Franz Kafka",
    "Emily Dickinson",
    "Mark Twain"
    ]

for  item in authors:
    print("Hi, I'd like to invite you to dinner dear " + item) # non so se voglia un loop, però non credo scriverò un invito custom per ogni autore :D 
 
   
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations . You’ll have to think of someone else to invite .

# • Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of the guest who can’t make it .
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting .
# • Print a second set of invitation messages, one for each person who is still in your list .

unavailable_guest = authors[2] 
print(f"\nUnfortunately, {unavailable_guest} can't make it to the party.")

authors[2]=additional_authors[0]

print("\nSending new invitations:")
for  item in authors:
    print("Hi, I'd like to invite you to dinner dear " + item) 
    
    
#More guests. Add, insert and append a new guest. 

new_authors = [
    "Toni Morrison",
    "Herman Melville",
    "Ray Bradbury"
]

authors.append(new_authors[0])
authors.insert(4, new_authors[1])
authors.pop(2)

print("\nSending more and more invitations:")
for  item in authors:
    print("Hi, I'd like to invite you to dinner dear " + item) 
    
authors.sort()
print(authors)

authors.sort(reverse=True)
print(authors)
print(sorted(authors))

new_authors.reverse()
print(new_authors)

print(len(new_authors))

print(additional_authors[-1])