from random import randint
from time import sleep

# Generate answer
answer = randint(1,100)

# print anser
print(answer)

username = input("Hi! What's your name? ")
print(f"Hi, {username} ! Guess the answer !")
print("You have 10 chance! Let's START")
count = 0

while (True):
    count += 1
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
        break

    elif guessnum > answer:
        print(f'Keep going.. That was too high, {username}..')
        
    elif guessnum < answer:
        print(f'keep going,, That was too low, {username}..')
    if count == 10:
        print('---------10 chance was done---------\n-------------You Failed-------------')
        break



