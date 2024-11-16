import math

def findMean(A):
    if len(A) == 1:
        return A[0]
    else:
        h1 = A[0:math.floor(len(A)/2)].copy()
        h1total = sum(h1)
        h1mean = h1total/len(h1)

        h2 = A[math.floor(len(A)/2): ].copy()
        h2total = sum(h2)    
        h2mean = h2total/len(h2)

        return h1mean + h2mean 
    
#https://stackoverflow.com/questions/37836323/average-of-a-sequence-of-integers-using-divide-and-conquer
def avgCalc(A, l, r):

    #base case
    if (l == r):
        return A[1]
    
    mid = (l+r)/2
    avgl = 0
    avgr = 0

    avgl = A[1]/r + avgCalc(A, l, mid)
    avgr = A[mid + 1]/r + avgCalc(A, mid+2, r)

    
    