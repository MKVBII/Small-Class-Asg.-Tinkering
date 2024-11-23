#Strig manipulation

def isNum(str: str):
    if str.isdigit():
        print('Yes')
    print('No')
#print(isNum('3,333'))

def nameFormat(str: str):
    strArr = str.split()
    print(f'{strArr[2]}, {strArr[0][0]}.{strArr[1][0]}')
#nameFormat('Pat Silly Doe')

def countCs(c: str, str: str):
    ctr = 0
    for char in str: 
        if char == c:
            ctr += 1
    if ctr > 1 or ctr == 0:
        print(f"{ctr} {c}'s")
    print(f'{ctr} {c}')

#countCs('n', 'Monday')

def madLib():
    s = str(input('Enter a word: '))
    n = int(input('Enter a number: '))
    if s == 'quit':
        quit()
    else:
        while s != 'quit':
            if n > 1 or n == 0:
                print(f'Eating {n} {s}s a day keeps you happy and healthy.')
            if n == 1:
                print(f'Eating {n} {s} a day keeps you happy and healthy.')
            s = str(input('Enter a word: '))
            n = int(input('Enter a number: '))

def palindrome(st: str):
    ns = ''
    for i in st:
        if i != ' ':
            ns += i
    rs = ''
    for i in ns[::-1]:
        rs += i
    if ns != rs:
        print(f'not a palindrome: {ns}')
        quit()
    print(f'palindrome: {st}')

#palindrome('never odd or even')

def remNonAlp(s: str):
    ns = ''
    for i in s:
        if i.isalpha():
            ns += i
    print(ns)

remNonAlp('-Hello, 1 world$!')
