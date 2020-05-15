from prac_08.unreliable_car import UnreliableCar

def main():
    my_bad_car = UnreliableCar("Dodgy chinese car", 100, 24.77)
    my_good_car = UnreliableCar("Good Japanese Car", 100, 97.88)


    #attempt to drive each car 10 times
    for i in range (1, 5):
        print("Attempting to drive car {} kilometers".format(i))
        print("{} drove {} km".format(my_bad_car.name, my_bad_car.drive(i)))
        print("{} drove {} km".format(my_good_car.name, my_good_car.drive(i)))

    print(my_bad_car)
    print(my_good_car)

main()
