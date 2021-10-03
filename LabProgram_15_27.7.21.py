'''LAB PROGRAM

Write a program to read a file, count and print total words starting with 'a' or
'A' in the file

Name:Vikhyat Jagini
Class:12
Date of execution:27/7/21
'''

def count():
    c=0
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\wordswithA.txt","r")
    s=f.read()
    print("Words which start with A:")
    for word in s.split():
        if(word[0] in "aA"):
            print(word)
            c=c+1
    print(" \nNumber of words starting with 'A' or 'a':",c)
    f.close()
count()

