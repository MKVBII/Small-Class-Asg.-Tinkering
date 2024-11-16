#QUESTION 1
def kilo_to_pounds(kilos):
    pounds = kilos*2.204
    return pounds

#print(kilo_to_pounds(37.8))

#QUESTION 2
def driving_cost(miles_per_gallon:float, dollars_per_gallon:float, miles_driven):
    cost_per_mile = (dollars_per_gallon/miles_per_gallon)*miles_driven
    print(f'{cost_per_mile:.2f}')

#driving_cost(20.0,3.1599, 10)
#driving_cost(20.0,3.1599, 50)
#driving_cost(20.0,3.1599, 400)


#QUESTION 3
def feet_to_steps(user_feet: float) -> int: 
    return int(user_feet/2.5)
def main(feet_walked):
    print(feet_to_steps(feet_walked))
#main(40.7)

#QUESTION 4
def int_to_reverse_binary(integer_value: int):
    bin = ''
    while integer_value > 0:
        bin = bin + str(integer_value%2)
        integer_value = integer_value // 2
    return bin

def string_reverse(input_string):
    print(str(input_string)[::-1])

def convert_to_binary(number:int):
    string_reverse(int_to_reverse_binary(number))

#convert_to_binary(7)

#QUESTION 5
def swap_values(user_val1:int, user_val2:int, user_val3:int, user_val4:int):
    ret =[user_val2, user_val1, user_val4, user_val3]
    return ret

def main(user_val1:int, user_val2:int, user_val3:int, user_val4:int):
    ret = swap_values(user_val1, user_val2, user_val3, user_val4)
    print(ret[0],ret[1],ret[2],ret[3])

#main(1,2,3,4)

#QUESTION 6
def fib(index):
    if index < 0:
        print(-1)
        exit()
    
    fib_arr = [0,1]
    if index == 0 or index == 1:
        print(fib_arr[index])
        exit()
    
    for i in range(2, index):
        fib_arr.append(fib_arr[i-1] + fib_arr[i-2])

    print(fib_arr[index-1])
    

#fib(8)