
minimum_length = 4
def main():
    password = get_password(minimum_length)





def get_password(minimum_length):

    password = input("Enter a password of minimum {} characters: ".format(minimum_length))

    while len(password) < minimum_length:
        password = input("Enter a password of minimum {} characters:".format(minimum_length))

    print_stars(password)



def print_stars(password):
    print('*' * len(password))

main()
