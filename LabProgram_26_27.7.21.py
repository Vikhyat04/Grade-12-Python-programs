#Program 26

#Write a Program to remove the lines with the letter 'a' in a file and write it to another file.


#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 27/07/2021


f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\input26.txt","r")
r=f.readlines()

def wFile(r):
    wList=[]
    for i in r:
        if "a" not in i.lower():
            wList.append(i)
    return wList
wList=wFile(r)
f.close()
f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\output26.txt","w")
f.writelines(wList)
f.close()
