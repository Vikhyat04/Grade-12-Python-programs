#Program 25

#WAP to read a particular data and count the occurance of a particular word

#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 27/08/2021


f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\wordC.txt",'r')
read=f.readlines()
f.close()

s=input("Enter the word to be searched: ")
c=0



for i in read:
    line=i.split()
    for j in line:
        if (s==j):
            c=c+1

print("The word '",s,"' occurs", c,"times")
