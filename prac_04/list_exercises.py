


numbers = []

for i in range(5):
    number = int(input("Number {}: ".format(i+1)))
    numbers.append(number) #add entered numbers to the list created

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is ", sum(numbers) / len(numbers)) # print respective outcomes


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
             'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

given_username = input("What is your username? ") #check if the entered username is a username stored on the system
if given_username in usernames:
    print("Access granted")
else:
    print("Access denied")
