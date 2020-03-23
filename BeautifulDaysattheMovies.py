# Given a range of numbered days, [i..j] and a number k, determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where absolute of (i - reverse(i)) is evenly divisible by k. 
# If a day's value is a beautiful number, it is a beautiful day. 
# Print the number of beautiful days in the range.
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def reverse(nr):
    reverseNumber = 0
    while int(nr) > 0:
        reverseNumber = reverseNumber * 10 + nr % 10
        nr = int(nr/10)
    return reverseNumber

def beautifulDays(i, j, k):
    beautifulDayCounter = 0
    for day in range(i,j+1):
        if abs(day - reverse(day)) % k == 0:
            beautifulDayCounter += 1
    return beautifulDayCounter