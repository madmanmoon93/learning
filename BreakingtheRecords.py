# Complete the breakingRecords function in the editor below.
# It must return an integer array containing the numbers of times she broke her records. 
# Index 0 is for breaking most points records, and index 1 is for breaking least points records. 
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    maxScore = scores[0]
    minScore = scores[0]
    maxScoreCounter, minScoreCounter = 0, 0
    for score in range(len(scores)):
        if scores[score] > maxScore:
            maxScore = scores[score]
            maxScoreCounter+=1
        if scores[score] < minScore:
            minScore = scores[score]
            minScoreCounter+=1
    print(maxScoreCounter, minScoreCounter)
