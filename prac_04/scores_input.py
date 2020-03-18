


scores = []
score = int(input("score: "))

while score >= 0:
    scores.append(score)
    score = int(input("score: "))

print("You're highest score is ", max(scores))



