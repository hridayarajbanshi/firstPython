

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
count = 1
while (count < 10):
        print("The count is: ", count)
        count = count + 1
    
# program to ask user with the name of the student and enter the name until selects N or n
list =[]
while True:
    name = input("Enter the name of the student: ")
    list.append(name)
    print("Do you want to continue? Y/N")
    choice = input()
    if choice == "y":
        continue
    else: 
         print("The list of students are: ", list)
         break