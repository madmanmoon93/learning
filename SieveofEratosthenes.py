# Iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. 
# The multiples of a given prime are generated as a sequence of numbers starting from that prime
# with constant difference between them that is equal to that prime.

n=100
list=list(range(2,n+1))
for divisor in list:
    index = divisor-2
    while index < len(list):
        dividend=list[index]
        if dividend % divisor == 0 and dividend != divisor:
            list.remove(dividend)
        index+=1
print(list)
