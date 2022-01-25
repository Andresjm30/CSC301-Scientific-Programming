import math
from math import sin
import scipy.integrate

y = lambda x: ((100 / x**2) * sin(10 / x))
exact = scipy.integrate.quad(y, 1, 3)
print("Exact Value = " + str(exact[0]))


def f(x):
    return ((100 / x**2) * sin(10 / x))

def simpsons_rule(a,b):
    c = (a+b) / 2.0
    h3 = abs(b-a) / 6.0
    return h3*(f(a) + 4.0*f(c) + f(b))

def composite_simpsons(a, b, n):
    step = (b - a) / n

    current = a
    rs = 0
    while (current < b):
        rs += simpsons_rule(current, current + step)
        current += step
    return rs

def absoluteError(approx, exact):
    return approx - exact

def relativeError(approx, exact):
    return (abs(approx - exact))/exact

def run_CompSimp():
    N = [2, 4, 8, 16, 32, 64, 128, 256, 512]
    print("Composite Simpsons Rule")
    for x in N:
        ExampleSimp = composite_simpsons(1, 3, x)
        AbsError = absoluteError(ExampleSimp, exact[0])
        RelError = relativeError(ExampleSimp, exact[0])
        print("_________________________________________________________________________________________________")
        print("N =" + str(x))
        print("Approximate Value: " + str(ExampleSimp), "  Absolute Error: " + str(AbsError), "  Relative Error: " + str(RelError))

run_CompSimp();

def recursive_asr(a,b,err,whole):
    c = (a+b) / 2.0
    left = simpsons_rule(a,c)
    right = simpsons_rule(c,b)
    if abs(left + right - whole) <= 15*err:
        return left + right + (left + right - whole)/15.0
    return recursive_asr(a,c,err/2.0,left) + recursive_asr(c,b,err/2.0,right)

def adaptive_simpsons_rule(a,b,err):
    return recursive_asr(a,b,err,simpsons_rule(a,b))

def run_AdapSimp():
    Error = [10**(-1), 10**(-2), 10**(-4), 10**(-8)]
    print("Adaptive Simpsons Rule:")
    for x in Error:
        ExampleAdap = adaptive_simpsons_rule(1, 3, x)
        AbsError = absoluteError(ExampleAdap, exact[0])
        RelError = relativeError(ExampleAdap, exact[0])
        print("_________________________________________________________________________________________________")
        print("Error Tolerance = " + str(x))
        print("Approximate Value: " + str(ExampleAdap), "  Absolute Error: " + str(AbsError), "  Relative Error: " + str(RelError))

run_AdapSimp();