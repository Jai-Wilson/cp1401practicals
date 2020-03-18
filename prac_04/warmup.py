

name = input("What is your name? ")
count = 0
for letter in name:
    if letter.lower() in 'aeiou':
        count +=1

print("The number of vowels in the name is {}".format(count))
