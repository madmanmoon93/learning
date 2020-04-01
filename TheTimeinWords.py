# Given the time in numerals, convert it into words
# https://www.hackerrank.com/challenges/the-time-in-words/problem?h_r=next-challenge&h_v=zen

def timeInWords(h,m):
    minuteLetterList=["o' clock","one","two","three","four","five","six","seven","eight",
                    "nine","ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen",
                    "eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four", 
                    "twenty five","twenty six","twenty seven","twenty eight", "twenty nine", "half"]
    hourLetterList=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    minuteDictionary = {}
    hourDictionary = {}
    for i in range (0,30):
        minuteDictionary[i] = minuteLetterList[i]
        minuteDictionary[i+30] = minuteLetterList[-i-1]
    for j in range (1,13):
        hourDictionary[j] = hourLetterList[j-1]
    if m in range(2,15) or m in range(16,30):
        result = (str(minuteDictionary[m]) + " minutes past " + str(hourDictionary[h]))
    elif m in range(31,45) or m in range(46,59):
        result = (str(minuteDictionary[m]) + " minutes to " + str(hourDictionary[h+1]))
    elif m == 0:
        result = (str(hourDictionary[h]) + " " + str(minuteDictionary[m]))
    elif m == 15 or m == 30:
        result = (str(minuteDictionary[m]) + " past " + str(hourDictionary[h]))
    elif m == 45:
        result = (str(minuteDictionary[m]) + " to " + str(hourDictionary[h+1]))
    else:
        result = (str(minuteDictionary[m]) + " minute past " + str(hourDictionary[h]))
    return result