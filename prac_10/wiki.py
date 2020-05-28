import wikipedia


user_search = input("What page would you like summarised?")
while user_search != '':
    print(wikipedia.summary(user_search))
    user_search = input("What page would you like summarised?")
