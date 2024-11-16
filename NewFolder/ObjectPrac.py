import math

class Restaurant:

    def __init__(self, name: str, rating: int, profits: float):
        self.name = name
        self.rating = rating
        self.profits = profits
        #self.total = self.rating + self.bookings

class Chain:
    def __init__(self, restaurant1: Restaurant, restaurant2: Restaurant, restaurant3: Restaurant):
        self.restaraunt1 = restaurant1
        self.restaurant2 = restaurant2
        self.restaurant3 = restaurant3
        self.profits = self.restaraunt1.profits + self.restaurant2.profits + self.restaurant3.profits

Arbys = Restaurant(input('Enter res name: '), input('Enter res rating: '), input('Enter res bookings: '))
Chic = Restaurant(input('Enter res name: '), input('Enter res rating: '), input('Enter res bookings: '))
Ramen = Restaurant(input('Enter res name: '), input('Enter res rating: '), input('Enter res bookings: '))

chain = Chain(Arbys, Chic, Ramen)

print(f'{Arbys.name}\n{Arbys.rating}\n{Arbys.profits}\n{Chic.name}\n{Chic.rating}\n{Chic.profits}\n{Ramen.name}\n{Ramen.rating}\n{Ramen.profits}\nChain Profits {float(chain.profits)}')



#object = Object()
#print(object.sum)