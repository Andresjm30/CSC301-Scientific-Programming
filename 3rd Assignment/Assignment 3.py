import math
import numpy as np

def main():
    X = [(1/10),(2/10),(3/10),(4/10)]
    N = (1,2,4,8,16)
    for i in X:
        value = 100
        for l in N:
            esValue = (sigma(i,l))
            remValue = (remain(i, l))
            absError = abs((esValue - math.cos(i)))
            relError = absError / math.cos(i)
            print("______________________________________________________________________________________________________")
            print("Function: Cos")
            print("x = {:<8}  n = {:<5}  | Taylor Cosine: {:<24} Exact Cosine: {:<24}  | Abs Error: {:<32} Rel Error: {:<32} |"
                    " Remainder Term: {:<32}".format(i,l,esValue, math.cos(i), absError, relError, remValue))
            if (absError < value):
                smalln = absError

        print("______________________________________________________________________________________________________")
        print("The smallest integer n such j = " + str(i) + " : " + str(smalln));

def sigma(x, n):
    sum = 0
    
    for k in range(0, n+1):
        sum += ((pow(-1,k) / math.factorial(2*k)) * pow(x, 2*k))
    
    return sum; 

def remain(x, n):
    f = 0
    remain = 0

    if (n % 4 == 0):
        f = np.cos(1)
    elif (n % 4 == 1):
        f = np.sin(1) * (-1)
    elif (n % 4 == 2):
        f = np.cos(1) * (-1)
    elif (n % 4 == 3):
        f = np.sin(1)

    remainder = (f * x**(n + 1)) / math.factorial(n + 1)

    return remainder;




main();
    