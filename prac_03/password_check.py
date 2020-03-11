

minimum_length = 4

def get_password():
    password = input("Enter a password of minimum {} characters: ".format(minimum_length))

    while len(password) < minimum_length:
        password = input("Enter a password of minimum {} characters:".format(minimum_length))

    print("*"*len(password))

get_password()
