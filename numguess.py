from random import randint
from time import sleep

# Generate answer
def game_start_set():
    answer = randint(1,100)

    # print anser
    print(answer)

    username = input("Hi! What's your name? ")
    print(f"Hi, {username} ! Guess the answer !")
    print("You have 10 chance! Let's START")

    return username, answer

def game(username, answer):
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
    return

if __name__=='__main__':
    username,answer = game_start_set()
    game(username, answer)
    while(True):
        opt = input("Do you want another game? (Y/N) : ")
        if opt == 'Y':
            username,answer = game_start_set()
            game(username, answer)
        else:
            print("OK ! BYE !")
            break

