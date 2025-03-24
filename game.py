from random import randint
number = randint(1,100)
guess = int(input("Input number"))
if guess == number:
    print("wow")
print(guess)