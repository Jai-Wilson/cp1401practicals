
def print_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


name=input("Enter name: ")
print_menu()
choice=input().upper()

while choice != "Q":
    if choice == "H":
        print("Hello")
    elif choice == "G":
        print("Goodbye")
    else:
        print("Invalid option")
    print_menu()
    choice=input()

print("You have quit the program")




