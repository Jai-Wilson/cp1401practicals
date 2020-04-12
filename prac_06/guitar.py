"""Guitar class file"""

CURRENT_YEAR = 2020

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):

        return CURRENT_YEAR - self.year

    def is_vintage(self):
        vintage = True if self.get_age() >= 50 else False
        return vintage
        # if  self.get_age() >= 50:
        #     vintage = True
        #     return vintage
        # else:
        #     return vintage


