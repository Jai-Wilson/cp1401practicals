import random
value = 20

def main():
    create_random_variable(value)
    input_file = open('temps_input.txt', 'r')
    output_file = open('temps_output.txt', 'w')
    for line in input_file:
        celsius = convert_to_celsius(float(line))
        print(celsius, file=output_file)
    input_file.close()
    output_file.close()




def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius



def create_random_variable(value):
    for i in range(value):
        random_number = random.uniform(-200, 200)
        temperatures_file = open('temps_input.txt', 'a')
        print(random_number, file=temperatures_file)
    temperatures_file.close()


main()