'''Write a program to read a text file and use it in append mode, show the working
of writelines()

Name:Vikhyat Jagini
Class:12
Date of execution:27/7/21
'''


f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UseFunc.txt","a")
content=("\nComputers is my cup of tea.","\nIt has several applications.")
f.writelines(content)
f.close()
