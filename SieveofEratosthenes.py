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
