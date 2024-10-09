def dont_run():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("Bruh for real?")
        
print("give me two numbers and i'll divide them")
print("press q to quit")

while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
    # except (ZeroDivisionError , ValueError , TypeError):
    #     print("Invalid input. Try again... ")
    except ZeroDivisionError:
        print("Error: You can't divide by zero! Please try again.")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except TypeError:
        print("Error: Type mismatch! Please make sure to enter valid numbers.")
    else: 
        print(answer)