from random import shuffle, choice


N = 10000

result = {
    'stay':0,
    'change':0,
}

doors = [0,0,1]

for _ in range(N+1):
    shuffle(doors)
    user_choice = choice(doors)
    if user_choice == 0:
        result['change']+=1
    if user_choice == 1:
        result['stay']+=1

print(result)
