import random
def scores(grade):
    result = ""
    if grade <= 100 and grade >= 90:
        result = "A"
    elif grade >= 80 and grade <90:
        result = "B"
    elif grade >= 70 and grade <80:
        result = "C"
    else:
        result = "D"
    print "Score: " + str(grade) + "; Your grade is "+ result

for i in range(10):
    grade = random.randint(60, 100)
    scores(grade)
    