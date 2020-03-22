# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
# given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    uniqueSocks = list(set(ar))
    sockPairs = 0
    for item in range(len(uniqueSocks)):
        socksCount = ar.count(uniqueSocks[item])
        sockPairs += int(socksCount/2)
    return sockPairs