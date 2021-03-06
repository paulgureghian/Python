# Created by Paul A. Gureghian in Oct 2020.
# This Python program generates a random number between 1 and 10
# Then compares it with a user inputted number

# Import library
import random

# Define a function which generates a random number
def new_rand_num_generator():

    return random.randint(1, 10)

# Define 'start_game' function
def start_game():

    number_of_attempts = 0

    print("")
    print("---------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("---------------------------------------")
    print("")

    # Generate a random number between 1 - 10
    rand_num = new_rand_num_generator()
    print("Random number is:", rand_num, "\n")

    # Get a user number and compare it to the rand_num
    try:

        number = int(input("Enter a number between 1 and 10: "))
        print("")

        if number < 1 or number > 10:
            raise ValueError("Enter a number between 1 and 10")

        if number == rand_num:

            number_of_attempts += 1
            print("You got it, it took you", number_of_attempts, "attempt")
            print("")

        else:

            number_of_attempts += 1
            print("Wrong guess, try again \n")

    except ValueError as err:
        print("Wrong value, enter a number between 1 and 10 \n".format(err))

    while number != rand_num:

        try:

            number = int(input("Enter a number between 1 and 10: "))
            print("")

            if number < 1 or number > 10:
                raise ValueError("Enter a number between 1 and 10")

            if number > rand_num:

                number_of_attempts += 1
                print("It's lower")
                print("")

            elif number < rand_num:

                number_of_attempts += 1
                print("It's higher")
                print("")

            else:

                number_of_attempts += 1
                print("You got it, it took you", number_of_attempts, "attempts")                      
                print("")
                print("The game is over\n")
                break

        except ValueError as err:
            print("Wrong value, enter a number between 1 and 10 \n".format(err))

# Call the start_game function
start_game()