import math 

def maximize(A):
    sa = []
    for i in range(len(A)):
        if A[i] > 0:
            sa.append(A[i])
    return sa

#B = [2,4,5,7,9]
#C = maximize(B)
#print(C)
#print(sum(C))



#https://www.geeksforgeeks.org/generate-hadamard-matrix-of-given-order/
def hmat(size):
    n = 2**size
    hadamard = [[0] * n for _ in range(n)] #initializes and 2^size x 2^size matrix 
    hadamard[0][0] = 1
    k = 1
    while (k < n): #fills the hadamard matrix in stages 
        for i in range(k):
            for j in range(k):
                hadamard[i+k][j] = hadamard[i][j]
                hadamard[i][j+k] = hadamard[i][j]
                hadamard[i+k][j+k] = -hadamard[i][j]
        k *= 2

    #displays the matrix 
    for i in range(n):
        for j in range(n):
            print(hadamard[i][j], end = ' ')
        print()

n = 2
hmat(n)
            
num = 92
print(92//10)
a = [1,2,3,4,5]
a /= math.sqrt(2)
print(a)