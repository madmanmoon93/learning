# For each array, perform a number of right circular rotations and return the value of the element at a given index.
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    a1 = a[-k%len(a):] + a[:-k%len(a)]
    result = list()
    for query in queries:
        result.append(a1[query])
    return result
