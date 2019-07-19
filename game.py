import random

numGuesses = 8;
num = random.randint(1, 50)

name = raw_input("Hello. What is your name?\n")
print(name + ", I'm thinking of a number from 1 to 50. Can you guess it? \n")

while numGuesses != 0:
    guess = raw_input("You have "  + str(numGuesses) +  " tries.\n")
    guess = int(guess)
    numGuesses = numGuesses - 1

    if guess < num:
        print("Your guess is too low! You have " + str(numGuesses) + " guesses left.")

    if guess > num:
        print("Your guess is too high! You have " + str(numGuesses) + " guesses left.")

    if guess == num:
        break

if guess == num:
    print("Wow! You guessed the number in " + str(8 - numGuesses) + " tries.")

if guess != num:
    print("Sorry. The number I was thinking of was " + str(num) + ".")
