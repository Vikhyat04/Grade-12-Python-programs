#PROGRAM 1

#WAP to calc (a+b)^3 or (a-b)^3 using user defined function
#Ask the choice from the user

#Not in q--> (a+b)^3=a^3+3a^2b+3ab^2+b^2 or (a-b)^3=a^3-3a^2b+3ab^2-b^3

#Name: Vikhyat
#Class: 12
#Date of Execution: 15/06/2021

def f1(a,b):
    print("Result:",(a**3)+(b**3)+(3*a*b*a)+(3*a*b*b))
def f2(a,b):
    print("Result:",(a**3)-(b**3)-(3*a*b*a)+(3*a*b*b))
print("Enter 2 numbers to calculate (a+b)^3 or (a-b)^3:")
x=int(input("Enter a value for num1:"))
y=int(input("Enter a value for num2:"))

print("Enter 1 to calculate (a+b)^3 or else,enter 2 for (a-b)^3:")
ch=int(input("Enter your choice:"))
if(ch==1):
    f1(x,y)
elif(ch==2):
    f2(x,y)
else:
    print("Invalid Input")

'''Output for Program 1

Enter 2 numbers to calculate (a+b)^3 or (a-b)^3:
Enter a value for num1:12
Enter a value for num2:8
Enter 1 to calculate (a+b)^3 or else,enter 2 for (a-b)^3:
Enter your choice:2
Result: 64

'''
