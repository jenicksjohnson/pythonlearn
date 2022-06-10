# for files
import os

# for renaming a text file
# os.rename("sample1.txt","test.txt")

# file=open("sample1.txt","w")
# file.write("abcd")
# file.close()

# for deleting a file
# os.remove("sample1.txt")

# directory/folder
# print(os.getcwd())  #to know crnt working directory
# os.mkdir("sample")  #to create a folder in crnt working directory
# os.chdir("./sample")   #to change current directory
# print(os.getcwd())
# file=open("sample.txt","w")
# file.write("hello")
# file.close()

# os.chdir("../")  #to go back to the directory
# print(os.getcwd())

# f=open("sample/sample.txt","r") #going to the file in another dir
# print(f.reading_file())
# f.close()

# for deleting folder ::
# os.rmdir("sample")  # work only if the dir is empty
# or
# import shutil
# shutil.rmtree("sample")  # removes folder even if it does have any files inside

##
# by os.rmdir
# os.mkdir("sample234")
# os0.rmdir("sample234")

# print(os.listdir())   ##print files in the current dir


# file=open("sample2.txt","w")
# file.write("111,a1@gmail.com,Ann,17000,Production")
# file.close()
#
# file=open("sample2.txt","a")
# file.write("\n112,b@gmail.com,Tina,19000,Development")
# file.close()
#
# file=open("sample2.txt","a")
# file.write("\n113,c@gmail.com,Anju,21000,Accounts")
# file.close()
#
# file=open("sample2.txt","a")
# file.write("\n114,v1@gmail.com,Anu,20000,Hr")
# file.close()
#
# file=open("sample2.txt","a")
# file.write("\n115,g1@gmail.com,Bibin,19000,Hr")
# file.close()
#
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection

# def create():
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("create table new_employee1 (Id INT,Email VARCHAR(30),Name VARCHAR(30),Salary INT,Field VARCHAR(30))")
#     con.commit()
#     cursor.close()
#     con.close()

# create()

# def insert(id,email,name,salary,field):
#     con = getconnection()
#     cursor = con.cursor()
#     cursor.execute("INSERT INTO new_employee1 values (%s,%s,%s,%s,%s)",(id,email,name,salary,field))
#     con.commit()
#     cursor.close()
#     con.close()

# def insert(a,b,c,d,e)
# file=open("sample2.txt","r")
# value=file.readlines()
# value=abc.split(", ")
# print(abc)
# values=[]
# for i in value:
#     line=i.strip("\n")
#     words=line.split(",")
##     print(words)
    # insert(words[0],words[1],words[2],words[3],words[4])
# print(values)

















































