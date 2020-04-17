#! /usr/bin/python3

import sys

N = int(sys.stdin.readline())

def findOddMan(arr):
    for j in range(0,len(arr),2):
        if(j == len(arr)-1):
            return (arr[j])
        elif(arr[j] != arr[j+1]):
            return(codes[j])

for i in range(1, N+1):
    G = int(sys.stdin.readline())
    codes = sys.stdin.readline().split()
    codes.sort()
    print(f"Case #{i}: {findOddMan(codes)}")


