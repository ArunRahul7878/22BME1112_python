count = 0
for i in range(101,400):
    a = str(i)
    b = a[0]
    c = a[1]
    d = a[2]
    if (int(b)) % 2 == 0 and (int(c)) % 2 == 0 and (int(d)) % 2 == 0:
        print(i)
        count+=1
                    
print(count,"numbers")        
