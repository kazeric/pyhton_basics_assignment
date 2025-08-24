def grading():
    score = int(input('Enter your score: '))
    if score >= 90:
        print('A')
    elif score <90 and score>=80:
        print('B')
    elif score<80 and score>=70:
        print('C')
    elif score < 70 and score>=60:
        print('D')
    elif score < 60 and score>=50:
        print('E')
    else:
        print('F')

grading()