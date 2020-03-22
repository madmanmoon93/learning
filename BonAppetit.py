# Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. 
# Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. 
# Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
# https://www.hackerrank.com/challenges/bon-appetit/problem

def arraySum(arr):
    sumArray = 0
    for element in arr:
        sumArray+=element
    return sumArray

def bonAppetit(bill, k, b):
    correctSplitBill = int((arraySum(bill) - bill[k]) / 2)
    if correctSplitBill == b:
        print("Bon Appetit")
    else:
        print(b - correctSplitBill)