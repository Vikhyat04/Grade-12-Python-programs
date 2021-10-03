
#Program 20

#Write a program to write roll no, name and marks of 'n' students in a data file "marks.dat"

#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 26/08/2021
n=int(input("Enter the number of students you want to store data of in the data file:"))
f=open(r"C:\Python\Class 12 python\Lab Programs\BinaryFiles\marks.dat",'a')

for i in range(n):
    print("Enter details of student", (i+1),"below")
    rol=int(input("Enter roll no of student:"))
    name=input("Enter name of student:")
    marks=float(input("Enter marks of student:"))
    rec=str(rol)+","+name+","+str(marks)+"\n"
    f.write(rec)
f.close()
