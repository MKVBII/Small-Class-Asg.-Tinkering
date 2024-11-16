output = f'{2*2}'
print(output)
#4

output = f'{2*2=}'
print(output)
#2*2=4

output  = f'{{2}} + {{3}} = {{5}}'
print(output)
#{2} + {3} = {5}

kids = 4
adults = 2
total = f'{kids+adults} total'
print(total)
#6 total

total = f'{kids+adults=} total'
print(total)
#kids+adults=6 total

name = 'Aiden'
print(f'{name:s}')# default presentation type: Aiden

number = 4
print(f'{number:d}') # decimal (integer values only): 4
print(f'{number:03d}') # leading 0 notation: 004
print(f'{number:b}') # binary(base 2) (integer values only): 100
print(f'{number:f}')# fixed point notation (6 places of precison): 4.000000
print(f'{number:.2f}')# programmer defined precision: 4.00


number = 7600
print(f'{number:,d}')# decimal (integer values only) with commas: 7,600
number = 7600.1
print(f'{number:,.2f}')# fixed point notation(programmer defined precision) with commas: 7,600.10

number = 31
print(f'{number:x}') #hexadecimal numbers 
print(f'{number:b}')
#1f

number = 44
print(f'{number:e}')
