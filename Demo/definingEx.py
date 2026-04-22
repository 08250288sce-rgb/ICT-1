def sum():
    a=5
    b=10
    print("The sum of a and b is:",a+b)
print()
def product():
    a=5
    b=10
    print("The product of a and b is:",a*b)
# sum() 
# product()
print()
def sum_with_parameters(x,y):#parameter
    print("The sum of",x,"and",y,"is:",x+y)
sum_with_parameters(3,7)
print()
def product_with_parameters(x,y):
    print("The product of",x,"and",y,"is:",x*y)
product_with_parameters(5,5)# arguments=function call
print()
def sum_with_return(x,y):
    return x+y
print("The sum of 4 and 6 is:",sum_with_return(4,6))
print()
def product_with_return(x,y):
    return x*y
print("The Product of 4 and 6 is:",product_with_return(4,6))
