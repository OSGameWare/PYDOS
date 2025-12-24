import random

print("Number Guessing Game")

number_to_guess = random.randrange(100)

chancesnum = input("How many guesses do you want? ")

chances = chancesnum

guess_counter = 0

print("\033c")

while guess_counter < int(chances):

    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and it only took you {guess_counter} attempts!')
        break

    elif guess_counter >= int(chances) and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    elif my_guess > number_to_guess:
        print('Your guess is less than ' + str(my_guess))

    elif my_guess < number_to_guess:
        print('Your guess is higher than ' + str(my_guess))