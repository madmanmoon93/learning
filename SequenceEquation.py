# Given a sequence of n integers, p(1), p(2), ... p(n) where each element is distinct and satisfies 1 <= p(x) <= n.
# For each x where 1 <= x <=n, find any integer y such that p(p(y)) == x and print the value of y on a new line.
# https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    result = list()
    for x in range(len(p)):
        result.append(p.index(p.index(x+1)+1)+1)
    return result