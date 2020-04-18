"""Car simulator file"""

from prac_06.car import Car

MENU = 'Menu:\n d) Drive \n r) Refuel \n q) Quit'



def main():
    print('Lets drive')
    car_name = input('What is the name of your car? ')
    my_car = Car(car_name, 100)
    print(my_car)
    print(MENU)
    user_choice = input('>>>').lower()
    while user_choice != 'q':
        if user_choice == 'd':
            drive(my_car)
        elif user_choice == 'r':
            refuel(my_car)
        else:
            print('Invalid choice')
        print(my_car)
        print(MENU)
        user_choice = input('>>>').lower()
    print("Goodbye {}'s driver".format(my_car.name))


def refuel(my_car):
    acceptable_amount = False
    while not acceptable_amount:
        try:
            fuel_amount = int(input('How many units of fuel do you want to add to the car? '))
            if fuel_amount <=0:
                print(fuel_amount, ' must be >= 0')
            else:
                my_car.add_fuel(fuel_amount)
        except ValueError:
            print('Invalid input')


def drive(my_car):
    if my_car.fuel <= 0:
        print('You have no fuel! Time to refuel')
    else:
        distance = int(input("How many km's do you want to drive? "))
        my_car.drive(distance)


main()
