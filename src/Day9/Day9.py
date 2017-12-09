import io
import re
import sys

with open("input.txt") as file:
    points, tags, garbageCount, open, close = (0, 0, 0, 0, 0)
    garbage, skip = (False, False)
    for char in file.read():
        if skip:
            skip = False
            continue
        elif char == '{' and garbage == False:
            open += 1
            tags += 1
        elif char == '}' and garbage == False:
            close +=1
            points += tags
            tags -= 1
        elif char == '!':
            skip = True
        elif char != '>' and garbage == True:
            garbageCount += 1
        elif char == '<':
            garbage = True
        elif char == '>':
            garbage = False

    print('Amount of points: ', points)
    print('Amount of non-canceled characters in the garbage: ',  garbageCount)
    print('Open Tags: ', open, " - Close Tags: ", close)
    file.close()