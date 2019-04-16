import os
from sys import exit

# PID2ISBN is a terminal application that accepts a product ID
#   and generate its corresponding ISBN-10 number.


### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.

    os.system('clear')
              
    print("\t*********************************************************")
    print("\t***  PID2ISBN - Convert Product ID to ISBN-10 number  ***")
    print("\t*********************************************************")
    
def get_pid():
    # Let users know what they can do.
    
    return input("\nEnter the Product ID: ")


def end_app_user():

    choice = input("Start again (y/[n])?: ")
    if choice == 'y':
        return False
    else:
        return True
    
def weighted_sum_digits(n):
    # A helper function to calculate the weigted sum of digits.
    # Used in determining the error control digit of the ISBN.

    s = 0
    i = 2
    while n:
        s += i * (n % 10)
        n //= 10
        i = i + 1
    return s

### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.

display_title_bar()

while (True):

    string_input = get_pid()

    # Trivial Product ID checks.

    if not string_input.isdigit():
        print("Product ID invalid: Contains non-numeric characters.\n")

    elif len(string_input) != 12:
        print("Product ID invalid: ID should be 12 digit long.\n")

    else:
        # Removing first 3 digits
        pid = int(string_input[3:])

        # Finding modulus
        last_character = 11 - (weighted_sum_digits(pid) % 11)

        # Determining the error control digit

        if(last_character == 11):
            isbn = string_input[3:] + '0'

        elif (last_character == 10):
            isbn = string_input[3:] + 'x'

        else:
            isbn = string_input[3:] + str(last_character)

        print("ISBN-10: " + isbn +'\n')

    if(end_app_user()):
        break