n = int(input("Enter the n value:"))
a = b = 0

for i in range(n):
    a += 1/((2+b)*(5+b))
    b += 3

print("The sum up to",n,"th term is",a)
