import random

numGuesses = 8;
num = random.randint(1, 50)

name = raw_input("Hello. What is your name?\n")
print(name + ", I'm thinking of a number from 1 to 50. Can you guess it?\n")

while numGuesses != 0:
    guess = raw_input("Give it your best shot! You have "  + str(numGuesses) +  " tries.\n")
