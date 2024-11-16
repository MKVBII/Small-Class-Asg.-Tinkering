import math

#1 SMALLEST NUMBER 
def smallestVal():
    num = [int(input('Enter a number (1/3): ')), int(input('Enter a number (2/3): ')), int(input('Enter a number (3/3): '))]
    minVal = min(num)
    print(minVal)

#2 INTERSTATE HIGHWAY NUMBERS
def highway():
    hwNum = int(input('Enter a highway number: '))

    if hwNum < 1 or hwNum > 999:
        print(f'{hwNum} is not a valid highway interstate number')
        exit()

    #primary highways
    if (len(str(hwNum)) <= 2):
        if (hwNum % 10 != 0):
            print(f'I-{hwNum} is primary, going north/south')
        else:
            print(f'I-{hwNum} is primary, going east/west')

    #auxiliary highways 
    if (len(str(hwNum)) == 3): 
        if (str(hwNum)[1] == 0 and str(hwNum)[2] == 0):
            print(f'{hwNum} is not a valid interstate highway number')
        if (hwNum % 10 != 0):
            print(f'I-{hwNum} is auxiliary, serving I-{str(hwNum)[1]}{str(hwNum)[2]}, going north/south')
        else:
            print(f'I-{hwNum} is auxiliary, serving I-{str(hwNum)[1]}{str(hwNum)[2]}, going east/west')

#3 SEASONS
def seasons():
    date = [str(input('Enter a month: ')), int(input('Enter a date in that month (number): '))]
    months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    
    if date[0] not in months or (date[1] < 0 or date[1] > 31) or (date[0] == 'Febuary' and (date[1] > 29)):
        print('Invalid')
        exit()

    #Spring
    if months.index(date[0]) in range(2,6):
        if (date[0] == months[2] and date[1] > 19) or (date[0] in months[3:5] and date[1] in range(1,31)) or (date[0] == months[5] and date[1] < 21):
            print('Spring')
            exit()

    #Summer
    if months.index(date[0]) in range(6,10):
        if (date[0] == months[6] and date[1] > 22) or (date[0] in months[4:9] and date[1] in range(1,31)) or (date[0] == months[9] and date[1] < 22):
            print('Summer')
            exit()

    #Autumn
    if months.index(date[0]) in range(10,13):
        if (date[0] == months[10] and date[1] > 21) or (date[0] in months[11:12] and date[1] in range(1,31)) or (date[0] == months[12] and date[1] < 21):
            print('Autumn')
            exit()

    #Winter
    if months.index(date[0]) == 11 and (date[1] > 20 and date[1] < 32):
        print('Winter')
        exit()
    if months.index(date[0]) in range(0,2) and date[1]:
        if (date[0] in months[0:2] and date[1] in range(1,31)) or (date[0] == months[2] and date[1] in range(1,29)):
            print('Winter')
            exit()
#seasons()


#4 EXACT CHANGE
def  change():
    change = int(input('Enter the amount of change: '))

    dollars = 0
    tens = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    dollarPlural = 'Dollar'
    quarterPlural = 'Quarter'
    dimePlural = 'Dime'
    nickelPlural = 'Nickel'
    pennyPlural = 'Penny'


    if (len(str(change)) >= 3):
        dollars = int(str(change)[ : len(str(change)) - 2])
        tens = int(str(change)[len(str(change)) - 2 : ])
        quarters = int(tens/25)
        dimes = int((tens % 25)/10)
        nickels = int(((tens % 25) % 10) / 5) 
        pennies = int(((tens % 25) % 10) % 5) 
        
    
    if (len(str(change)) <= 2):
        tens = int(str(change)[len(str(change)) - 2 : ])
        quarters = int(tens/25)
        dimes = int((tens % 25)/10)
        nickels = int(((tens % 25) % 10) / 5) 
        pennies = int(((tens % 25) % 10) % 5) 

    money = [dollars, quarters, dimes, nickels, pennies]
    mPlurals = [dollarPlural, quarterPlural, dimePlural, nickelPlural, pennyPlural]

    for i in range(len(money)):
        if money[i] > 1 and i < 4:
            mPlurals[i] = mPlurals[i] + 's'
        if i == 4 and money[i] > 1:
            mPlurals[i] = 'Pennies'

    for i in range(len(money)):
        if money[i] > 0:
            print(f'{money[i]} {mPlurals[i]}')

    

change()

#5 LEAP YEAR 
def leapYear():
    year = int(input('Enter a year number: '))

    #century years
    if str(year)[len(str(year))-1] == '0' and str(year)[len(str(year))-2] == '0':
        if year % 400 == 0:
            print(f'{year} - leap year')
        if year % 400 != 0:
            print(f'{year} - not a leap year')
    
    if year % 4 == 0:
        print(f'{year} - leap year')
    if year % 4 != 0:
        print(f'{year} - not a leap year')

#leapYear()

#6 GOLF SCORES 
def golfScores():
    strokes = int(input('Enter the number of strokes takes: '))
    par = int(input('Enter the par number (expected strokes): '))
    score = par - strokes
    scName = ''
    if par not in range(3,6):
        scName = 'Error'
        print(f'Par {par} in {strokes} strokes is {scName}')
        exit()

    #Eagle
    if score == 2:
        scName = 'Eagle'
    #Birdie
    if score == 1:
        scName = 'Birdie'
    #Par
    if score == 0:
        scName = 'Par'
    #Bogey
    if score == -1:
        scName = 'Bogey'

    if scName == '':
        scName = 'Error'

    print(f'Par {par} in {strokes} strokes is {scName}')
    
#golfScores()
#print(3 % 10)
