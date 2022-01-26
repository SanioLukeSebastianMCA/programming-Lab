a=input("enter the words:")
b=input("enter word:")
if b in a:
  for vowel in b:
    if vowel[0] in 'aeiou':
        print(list(vowel))
else:
    print("Element not found.")