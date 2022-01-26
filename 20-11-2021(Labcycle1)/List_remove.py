list = [3,4,5]
print("Original list:")
print(list)
for i in list:
   if i%2 == 0:
      list.remove(i)
print("after deleted even numbers:")
print(list)