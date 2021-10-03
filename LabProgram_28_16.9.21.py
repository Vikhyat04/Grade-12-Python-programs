
#Program 28

#Write a program to create a CSV file containing an item, item number, item prices.
#(i)Write data into the file
#(b)Read data from the file
#(c)Search for an item depending on item number


#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 16/09/2021

import csv


def input_entries():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\products.csv","w",newline = "")
    writer = csv.writer(f)
    data = ["Number","Name","Price"]
    writer.writerow(data)
    rec = []
    print("Inputting Entries")
    print("-----------")
    while True:
        number = int(input("Enter the number of the product:"))
        name = input("Enter the name of the product:")
        price = input("Enter the price of the product:")
        data = [number,name,price]
        rec.append(data)
        more_entries = input("Do you want to enter more records?(Y/N)")
        if more_entries in ["N","n"]:
            break
    print("-----------")
    writer.writerows(rec)
    print("Written to the CSV file succesfully.")
    f.close()
    


def read_entries():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\products.csv","r")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()

def search ():
    f = open(r"C:\Python\Class 12 python\Lab Programs\CSVFiles\products.csv","r")
    reader = csv.reader(f)
    number = int(input("Enter the item number to be searched:"))
    next(reader)# To skip the first row
    for i in reader:
        if ((i[0])== str(number)):
            print("Item found:")
            print(i)
            break
    else:
        print("Item number not found")
    f.close()
    
input_entries()
read_entries()
search()
