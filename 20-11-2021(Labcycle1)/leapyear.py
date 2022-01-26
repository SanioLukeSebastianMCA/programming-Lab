a=int(input("enter the starting year:"))
b=int(input("enter the ending year:"))
for year in range(a,b):
    if year%400==0 or year%4==0 and year%100!=0:
        print("leap years are:",year)
