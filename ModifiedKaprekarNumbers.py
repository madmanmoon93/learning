# A modified Kaprekar number is a positive whole number with a special property. 
# If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p, q):
    kaprekarList = []
    for number in range (p,q+1):
        numberSquared = number * number
        lengthOfNumberSquared = int(len(str(numberSquared)))
        if lengthOfNumberSquared % 2 == 1:
            digitSplit = int(lengthOfNumberSquared/2) + 1
        else:
            digitSplit = lengthOfNumberSquared/2
        rightSide = numberSquared % (10 ** digitSplit)
        leftSide = int(numberSquared / (10 ** digitSplit))
        if rightSide + leftSide == number:
            kaprekarList.append(number)
    if not kaprekarList:
        print("INVALID RANGE")
    else:
        print(*kaprekarList)
