# In this challenge, you will be given a list of letter heights in the alphabet and a string. 
# Using the letter heights given, determine the area of the rectangle highlight assuming all letters are 1 mm2 wide. 
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    wordList = list(word)
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    maxHeight = 0
    for letter in wordList:
        letterHeight = h[alphabetList.index(letter)]
        if letterHeight > maxHeight:
            maxHeight = letterHeight
    return maxHeight * len(wordList)