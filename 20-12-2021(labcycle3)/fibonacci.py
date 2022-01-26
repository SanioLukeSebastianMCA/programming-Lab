n=int(input("enter the number:"))
a=0
b=1
sum=0
count=1
print("fibonacci series are:")
while(count<=n):
    print(sum)
    count+=1
    a=b
    b=sum
    sum=a+b