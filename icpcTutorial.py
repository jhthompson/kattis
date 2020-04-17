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
        ]
    if(n <= 13):
        return factorials[n]
    else:
        # factorial(13) goes past max m of 10^9 
        return factorials[13] 
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
