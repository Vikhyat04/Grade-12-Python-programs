
#Program 27

#Write a program to create a CSV file which stores username and password
#(a)Write contents into the file
#(b)Read contents of the file
#(c)Depending on the user name print the password


#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 27/07/2021

import csv

def input_entries():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\passwords.csv","w",newline = "")
    writer = csv.writer(f)
    data = ["Username","Password"]
    writer.writerow(data)
    rec = []
    print("Inputting Entries")
    print("-----------")
    while True:
        username = input("Enter the username:")
        password = input("Enter the password:")
        data = [username,password]
        rec.append(data)
        more_entries = input("Do you want to enter more records?(Y/N)")
        if more_entries in ["N","n"]:
            break
    print("-----------")
    writer.writerows(rec)
    print("Written to the CSV file succesfully.")
    f.close()
    


def read_entries():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\passwords.csv","r")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()

def search ():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\passwords.csv","r")
    reader = csv.reader(f)
    username = input("Enter the username to be searched:")

    next(reader)# To skip the first row
    for i in reader:
        if i[0].lower() == username.lower():
            print(f"Password of the user",i[0] ,"is:",i[1])
            break
    else:
        print("Username is not found.")
    f.close()
    
input_entries()
read_entries()
search()
