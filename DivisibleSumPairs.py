# You are given an array of integers, ar,  and a positive integer, k. 
# Find and print the number of (i,j) pairs where i < j and ar[i] + ar[j] is divisible by k. 
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    counter = 0
    for integer1 in range(0,n):
        for integer2 in range(integer1+1, n):
            if (ar[integer1] + ar[integer2]) % k == 0:
                counter+=1
    return counter