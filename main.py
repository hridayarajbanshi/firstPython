

#program to ask 3 numbers and print the greatest number 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if(a < b):
    print("B is greater", b)
elif(b < c):
    print("C is greater", c)
elif(c<a):
    print("A is greater", a)
