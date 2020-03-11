"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

result = 0

def main():
    score = float(input("Enter score: "))
    result = score_calculator(score)
    print(result)

    random_score = random.randrange(0, 100) #generates random number
    print("Your random score is: {}".format(random_score))
    result = score_calculator(random_score) #takes the result variable from the called function
    print(result)






def score_calculator(score): #deciphers user's score and figures out result
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result  = "Pass"
    else:
        result = "Bad"
    return result #returns result to the main function


main()


