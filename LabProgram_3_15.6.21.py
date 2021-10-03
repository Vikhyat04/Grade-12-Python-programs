#Program3

#Write a user defined function to accept lower limit and upper limit and print all odd and even numbers between those limits

#Name:Vikhyat
#Class:12
#Date of Execution:15.06.2021

def FuncOddEven(x,y):
    print("Odd numbers witin the range",x,"and",y,"are printed below:")
    for i in range(x+1,y):
        if((i%2!=0)):
            print(i)
    print("Even numbers witin the range",x,"and",y,"are printed below:")
    for i in range(x+1,y):
        if((i%2==0)):
            print(i)
print("Enter the lower limit and higher limit respectively to see the odd numbers and even numbers within that range:")            
l=int(input("Enter the lower limit:"))
u=int(input("Enter the higher limit:"))
if(u>l):
    FuncOddEven(l,u)
else:
    print("Invalid input")


'''Output for Program 3

Enter the lower limit and higher limit respectively to see the odd numbers and even numbers within that range:
Enter the lower limit:23
Enter the higher limit:45
Odd numbers witin the range 23 and 45 are printed below:
25
27
29
31
33
35
37
39
41
43
Even numbers witin the range 23 and 45 are printed below:
24
26
28
30
32
34
36
38
40
42
44

'''
