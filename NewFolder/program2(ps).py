import math
from math import pow, sqrt

def divide():
    user_num = float(input())
    div_num = float(input())
    x = 0
    y = 0
    z = 0
    for i in range(0, 3):
        user_num = math.floor(user_num/div_num)
        if i == 0:
            x = user_num
        if i == 1:
            y = user_num
        if i == 2:
            z = user_num
    print(x, y, z)
divide()


def costPerMile():
     mileage = float(input())
     cost = float(input())
     costPerMile = cost/mileage
     print(f'{costPerMile*20:.2f} {costPerMile*75:.2f} {costPerMile*500:.2f}') 
costPerMile()
#costPerMile(25.0, 3.1599)  

def burnedCalories():
    age = float(input())
    weight = float(input())
    hr = float(input())
    time = float(input())
    caloriesBurned = ((age*0.2757 + weight*0.03295 + hr*1.0781 - 75.4991)*time)/8.368
    print(f'{caloriesBurned:.2f}')
burnedCalories()
#burnedCalories(49, 155, 148, 60)

def math():    
    x = float(input())
    y = float(input())
    z = float(input())
    pw = pow(x,z)
    xDblPow = pow(x, pow(y,z))
    ab = abs(x-y)
    sq = sqrt(pw)
    print(f'{pw:.2f} {xDblPow:.2f} {ab:.2f} {sq:.2f}')
math()
#math(5.0, 1.5, 3.2)

def musicalFrequencies():
    initialFreq = float(input())
    print(f'{initialFreq:.2f}')
    for i in range(1,4):
        print(f'{initialFreq*pow(pow(2,1/12),i):.2f} Hz')
musicalFrequencies()

#musicalFrequencies(440)

def currConversion():
    nickels = float(input())
    dimes = float(input())
    quarters = float(input())
    print(f' Amount: ${(0.05*nickels + 0.10*dimes + 0.25*quarters):.2f}')
currConversion

#currConversion(3,1,4)