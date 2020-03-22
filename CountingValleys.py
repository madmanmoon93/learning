# Gary is an avid hiker. During his last hike he took exactly n steps. 
# For every step he took, he noted if it was an uphill, U, or a downhill, D step.
# Return the number of valleys Gary traversed. 
# A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.
# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(n, s):
    seaLevelCounter = 0
    seaLevelCounterList = list()
    stepList = list(s)
    valleyCounter = 0
    for step in range(n):
        if stepList[step] == "U":
            seaLevelCounter += 1
        else:
            seaLevelCounter += -1
        seaLevelCounterList.append(seaLevelCounter)
        if seaLevelCounter == 0 and seaLevelCounterList[step-1] < 0:
            valleyCounter += 1
    return(valleyCounter)