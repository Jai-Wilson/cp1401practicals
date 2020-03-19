import random


picks = int(input('How many picks would you like to generate? '))
total = 6
values = []
for i in range(picks):
    count = 0
    random_values = []
    while count < total:
        random_number = random.randrange(1, 46)
        random_values.append(random_number)
        count +=1
    random_values.sort()
    values.append(random_values)
    print(values[i])
