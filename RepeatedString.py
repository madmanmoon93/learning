# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first letters of Lilah's infinite string.
# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    finalStringList = list(s)
    occurrence = (int(n/len(s)) * s.count("a")) + (finalStringList[:(n % len(s))].count("a"))
    return occurrence