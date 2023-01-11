from random import shuffle, choice


N = 10000

doors - [0,0,1]
shuffle(doors)
user_choice = choice(doors)

result = {
    'stay':0,
    'change':0,
}

if user_choice == 0:
    result['change']+=1
if user_choice == 1:
    result['stay']+=1

