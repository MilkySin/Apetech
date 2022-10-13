# a replica of apetech C class but in python
# starting conditons
from math import inf
from multiprocessing.sharedctypes import Value

x = 1
list = []

while x > 0:
    try:
        x = int(input("number: "))
    except:
        raise ValueError("not a number")
    if x > 0:
        list.append(x)
    if x <= 0:
        max = -inf
        min = inf
        for i in list:
            if max < i:
                max = i
            if min > i:
                min = i
        for i in list:
            total = 0
            avg = 0
            total += i
            avg = total / len(list)
        print(f"max: {max}, min: {min}, avg: {avg}")
