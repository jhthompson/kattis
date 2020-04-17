#! /usr/bin/python3

import sys

for i in sys.stdin:
    longAuthor = str(i)

    for char in longAuthor:
        if(char.isupper()):
            print(char, end = "")
    print()
