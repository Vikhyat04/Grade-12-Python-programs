#Write a program to count the number of vowels present in text file
f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\vowelsCount.txt","r")
def countV():
    str=f.read()
    count=0
    for i in str:
        if i in "aeiouAEIOU":
            count=count+1
    print("Number of vowels in text file:",count)
    f.close()
countV()
