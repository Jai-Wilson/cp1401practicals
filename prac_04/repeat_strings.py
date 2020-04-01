


list_strings = []
repeat_strings = []
user_input = input("Enter string here: ")

if user_input in list_strings: #checks if string has already been entered
    repeat_strings.append(user_input) #if so, add to repeat strins list
list_strings.append(user_input) #add to strings list

while len(user_input) != 0:
    user_input = input("Enter string here: ")
    if user_input in list_strings:
        repeat_strings.append(user_input)
    list_strings.append(user_input)


print("The strings you entered were: {}".format(list_strings)) #print the strings list and repeat strings list
print("The strings you repeated were: {}".format(repeat_strings))
