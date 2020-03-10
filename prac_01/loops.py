


for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 101, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

user_number = int(input('How many stars would you like to print: '))

for m in range(1, user_number + 1, 1):
    print('*', end='')
print()


amount_of_lines = int(input("How many lines of stars would you like to print? "))

for n in range(1, amount_of_lines + 1, 1):
    print('*' * n)
print()
