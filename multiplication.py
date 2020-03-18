# number1 = 999999999999999999999999999999912562211261
# number2 = 1341412412412412124152152152151252121412412421412
# product = 0
# counter = 0
# while int(number2)>0:
#     modulo = number2 % 10
#     product = product + (modulo * number1 * 10**counter)
#     number2 = int(number2/10)
#     counter+=1
# print(product)

Number1 = 123456789
Number2 = 987654321
List2 = list(str(Number2))
NumberOfDigits2 = range(len(List2))
ProductList = list()
ResultList = list()
for Digit in NumberOfDigits2: # Individual digits of Number2 list multiplied with Number1 as a whole
    Product = int(List2[Digit])*Number1
    ProductList.append(Product)
ProductList.reverse()
# print(ProductList)
exp = 0
Carry = 0
for j in range(len(ProductList)+len(str(ProductList[-1]))-1):
    Result = Carry
    Carry = 0
    for i in range(len(ProductList)):
        if exp >= i:
            Result = Result + int(ProductList[i]/(10**(exp-i)))%10
            if Result > 9:
                Result-=10
                Carry+=1
    ResultList.append(Result)
    exp+=1
ResultList.reverse()
print(ResultList)