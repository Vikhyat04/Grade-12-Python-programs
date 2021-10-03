#Program 9

'''
Write a  program to display frequencies of all elements of a list

Name: Vikhyat Jagini
Class: 12
Date of Execution: 6/7/2021

'''

def frq(l):
    l1=[]
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
            l1.append(l.count(i))
    print("Element \t \t \t Frequency")
    for i in range(len(l1)):
        print(l2[i],"\t \t \t \t",l1[i])




print("Enter a list to see frequency of each element:")
l=eval(input("Enter a list:"))
frq(l)
