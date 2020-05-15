from random import randint
from prac_08.car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        rand_num = randint(0, 100)
        if rand_num >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven

