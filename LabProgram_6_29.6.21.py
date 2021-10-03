#Program 6

#Write a user defined function to check whether the entered number is a perfect no.or not

#Name:Vikhyat Jagini
#Class:12
#Date of Execution:29/06/2021


def perf(a):
    hold=0
    for i in range(1,((int)(a/2))+1):
        if(a%i==0):
            hold=hold+i
    return hold
num=int(input("Enter a number to see if it is perfect or not:"))
if(num==perf(num)):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")


'''Output for Program 6

Enter a number to see if it is perfect or not:28
28 is a perfect number

'''
