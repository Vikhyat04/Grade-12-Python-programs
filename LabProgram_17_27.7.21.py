'''
Write a program to read from a text file and show file handling functions

Name:Vikhyat Jagini
Class:12
Date of execution:27/7/21
'''

f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UseFunc.txt","r")

print("\n 1.",f.name,"is the file name of the text file")
#returns file name

f_contents=f.read()
print("\n\n 2.Read contents displayed below using the read function:\n")
print(f_contents)
#reads all contents of file

f.seek(0)
#Used to change position of pointer
f_contents=f.readlines()
print("\n\n 3. Read contents displayed below using the readlines function:\n")
print(f_contents)

f.seek(0)
f_content1=f.readline()
print("\n \n 4. Read contents displayed below using the readline function:\n")
print(f_content1)

f.seek(0)
print(" \n\n 5. Another way of displaying using a for loop\n")
for line in f:
    print(line,end="")
f.seek(0)
f_contents=f.read(5)
print(" \n\n\n 6. Read contents (5 characters in this case) is displayed below: \n")
print(f_contents)

print("\n\n 7.",f.tell(),"is the position of the pointer after reading 5 characters using the tell function")

f.close()

'''
f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UseFunc.txt","a+")
f.writelines(["Computers is my cup of tea.","I love it"])
print("\n\n 8.Output on appending using writelines function")
print(f.read())
f.close()

f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UseFunc.txt","w+")
f.write("Computers is really cool.")
print("\n\n 9.Output on using write function")
f.seek(0)
print(f.read())



f.close()
'''
