# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let L be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints: floor(sqrt(L)) <= row <= column <= ceil(sqrt(L))
# The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on.
# https://www.hackerrank.com/challenges/encryption/problem

import math
def encryption(s):
    stringLength = len(s)
    stringList = list(s)
    stringLengthSqrt = math.sqrt(stringLength)
    if int(stringLengthSqrt) == stringLengthSqrt:
        width, height = int(stringLengthSqrt), int(stringLengthSqrt)
    else:
        width = int(stringLengthSqrt) + 1
        height = int(stringLengthSqrt)
        if width * height < stringLength:
            height += 1
    matrix = [["" for x in range(width)] for y in range(height)]
    stringCounter = 0
    for i in range(height):
        for j in range(width):
            if stringCounter <= (stringLength - 1):
                matrix[i][j] = stringList[stringCounter]
                stringCounter += 1
    intermediaryList = []
    for a in range(width):
        for b in range(height):
            intermediaryList.append(matrix[b][a])
        intermediaryList.append(" ")
    finalString="".join(intermediaryList)
    return finalString