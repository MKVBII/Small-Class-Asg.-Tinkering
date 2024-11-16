my_list = ['bananas', 'apples', 3, 'kiwis', 'mangoes', True]
#print(my_list)
#print(my_list[3])
#print(my_list[-1])

prices = ['$20', 14.99, 5]
#print(prices)
prices.append('nig')
#print(prices)
prices.remove('nig') 
#print(prices)
prices.pop(2)
#print(prices)

#inserting elements into list via 'input' method 
#city_list = [input(), input(), input()]
#print(city_list)

A = [1,2,3,4,5,6,7,8,9,10]
print(A[:5])
print(A[:5:3])
print(A[:-1])
print(A[::-1])
print(A)
print(len(A))
del A[0:5] #used to delete elements from a list at a given index 

B = [1,2,3]
C = [B*4]
print(C)

tuple = (1,2,3,4,5)
print(tuple.index(1))

#NAMED TUPLES 
from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])
chevy = Car('Chevy', 'Blazer', 32000, 275, 8)
corvette = Car('Corvette', 'X3', 90000, 500, 2)
print(chevy)
print(corvette)
print(corvette.model)
print(corvette.price + corvette.horsepower)

City = namedtuple('City',['name', 'state', 'population'])
citydata = City(input(), input(), int(input()))
print(f'City name: {citydata[0]}\nState: {citydata[1]}\nPop.: {citydata[2]}')

#SETS
set = {1,2,3,4}
set2 = {4,5,6}
print(set.symmetric_difference(set2))
print(set.union(set2))
