# Given a time in-hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    unconvertedTime = list(s)
    convertedTime = unconvertedTime[:len(unconvertedTime)-2]
    hourHour = unconvertedTime[0]+unconvertedTime[1]
    timeConvention = unconvertedTime[-2]+unconvertedTime[-1]

    if timeConvention == "PM" and hourHour == "12":
        convertedTime = unconvertedTime[:len(unconvertedTime)-2] 

    elif timeConvention == "AM" and hourHour == "12": 
        convertedTime[0] = "0"
        convertedTime[1] = "0"

    elif timeConvention == "PM":
        convertedTime[0] = str(int(convertedTime[0])+1)
        convertedTime[1] = str(int(convertedTime[1])+2) 

    convertedTime = "".join([str(Digit) for Digit in convertedTime])
    return convertedTime