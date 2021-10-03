#Program 2

#WAP using user defined function, accept a positive number from user, find square,cube and square root of that number

#Name:Vikhyat
#Class:12
#Date of Execution:15.06.2021

def calc(x):
    print("Square of",x,"is",x*x)
    print("Cube of",x,"is",x*x*x)
    print("Square Root of",x,"is",x**0.5)
num=int(input("Enter a positive number to see its square,cube and square root:"))
if(num>0):
    calc(num)
else:
    print("Invalid input")

'''Output for Program 2

Enter a positive number to see its square,cube and square root:23
Square of 23 is 529
Cube of 23 is 12167
Square Root of 23 is 4.795831523312719

'''
