import random

value = 20

for i in range(value):
    random_number = random.uniform(-200, 200)
    file = open('temps_input.txt', 'a')
    file.write('{}\n'.format(random_number))
