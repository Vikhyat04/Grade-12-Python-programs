
'''
PROGRAM 19

Write a program to perform all operations of binary file.

Name:Vikhyat Jagini
Class:12
Date of Execution: 11/08/2021
'''

import pickle
def write():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'wb')
    record=[]
    while True:
        rn=int(input("Enter roll no:"))
        nam=input("Enter name:")
        ma=int(input("Enter marks:"))
        data=[rn,nam,ma]
        record.append(data)
        ch=input("Press y to continue, n to end:")
        if ch=='n':
            break     
    pickle.dump(record,f)
    f.close()

def read():
    f1=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'rb')
    while True:
        try:
            s=pickle.load(f1)
            print(s)
            for i in s:
                print(i)
        except Exception:
            break

def append():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'rb+')
    rec=pickle.load(f)
    while True:
        rn=int(input("Enter roll no:"))
        nam=input("Enter name:")
        ma=int(input("enter marks:"))
        data=[rn,nam,ma]
        rec.append(data)
        ch=input("Press y to continue, n to end:")
        if ch=='n':
            break
    f.seek(0)
    pickle.dump(rec,f)
    f.close()

def search():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'rb')
    found=0
    rno=int(input("Enter rollno whose record to be found:"))
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i[0]==rno:
                    print(i)
                    found=1
                    break
    except Exception:
        f.close()
    if found==0:
        print("No record found")


def update():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'rb+')
    r=int(input("Enter rollno whose record to be updated:"))
    f.seek(0)
    try:
        while True:
            rpos=f.tell()
            s=pickle.load(f)
            print(s)
            for i in s:
                if i[0]==r:
                    print("Current Name=",i[1])
                    found=1
                    i[1]=input("Enter name:")
                    f.seek(rpos)
                    pickle.dump(s,f)
                    break
    except Exception:
        f.close()
        
    if found==0:
        print("No record found")
    
            

def delete():
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'rb')
    s=pickle.load(f)
    print(s)
    f.close()
    rno=int(input("Enter rollno whose record to be deleted:"))
    f=open(r"C:\Python\Class 12 python\Lab Programs\TextFiles\UsebinFunc.txt",'wb')
    reclst=[]
    for i in s:
        if i[0]==rno:
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    
    f.close()

def MainMenue():
    print("SELECT YOUR OPTION")
    print("1.WRITE DATA")
    print("2.READ DATA")
    print("3.APPEND DATA")
    print("4.SEARCH DATA")
    print("5.UPDATE DATA")
    print("6.DELETE DATA")
    print("7.EXIT")
    ch=int(input("Enter your choice:"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        append()
    elif ch==4:
        search()
    elif ch==5:
        update()
    elif ch==6:
        delete()
    elif ch==7:
        exit(0)



MainMenue()
    
