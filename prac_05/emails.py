


def main():
    user_data = {}
    user_email = input("What is your email? ")
    while user_email != "":
        true_user_name = get_name(user_email) #get the users name
        user_data[user_email] = true_user_name #store data into dictionary
        user_email = input("What is your email? ")
    for email, name in user_data.items():
        print(name, "({})".format(email)) #print stored information from dictionary





def get_name(user_email):
    user_name = user_email.split("@") #split the email at the "@" symbol
    trial_user_name = user_name[0].split(".") #if a dot is present, split the name at said dot
    true_user_name = " ".join(trial_user_name).title() #Join the name with correct grammar
    choice = input("Is your name " + true_user_name + "? Y/N")
    if choice.upper() != "Y" and "" != choice: #determine if generated name is correct or not
        true_user_name = input("What is your name? ") #if generated name is not correct, add correct name

    return true_user_name #return name


main()
