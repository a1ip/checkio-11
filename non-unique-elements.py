#!/bin/python
# print("non-unique-elements")

a = [1, 2, 3, 1, 3]
b = [1, 2, 3, 4, 5]
c = [5, 5, 5, 5, 5]
d = [10, 9, 10, 9, 8]

# for i in array:
#     print("i: ", i)

# print(array, " length: ", len(array))

def checkio(data):
    uniques = {}
    for x in data:
        if x not in uniques:
            uniques[x] = 1
        else:
            uniques[x] = uniques[x] + 1

    result = []
    result = list(filter((lambda x: uniques[x] > 1), data))

    return result

print("result: ", checkio(a))
print("result: ", checkio(b))
print("result: ", checkio(c))
print("result: ", checkio(d))
