''' Write a program to read the contents of a file and replace all space characters
with '#'


Name:Vikhyat Jagini
Class:12
Date of execution:27/7/21
'''

def rep():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\replace#.txt","r+")
    s=f.read()
    str=""
    for i in s:
            if(i==" "):
                str=str+"#"
            else:
                str=str+i
    f.seek(0)
    f.write("Output:"+str)
    f.close()
rep()

