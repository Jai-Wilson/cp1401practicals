from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """Main function deciphering which user input will result in which action"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive!")
    print(MENU)
    choice = get_selection()
    cumulative_bill = 0
    current_taxi = None

    while choice != 'Q':
        if choice == 'C':
            display_taxis(taxis)
            taxi_choice = int(input('Choose taxi: '))
            print('Bill tp date: ${:.2f}'.format(cumulative_bill))
            current_taxi = taxis[taxi_choice]

        elif choice == 'D':
            distance_of_drive = int(input('Drive how far? '))
            current_taxi.drive(distance_of_drive)
            cost_of_trip = current_taxi.get_fare()
            print('Your {} trip cost you ${}'.format(current_taxi.name, cost_of_trip))
            cumulative_bill += current_taxi.get_fare()

        print(MENU)
        choice = get_selection()

    print("Your final bill is {}".format(cumulative_bill))
    display_taxis(taxis)


def get_selection():
    """Take the user input and decides if it is a valid input or not"""
    acceptable_choices = ['Q', 'C', 'D']
    valid_choice = False
    while not valid_choice:
        choice = input('>>> ').upper()
        if choice not in acceptable_choices:
            print('Invalid choice')
            choice = input('>>> ')
        else:
            valid_choice = True
    return choice


def display_taxis(taxis):
    """Display the available taxis"""
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, taxi))


main()
