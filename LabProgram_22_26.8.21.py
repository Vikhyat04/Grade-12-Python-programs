#Program 22

#A binary file "book.dat" has structure[Book no,Book Name,Author,Price]
#
#(a)Write a user defined function createfile() to input for a record and add to book.dat
#(b)Write a function countrec(Author) in Python which accepts the Author name as parameter
#   and count and return number of books by the given Author stored in the binary file 'book.dat'

#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 26/08/2021
import pickle
def createfile():
    f=open(r"C:\Python\Class 12 python\Lab Programs\BinaryFiles\book.dat",'ab')
    BookNo=int(input("Book no:"))
    Book_Name=input("Book Name:")
    Author=input("Author Name:")
    price=int(input("Book price:"))
    rec=[BookNo,Book_Name,Author,price]
    pickle.dump(rec,f)
    f.close()
def countrec(Author):
    f=open(r"C:\Python\Class 12 python\Lab Programs\BinaryFiles\book.dat",'rb')
    num=0
    try:
        while True:
            rec=pickle.load(f)
            if (Author==rec[2]):
                num=num+1
                print(rec[0],rec[1],rec[2],rec[3])
    except:
        f.close()
        return num
w=int(input("Enter number of books you want to enter:"))
for i in range (0,w):
    createfile()
name=input("Enter name of author you want to search for:")
n=countrec(name)
print( name+" wrote ",n,"books in file")
