import random 
import math
number = random.randint(1,100)
tries = 7 
try:
    for i in range(tries):
        guess = input("please provide a guess: ")
        guess_int = int(guess)
        if guess_int == number:
            print("You are a good player, you guessed properly")
            break
        elif (i == tries-1):
            print("your chances are done!! useless!!")
            
        elif guess_int > number:
            print("please guess with a smaller value")
        elif guess_int < number:
            print("please guess with a larger value")
except ValueError:
    print("Please provide a numeric guess")



