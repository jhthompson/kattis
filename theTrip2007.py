#! /usr/bin/python3

from collections import OrderedDict
from collections import Counter

while True:
    n = input()

    if(n == 0):
        break

    bags = input().split()
    bags = list(map(int, bags))
    bags = Counter(bags)
    #print(bags)
    #print(OrderedDict(sorted(bags.items(), key = lambda t : t[1], reverse=True)))

    orderedBags = OrderedDict(sorted(bags.items(), key = lambda t : t[1], reverse=True))

    result = []
    for i in range(orderedBags
    for key, value in orderedBags.items():
        #print(key, '->', value)

