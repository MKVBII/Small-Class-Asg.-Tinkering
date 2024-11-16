#lab one: LIST BASICS 
def lab1():
    my_flower1 = str(input('my flower 1: '))
    my_flower2 = str(input('my flower 2: '))
    my_flower3 = str(input('my flower 3: '))
    my_list = [my_flower1, my_flower2, my_flower3]
    print('my list', my_list)

    your_flower1 = str(input('your flower 1: '))
    your_flower2 = str(input('your flower 2: '))
    your_list = [your_flower1, your_flower2]
    print('your list', your_list)

    our_list = my_list + your_list
    print('our list', our_list)

    their_flower = str(input('their flower: '))
    our_list.append(their_flower)
    our_list[1] = their_flower
    print(our_list)
    our_list.remove(their_flower)
    print(our_list)
    our_list.pop(1)
    print(our_list)

#lab two: SET BASICS
def lab2():
    my_fruit1 = str(input('my fruit 1: '))
    my_fruit2 = str(input('my fruit 2: '))
    my_fruit3 = str(input('my fruit 3: '))
    fruits = {my_fruit1, my_fruit2, my_fruit3}
    print('fruits', fruits)

    your_fruit1 = str(input('your fruit 1: '))
    your_fruit2 = str(input('your fruit 2: '))
    fruits.add(your_fruit1)
    fruits.add(your_fruit2)
    print('fruits', fruits)

    their_fruit = str(input('their fruit: '))
    fruits.add(their_fruit)
    print('fruits', fruits)

    fruits.add(your_fruit1)
    print('fruits', fruits)
    fruits.remove(your_fruit1)
    print('fruits', fruits)

#lab 3: INPUT AND FORMATTED OUTPUT : RIGHT FACING ARROW
def lab3():
    head = input('input what you would like the head of the arrow to be: ')
    body = input('input what you would like the body of the arrow to be: ')
    print(' '*6+head)
    print(body*6+head*2)
    print(body*6+head*3)
    print(body*6+head*2)
    print(' '*6+head)

#lab 4: PHONE NUMBER BREAKDOWN
def lab4():
    num = int(input('Enter a 10 digit number that doesnt begin with 0: '))
    print(f'({num//10000000}) {(num%10000000)//10000}-{num%10000}')

#lab 5: SIMPLE STATISTICS LAB
def lab5():        
    num1 = float(input('enter any real number: '))
    num2 = float(input('enter any real number: '))
    num3 = float(input('enter any real number: '))
    num4 = float(input('enter any real number: '))

    print(f'{num1*num2*num3*num4:.0f} {(num1+num2+num3+num4)/4:.0f}')
    print(f'{num1*num2*num3*num4:.3f} {(num1+num2+num3+num4)/4:.3f}')

prompt = int(input("which lab would you like to test? 1,2,3,4 or 5?: "))
match prompt:
    case 1:
        print('LAB 1: LIST BASICS')
        lab1()
    case 2:
        print('LAB 2: SET BASICS')
        lab2()
    case 3:
        print('LAB 3: INPUT AND FORMATTED OUTPUT : RIGHT FACING ARROW')
        lab3()
    case 4:
        print('LAB 4: PHONE NUMBER BREAKDOWN')
        lab4()
    case 5:
        print('LAB 5: SIMPLE STATISTICS LAB')
        lab5()
    case _:
        print('Run the code again and enter an integer 1 through five')

