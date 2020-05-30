import wikipedia


user_search = input("What page would you like summarised?")
while user_search != '':
    valid_entry = False
    while not valid_entry:
        try:
            user_page = wikipedia.page(user_search)
            print('The page title is {}'.format(user_page.title))
            print('The page URL is {} '.format(user_page.url))
            print(wikipedia.summary(user_search))
            valid_entry = True

            user_search = input("What page would you like summarised?")
        except wikipedia.DisambiguationError:
            print("Please choose a more specific input")
            user_search = input("What page would you like summarised?")


