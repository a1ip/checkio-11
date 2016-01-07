#!/bin/python
print("median")

#ternary: a if test else b
def checkio(array):
    sortedList = sorted(array)
    arrayLength = len(sortedList)
    median = int(arrayLength / 2)

    if (arrayLength % 2 == 0):
        return ((sortedList[median] + sortedList[median - 1]) / 2)
    else:
        return (sortedList[median])

a = [1, 2, 3, 4, 5]
b = [3, 1, 2, 5, 3]
c = [1, 300, 2, 200, 1]
d = [3, 6, 20, 99, 10, 15]
arrays = [a, b, c, d]

print("arrays: ", arrays)

for array in arrays:
    print("array: ", checkio(array))
