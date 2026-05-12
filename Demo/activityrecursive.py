def fun1(x,y):
    if x==0:
        return y
    else:
        return fun1(x-1,x+y)
x = int(input("Enter a number of x:"))
y = int(input("Enter a number of y:"))
print("fun1 of numbers from 1 to",x,y,"is:",fun1(x,y))