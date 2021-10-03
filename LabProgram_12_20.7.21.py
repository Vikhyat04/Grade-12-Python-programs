#Write a program to read a file named "abc.txt" and copy these contents
#into another file name "xyz.txt"

#Name:
#Class:
#Date of Execution:

def copy():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\abc.txt","r")
    f1=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\xyz.txt","w")
    while True:
        c=f.read(1)
        if not c:
            break
        f1.write(c)       
    f.close()
    f1.close()
copy()
    
