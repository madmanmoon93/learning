# Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

import math
def aVeryBigSum(ar):
    DigitSum = 0
    CarryOver = 0
    DigitSumList = list()
    for i in range(int(math.log10(max(ar))+1)): # Loop through array as many times as the highest number of digits in array
        DigitSum = CarryOver
        CarryOver = 0
        for j in range(len(ar)): # Loop through each item in array
            DigitSum = DigitSum + int(ar[j]/(10**i))%10
            if DigitSum > 9:
                CarryOver+=1
                DigitSum-=10
        DigitSumList.append(DigitSum)
    if CarryOver > 0:
        DigitSumList.append(CarryOver)
    DigitSumList.reverse()
    return int(''.join(str(Digit) for Digit in DigitSumList))
ar = [999,999,999]
result = aVeryBigSum(ar)
print(result)