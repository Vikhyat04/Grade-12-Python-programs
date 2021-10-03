#Write a program to read a file name "story.txt",count and print the total number of
#alphabets in the file


 #Name:
 #Date of Execution:
 #Class:


def count_a():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\story.txt","r")
    #f points to starting of file
    count=0
    while(True):
        c=f.read(1)
        
        if not c:
            #means come to file
            break
        if((c>='A'and c<='Z')or(c>'a' and c<='z')):
            count=count+1
    print("Total alphabets=",count)
count_a()

            
            

