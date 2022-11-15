x = int(input("Enter x:"))
y = int(input("Enter y:"))
a = 0
for j in range(100,1000):
    numlist = list(str(j))
    b = 1
    for i in numlist:
        b = b * int(i)   
    if x < b < y:
        print(j)
        a+= 1
        
print()
print(a,"numbers satisfies the criteria")
