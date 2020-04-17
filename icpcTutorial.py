#! /usr/bin/python3

import math

mnt = input().split()

m = int(mnt[0])
n = int(mnt[1])
t = int(mnt[2])

def one(n):
    factorials = [
            1,
            1,
            2,
            6,
            24,
            120,
            720,
            5040,
            40320,
            362880,
            3628800,
            39916800,
            479001600,
            6227020800,
            87178291200,
            1307674368000,
            20922789888000,
            355687428096000,
            6402373705728000,
            121645100408832000,
            2432902008176640000,
            51090942171709440000,
            1124000727777607680000,
            25852016738884976640000,
            620448401733239439360000,
        ]
    if(n <= 24):
        return factorials[n]
    else:
        # way past max m of 10^9 at this point
        return factorials[24] 
def two(n):
    return math.pow(2, n) 
def three(n):
    return math.pow(n, 4)
def four(n):
    return math.pow(n, 3)
def five(n):
    return math.pow(n, 2)
def six(n):
    return n * math.log(n, 2)
def seven(n):
    return n

def performOperations(t):
    mapping = {1: one,
            2: two,
            3: three,
            4: four,
            5: five,
            6: six,
            7: seven}
    return mapping[t] 

try:
    if(performOperations(t)(n) > m):
        print("TLE")
    else:
        print("AC")
except:
    print("TLE")
