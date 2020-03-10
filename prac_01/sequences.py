def menu():
    print('(E)ven numbers')
    print('(O)dd numbers')
    print('(S)quare numbers')
    print("(Q)uit")

number_1 = int(input("Ener your 1st number: "))
number_2 = int(input("Enter your 2nd number "))
number=[]
if number_1 < number_2:
    x = int(number_1)
    y = int(number_2)
    for i in range (x, y +1, 1):
        number.append(i)
else:

    x = int(number_2)
    y = int(number_1)
    for i in range (x, y + 1, 1):
        number.append(i)

menu()
choice=input().upper()
while choice != "Q":
    if choice == "E":
        print("Even numbers are:")
        for j in range(len(number)):
            if number[j] % 2 == 0:
                print(number[j], ', ', end='')


    elif choice == "O":
        print("Odd numbers are: ")
        for k in range(len(number)):
            if number[k] % 2 == 1:
                print(number[k], ', ', end='')
    elif choice == "S":
        print("The squares are: ")
        for n in range(len(number)):
            square = number[n] ** 2
            print(square, ", ", end='')
    else:
        print("Invalid option")

    print()
    menu()
    choice=input().upper()

print("Complete")


