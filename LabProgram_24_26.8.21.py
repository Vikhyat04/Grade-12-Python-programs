#Program 24

#Write a random number generator that generates random numbers between 1 and 6 (simulates a dice)

#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 26/08/2021

import random
def rolladice():
    counter=0
    myList=[]
    while(counter<6):
        randomNumber=random.randint(1,6)
        myList.append(randomNumber)
        if(counter>=6):
            pass
        else:
            return myList
n=1
while(n==1):
    n=int(input("Enter 1 to roll a dice and get a random number:"))
    if(n==1):
        print(rolladice())
