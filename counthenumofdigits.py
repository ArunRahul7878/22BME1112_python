n = int(input("Enter a number:"))
numlist = list(str(n))
a=b=0
for i in numlist:
    if i == '0':
       a += 1
       
    elif i == '5':
       b += 1

print("The number of '0' is",a)
print("The number of '5' is",b)
