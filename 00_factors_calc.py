# Functions go here

# Puts a series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions ():

    statement_generator("Instructions / Information", "=")
    print()
    print("These are the instructions")
    print()
    print("Come back to write instructions Jack!")
    print()
    print()
    return ""

    instructions()















# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number 
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error) 
            print()























# gets factors, returns a sorted list
#def get_factors(to_factor):

import random

# set up a list...

my_list = []

# generate 4 random numbers between 1 & 10...
for item in range(0, 4):

    # generate random number between 1 and 10
    random_num = random.randint(1, 10)

    # add number to list 
    my_list.append(random_num)


# print the *unsorted* list...
print(my_list)

# sort the list
my_list.sort()

my_list_len = len(my_list)

# print the sorted list
print()
print(my_list)
print("The list has {} items".format(my_list_len))
print()



































# Main Routine goes here

# Heading 
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input ("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.   Itself ;)"

    # comments for squares / primes 
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # output factors and comment 

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is speacial..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")