# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers. 
# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    arrSum = 0
    arrPartialSum = 0
    arrPartialSumList = []
    for number in arr:
        arrSum+=number
    for number in arr:
        arrPartialSum=arrSum-number
        arrPartialSumList.append(arrPartialSum)
    print(min(arrPartialSumList), max(arrPartialSumList))