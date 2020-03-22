# Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend.
# If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.
# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    amountSpent = 0
    amountSpentList = list()
    for keyboard in range(len(keyboards)):
        for drive in range(len(drives)):
            amountSpent = keyboards[keyboard] + drives[drive]
            if amountSpent > b:
                pass
            else:
                amountSpentList.append(amountSpent)
    if len(amountSpentList) == 0:
        return -1
    else:
        return (max(amountSpentList))