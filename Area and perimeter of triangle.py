a = float(input("Enter the 1st side: "))
b = float(input("Enter the 2nd side: "))
c = float(input("Enter the 3rd side: "))

p = a + b + c
s = (a + b + c) / 2
r = s * (s - a) * (s - b) * (s - c)
t = r ** 0.5

print("The Perimeter of the triangle is : ", p)
print("The Area of the triangle is : ", t)