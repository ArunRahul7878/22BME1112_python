w = float(input("Enter the weight in kilogram:"))
h = float(input("Enter the height in meter:"))
bmi =  w/(h**2)
print(bmi)
if bmi < 18.5:
    print("Underweight")
    
elif 18.5 <= bmi <= 24.9:
    print("Normal")
    
elif 25 <= bmi <= 29.9:   
    print("Overweight")
    
elif bmi >= 30:
    print("Obsity")
    
else:
    print("ERROR")
