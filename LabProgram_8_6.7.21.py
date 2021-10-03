#Program 8

'''
Write a  program to accept a string(a sentence) and return a string having first letter of each word in capital letters

Name: Vikhyat Jagini
Class: 12
Date of Execution: 6/7/2021

'''

def cap(str):
    str1=str.split()
    str2=""
    for a in str1:
        str2=str2+a.capitalize()+" "
    print(str2)
print("Enter a sentence to see each word in the string capitalized:")
str=input("Enter your sentence:")
cap(str)
