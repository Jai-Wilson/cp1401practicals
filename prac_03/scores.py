import random

def main():
    number = int((input("How many scores would you like to generate? ")))

    for i in range(number):
        random_score = random.randrange(0, 100)
        result = score_calculator(random_score)
        write_file(random_score, result)









def score_calculator(score): #deciphers user's score and figures out result
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result  = "Passable"
    else:
        result = "Bad"
    return result #returns result to the main function


def write_file(random_scores, result):
    file=open('Scores and results.txt', 'a')
    file.write("The score of {} is {}\n".format(random_scores, result))

main()



