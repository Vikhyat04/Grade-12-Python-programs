#Program 7

#Write a program using a user defined functions, which accepts a list having even number of elements and swaps the elements at adjacent position

#Name:Vikhyat Jagini
#Class:12
#Date of Execution:29/06/2021


def switch(l):
    for i in range(0,len(l)-1,2):
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp
l=eval(input("Enter a list to see their positions swapped:"))
if(len(l)%2==0):
    switch(l)
    print(l)
else:
    print("Please enter even number of elements in the list")

'''Output for Program 7

Enter a list to see their positions swapped:[10,20,30,40]
[20, 10, 40, 30]
'''
