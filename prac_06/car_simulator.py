"""Car simulator file"""

from prac_06.car import Car

print('Lets drive')
car_name = input('What is the name of your car? ')
my_car = Car(car_name, 100)

distance = int(input("How many km's do you want to drive? "))
my_car.drive(distance)
print(my_car)

