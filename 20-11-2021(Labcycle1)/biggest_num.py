a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if(a>b and a>c):
    print("biggest number is",a)
elif(b>c and b>a):
    print("biggest number is",b)
else:
    print("biggest number is",c)