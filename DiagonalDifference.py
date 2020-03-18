# Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diagonalSum = 0
    for i in range(n):
        diagonalSum = diagonalSum + (arr[i][i] - arr[i][n-i-1])
    return abs(diagonalSum)