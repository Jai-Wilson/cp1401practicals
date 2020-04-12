"""Guitars file"""


from prac_06.guitar import Guitar

def main():
    guitars = []
    print('My guitars!')
    # name = input('Name: ')
    # while name != '':
    #     year = int(input('Year: '))
    #     cost = float(input('Cost: $'))
    #     new_guitar = Guitar(name, year, cost)
    #     guitars.append(new_guitar)
    #     print('{} ({}) : ${:.2f} added.'.format(name, year, cost))
    #     name = input('Name: ')


    # the follwoing guitars used for testing purposes only

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print('these are my guitars:')
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage() == True:
            vintage_string = '(vintage)'
        else:
            vintage_string = ''

        print('Guitar {}: {:>20} ({}), worth ${:10,.2f}{}'.format(i, guitar.name, guitar.year, guitar.cost, vintage_string))





main()
