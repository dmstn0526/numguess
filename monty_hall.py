from random import shuffle, choice


result = {
    'stay_to_win':0,
    'move_to_win':0,
}

doors = [0,0,1]

iter_num = int(input("Enter some num(100-10000): "))

for _ in range(iter_num):
    shuffle(doors)
    user_choice = choice(doors)
    if user_choice == 0:
        result['move_to_win']+=1
    if user_choice == 1:
        result['stay_to_win']+=1

print(result)
