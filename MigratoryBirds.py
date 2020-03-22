# Print the type number of the most common bird;
# if two or more types of birds are equally common, choose the type with the smallest ID number.
# It is guaranteed that each type is 1, 2, 3, 4 or 5
# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen

def migratoryBirds(arr):
    birdTypeCounterList = [0,0,0,0,0]
    for bird in arr:
        birdTypeCounterList[bird-1]+=1
    return(birdTypeCounterList.index(max(birdTypeCounterList))+1)
