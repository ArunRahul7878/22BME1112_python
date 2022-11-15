n = int(input("Enter the nth group you want to print:"))
a =0

for j in range(1,101,2):
    a += 1
    if a == n:
        for i in range(1,j+1):
            print(i,end = ",")

b = 0


