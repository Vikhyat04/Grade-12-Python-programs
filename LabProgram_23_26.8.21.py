#Program 23


#Consider the following definition of dictionary Member.
#Member={'Member No.':_________,'Name':______}
#Write contents into a binary file

#Name: Vikhyat Jagini
#Class: 12
#Date of Execution: 26/08/2021

import pickle
f=open(r"C:\Python\Class 12 python\Lab Programs\BinaryFiles\test.dat",'wb')
while True:
    dic={}
    no=int(input("Enter member number:"))
    name=input("Enter name:")
    dic["Member No"]=no
    dic["Name"]=name
    pickle.dump(dic,f)
    user=input("If you want to enter more members, enter yes or else, enter no:")
    if (user!="yes"):
        break
print("Thank you")
f.close()
    
