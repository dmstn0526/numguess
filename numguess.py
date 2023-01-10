from random import randint
from time import sleep

# Generate answer
answer = randint(1,100)

# print anser
print(answer)

username = input("Hi! What's your name? ")
print(f"Hi, {username} ! Guess the answer !")

# Guess number
guessnum = int(input("Guess the answer (1~100) : "))
print(f"{username} ! You guessed {guessnum} !")

# Compare answer with user's guess
if guessnum==answer : 
    print("****************************")
    sleep(1)
    print("****************************")
    sleep(1)
    print("****************************")
    sleep(1)
    print(f'You got it right!! The anwer is {answer}!!')
elif guessnum > answer:
    print(f'Keep going.. That was too high, {username}..')
elif guessnum < answer:
    print(f'keep going,, That was too low, {username}..')

