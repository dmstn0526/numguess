from random import randint

# Generate answer
answer = randing(1,100)

# print anser
print(answer)

username = input("Hi! What's your name? ")
print(f"Hi, {username} ! Guess the answer !")

# Guess number
guessnum = input("Guess the answer (1~100) : ")
print(f"{username} ! You guessed {guessnum} !")
