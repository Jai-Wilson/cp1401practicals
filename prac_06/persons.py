"""Persons file for manipulating the person class"""

from operator import attrgetter

from prac_06.person import Person

acceptable_entry = False
no_of_peple = None
while not acceptable_entry:

    try:
        no_of_people = int(input("How many people would you like to enter the details of? "))
        acceptable_entry = True
    except ValueError:
        print('Please enter a valid number')

people = []
for i in range(no_of_people):
    person_first_name = input('What is their first name? ')
    person_last_name = input("What is their second name? ")
    acceptable_age = False
    person_age = None
    while not acceptable_age:
        try:
            person_age = int(input('What is their age? '))
            acceptable_age = True
        except ValueError:
            print('Enter a valid number')

    new_person = Person(person_first_name, person_last_name, person_age)
    people.append(new_person)

people.sort(key=attrgetter('last_name'))
print('People stored in database')
for i in range(len(people)):
    print(people[i])
