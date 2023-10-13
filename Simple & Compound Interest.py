print("   ***Calculator for Simple & Compound Interest***   ")
print("1.Simple Interest")
print("2.Compound Interest")
P=eval(input("Enter the value of Principal:"))
R=eval(input("Enter the annual Rate of Interest:"))
T=eval(input("Enter the Time:"))
Simple_Int = P*R*T/100
Amount = P+Simple_Int
Ammount = P*(pow((1+R/100), T))
Compound_Int = Ammount-P
b=eval(input("Enter Your choice:"))
if b==1:
    print("Simple Interest:",Simple_Int)
    print("Amount:",Amount)
else:
    print("Compound Interest:",Compound_Int)
    print("Amount:",Ammount)
