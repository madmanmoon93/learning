# Write a program that prints a staircase of size . 
# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    for i in range(n):
        print(" " * (n-i-1) + "#" * (i+1))