# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# https://projecteuler.net/problem=4

def p(x):
    z=x
    y=0
    while int(x) > 0:
        y=y*10+x%10
        x=int(x/10)
    return y==z

def f():
    for i in range (1000000,10000,-1):
        if p(i):
            for j in range (999,100,-1):
                if i % j == 0 and i / j in range(100,1000):
                    return (i, j, int(i/j)  )

print(f())
