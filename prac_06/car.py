"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, name='', fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """initialise string formatting for the class"""

        return '{}, fuel={}, odomoter={}'.format(self.name, self.fuel, self.odometer)


    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            print('You travelled {}km before running out of fuel'.format(self.fuel))
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
    def refuel(self, amount):

        self.fuel +=amount
        return self.fuel
