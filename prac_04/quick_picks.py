import random


picks = int(input('How many picks would you like to generate? ')) #generate the amount of quick picks
total = 6
values = []
for i in range(picks):
    count = 0
    random_values = []
    while count < total:
        random_number = random.randrange(1, 46) #generate random values
        random_values.append(random_number) #add to list
        count +=1
    random_values.sort() #sort the values in acending order
    values.append(random_values) #add to values list
    print(values[i]) #print the respective line of the code
