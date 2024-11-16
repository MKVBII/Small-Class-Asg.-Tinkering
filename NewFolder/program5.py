#QUESTION 1
def reverseBinaryOf(x):
    ret = ''
    while x > 0:
        ret = ret + str(int(x%2))
        x = int(x/2)

    print(str(ret))
#reverseBinaryOf(7)

#QUESTION 2
def strengthenPassword(password):
    
    newPass = ''
    for i in password:
        if i == 'i':
            newPass = newPass + '1'
        elif i == 'a':
            newPass = newPass + '@'
        elif i == 'm':
            newPass = newPass + 'M'
        elif i == 'B':
            newPass = newPass + '8'
        elif i == 's':
            newPass = newPass + '$'
        else:
            newPass = newPass + i
    newPass = newPass + '!'
        

    print(newPass)

#strengthenPassword('mypassword')

#QUESTION 3
def intervalFive(x, y):
    while x <= y:
        print(x)
        x = x+5

#intervalFive(5,20)

#QUESTION 4
def reverse():
    s = str(input('Enter a string: '))
    end = ['d', 'done', 'Done']
    while s not in end:
        print(s[::-1])

        s = str(input('Enter a string:'))

#reverse()

#QUESTION 5
def bruteForce(a,b,c,x,y,z):
    for i in range(-10,11):
        for j in range(-10,11):
            if ((i*a)+(b*j) == c) and ((i*x)+(j*y )== z):   
                print(f'x = {i} , y = {j}')
                exit()
    print('There is no solution')

#bruteForce(1,2,3,4,5,6)

#QUESTION 6
def adjustVal():
    reps = int(input())
    values = []

    i = 0
    while i < reps:
        value = float(input())
        values.append(value)
        i = i + 1

    max = 0
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]

    adjustedVals = []
    for i in range(len(values)):
         adjustedVals.append(values[i]/max)

    for i in range(len(adjustedVals)):
        print(f'{adjustedVals[i]:.2f}')
    

adjustVal()