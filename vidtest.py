

secret_number = 4

guess = False

while guess == False:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if user_guess != secret_number:
        print('Unlucky, try again')

    elif user_guess == secret_number:
        print("Well done, the number was", secret_number)
        guess = True
        break

print('game over')




