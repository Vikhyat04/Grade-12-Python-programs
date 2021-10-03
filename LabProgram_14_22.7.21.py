#Write a program to count the number of words present in text file
f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\wordCount.txt","r")
def countW():
    str=f.read()
    l=str.split()
    print("Number of words in text file:",len(l))
    f.close()
countW()
