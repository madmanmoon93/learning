# Lily has a chocolate bar that she wants to share it with Ron for his birthday.
# Each of the squares has an integer on it. She decides to share a contiguous segment
# of the bar selected such that the length of the segment matches Ron's birth month and 
# the sum of the integers on the squares is equal to his birth day. 
# You must determine how many ways she can divide the chocolate.
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def arraySum(arr):
    sumArray = 0
    for element in arr:
        sumArray+=element
    return sumArray

def birthday(s,d,m):
    sharedChocolate = 0
    if len(s) == m and arraySum(s) == d:
        sharedChocolate = 1
        return sharedChocolate
    for chocolate in range(len(s)-(m-1)):
        if arraySum(s[chocolate:(m+chocolate)]) == d:
            sharedChocolate+=1
    return sharedChocolate
