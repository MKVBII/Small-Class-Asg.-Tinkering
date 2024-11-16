#QUESTION 1

#push
def push(A, x):
    dec = [x]
    A = dec + A
    return A

#pop
def pop(A): 
    x = A[0]
    X = []
    for i in range(1, len(A)):
        X[i] = A[i]
    A = X
    return x

#enqueue
def dequeue(A):
    x = A[-1]
    X = []
    for i in range(0, len(A)-2):
        X[i] = A[i]
    A = X
    return x

#enqueue
def enqueue(A, n):
    X = [n]
    A = X + A
    return A

#removeDuplicates
def removeDups(A):
    #CUT OFF
    

# QUESTION 2 (STARTED BEFORE QUESTION 1, I DONT KNOW WHY) 
# Input: Two n x n matrices A and B (n = number of elements)
# Output: Matrix C = AB
def MatrixMultiply(A, B, n):
    C = [[0 for a in range(n)] for b in range (n)]
    for i in range(0,n-1):
        for j in range(0, n-1):
            for k in range(0, n-1):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C