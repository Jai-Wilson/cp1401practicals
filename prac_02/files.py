

out_file=open('names.txt', 'w')
name = str(input("What is your name? "))
print("Your name is {}".format(name), file=out_file)
out_file.close()

in_file=open('names.txt', 'r')
print(in_file.read())
in_file.close()

in_file=open('numbers.txt', 'r')
number_1 = int(in_file.readline())
number_2=int(in_file.readline())
in_file.close()
print("the numbers are {} and {}. The addiition of these is ".format(number_1, number_2), number_1 + number_2)
in_file.close()

in_file=open('numbers.txt', 'r')
count = 0
for line in in_file:
    number=int(line)
    count += number
print("The sum of values in the file is ", count)
in_file.close()

