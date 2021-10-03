#Program 5

#Write a user defined function to perform all arithmatic operations on two numbers(+,-,*,/,%)

#Name:Vikhyat
#Class:12
#Date of Execution:15.06.2021

def op(x,y):
    print(x+y,"is sum of",x,"and",y)
    print(x-y,"is difference of",x,"and",y)
    print(x*y,"is product of",x,"and",y)
    print(x/y,"is quotient of",x,"and",y)
    print(x%y,"is modulus of",x,"and",y)

print("Enter two numbers to see the calculation of all arithmetic operations on them: ")            
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
op(num1,num2)

'''Output for Program 5

Enter two numbers to see the calculation of all arithmetic operations on them: 
Enter num1:6
Enter num2:13
19 is sum of 6 and 13
-7 is difference of 6 and 13
78 is product of 6 and 13
0.46153846153846156 is quotient of 6 and 13
6 is modulus of 6 and 13

'''
