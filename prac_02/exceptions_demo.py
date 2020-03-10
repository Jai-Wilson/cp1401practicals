"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value error will occur when a number is not entered by the user
2. When will a ZeroDivisionError occur?
A zero division error will occur when a 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, the following code demonstrates that
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator Can not equal 0!")
        print()
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")