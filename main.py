# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# op = input("Enter the operator: ")
# def sum(a,b):
#     return a+b
# def sub(a,b):

#     return a-b
# def mul(a,b):
  
#      return a*b
# def div(a,b):
#      return a/b

# if(op=="+"):
#     print(sum(a,b))
# elif(op=="-"):
#     print(sub(a,b))
# elif(op=="*"):
#     print(mul(a,b))
# elif(op=="/"):
#     print(div(a,b))
# else:
#     print("Invalid operator")

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(1,2,3))




# def person(first=None, middle= "anal", last = None):
#     if first and middle and last: 
#         print(f"{first} {middle} {last}")
#     elif first and last:
#         print(f"{first} {last}")
    
# print(person(first="ram", last="hari"))
# operation = input("Enter the operation:")
# balance = 3000
# def checkBalance():
#         return print("Your balance is: ", balance)
# if operation == "viewBalance":
#     checkBalance()


#key mapping 
person ={
    "name": 'alex',
    "age": 34
}
print(f"{person["name"]} and his age is {person["age"]}")
print(person.get("name"))

#ask the name age gender of 3 student

list = []
for i in range(3):
    name = input("Enter the name:")
    age = input("Enter the age: ")
    gender = input("Enter the gender: ")
    student = {
         "name": name,
         "age": age,
         "gender": gender
      }
    list.append(student)
print(list)

#program to ask 3 numbers and print the greatest number 
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if(a < b):
#     print("B is greater", b)
# elif(b < c):
#     print("C is greater", c)
# elif(c<a):
#     print("A is greater", a)

#while loop
# count = 1
# while (count < 10):
#         print("The count is: ", count)
#         count = count + 1


# #tuple
# tuple = (1,2,3,4,5)
# print(tuple)

