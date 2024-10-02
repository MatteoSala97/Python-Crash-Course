# Store a person’s name in a variable, and print a message to that person . Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?
# Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase .

name="eric"
print("Hello "+name.title()+ ", would you like to learn some Python today?")
print("Hello "+name.upper()+ ", would you like to learn some Python today?")
print("Hello "+name.lower()+ ", would you like to learn some Python today?")

#Find a quote from a famous person you admire . Print the quote and the name of its author . Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

author="Albert Einstein"
quote='“A person who never made a mistake never tried anything new.”'

print(author+" once said: "+quote)

# Repeat Exercise 2-5, but this time store the famous per-son’s name in a variable called famous_person . Then compose your message and store it in a new variable called message . Print your message .

author="Albert Einstein"
quote='“A person who never made a mistake never tried anything new.”'
full_msg= author+" once said: "+quote
print(full_msg)

print(author.rstrip() + "\n once said" + quote.lstrip())