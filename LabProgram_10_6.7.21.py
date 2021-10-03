#Program 10

'''
Write a program to display those strings which are starting with "A" or "a" of a given string of list

Name: Vikhyat Jagini
Class: 12
Date of Execution: 6/7/2021

'''

def chk(l):
    for i in l:
        if(i[0] in "Aa"):
            print(i)

print("Enter a list of strings to see which elements start with A or a:")
l=eval(input("Enter a list:"))
chk(l)
