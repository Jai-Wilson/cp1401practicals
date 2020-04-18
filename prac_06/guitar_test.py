"""Guitar test file"""

from prac_06.guitar import Guitar

lindsays_guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
other_guitar = Guitar("Another guitar", 2013, 28)


print('{} get_age() - Expected {} got {}'.format(lindsays_guitar.name, 98, lindsays_guitar.get_age()))
print('{} get_age() - Expected {} got {}'.format(other_guitar.name, 98, other_guitar.get_age()))
print('{} get_age() - Expected {} got {}'.format(lindsays_guitar.name, True, lindsays_guitar.is_vintage()))
print('{} get_age() - Expected {} got {}'.format(other_guitar.name, False, other_guitar.is_vintage()))

