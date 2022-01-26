str1="the number is string"
count=0
for i in range(0,len(str1)):
    if(str1[i]!=''):
        count+=1
print("number of characters in string:",str(count))