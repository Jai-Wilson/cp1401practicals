def main():
    friend_data = {}
    choice = menu()
    while choice.upper != 'Q':
        if choice.upper() == 'A':
            friend_data = add_friend_data(friend_data)
        elif choice.upper() == 'C':
            friend_data = change_an_address(friend_data)
        elif choice.upper() == 'P':
            print_an_address(friend_data)
        choice = menu()

def add_friend_data(friend_data):
    friend_name = input("What is your friend's name? ")
    friend_address = input("What is your friend's address? ")
    friend_data[friend_name] = friend_address
    return friend_data


def menu():
    acceptable_choices = ['A', 'C', 'P', 'Q']

    choice = input("What would you like to do? \n"
                   "A - Add a new friend\n"
                   "C - Change an address\n"
                   "P - Print an Address\n"
                   "Q - Quit >>> ")

    while choice.upper() not in acceptable_choices:
        print("Invalid input!")
        choice = input("What would you like to do? \n"
                       "A - Add a new friend\n"
                       "C - Change an address\n"
                       "P - Print an Address\n"
                       "Q - Quit >>> ")
    return choice


def change_an_address(friend_data):
    name = input("Who's address would you like to change? ")
    while name not in friend_data.keys():
        print("Name not in the database")
        name = input("Who's address would you like to change? ")
    friend_data[name] = input("Enter a new address for {}: ".format(name))
    return friend_data


def print_an_address(friend_data):
    name = input("Who's address would you like to print?")
    while name not in friend_data.keys():
        print("That name is not in the database")
        name = input("Who's address would you like to print? ")
    print("{}'s address is {}".format(name, friend_data[name]))


main()
