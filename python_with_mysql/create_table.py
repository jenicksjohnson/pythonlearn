### Creating a connection from mysql
#
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection
#
# # ### Creating table
#
# def createtable():
#     con=getconnection()
#     cursor=con.cursor()    ##used to cntrol structure that enables travelsal
#     cursor.execute("create table employee (Id int primary key,Email varchar(30),Name varchar(30),Roll_no int,Salary int,Dept varchar(30))")
#     con.commit() ##by default python or connector does not auto commit
#                     #it is an important method
#     cursor.close()
#     con.close()
#
# createtable()


### Creating sql database

# import mysql.connector as m
# connection=m.connect(host="localhost",user="root",password="root")
#
# db_cursor=connection.cursor()
# db_cursor.execute("CREATE DATABASE my_db")
# db_cursor.execute("SHOW DATABASES")
# ### for printing all databases::
# for i in db_cursor:
#     print(i)
# db_cursor.close()
# connection.close()


### printing values in a table on mysql

# def selectData():
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("select * from emp_data")
#     result=cursor.fetchall()
#     con.commit()
#     cursor.close()
#     con.close()
##     print(result)
    # for i in result:
    #     print(i)
#
# selectData()

#### inserting values into a sql table
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection
#
# def insertstudent():
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("insert into employee values (1,'a@gmail.com','alan',1155,10500,'mech')")
#     con.commit()
#     cursor.close()
#     con.close()
#
# insertstudent()

###inserting  multiple values::
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection

# def insertstudent(id,email,name,rollno,salary,dept):
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s)",(id,email,name,rollno,salary,dept))
#     con.commit()
#     cursor.close()
#     con.close()
#
# insertstudent(1,"a@gmail.com","alex",1155,10600,"civil")
# insertstudent(3,"fg@gmail.com","alice",1158,11500,"mech")

### fetching all data


# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection

# def selectdata():
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("select * from new_employee1")
#     result=cursor.fetchall()
#     con.commit()
#     cursor.close()
#     con.close()
#     for i in result:
#         print(i)
#
# selectdata()

### deleting an item from a table::
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection
#
# def selectdata(id):
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("delete from employee where id = (%s)",(id,))
#     con.commit()
#     cursor.close()
#     con.close()
#
# selectdata(1)

### updating a table
# import mysql.connector as m
# def getconnection():
#     connection=m.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection

# def selectdata(id,name):
#     con=getconnection()
#     cursor=con.cursor()
#     cursor.execute("update employee set name= %s where id = (%s)",(name,id))
#     con.commit()
#     cursor.close()
#     con.close()
#
# selectdata(2,"Dev")


# getting details by giving Id as input

# import mysql.connector as max
# def getconnect():
#     connection=max.connect(host="localhost",user="root",password="root",database="studentdb")
#     return connection

# def selecteddata(id):
#     con=getconnect()
#     cursor=con.cursor()
#     cursor.execute("select * from new_employee1 where Id =(%s)",(id,))
#     result=cursor.fetchall()
#     con.commit()
#     cursor.close()
#     con.close()
#     print(result)

# new=int(input("Enter the Id: "))
# selecteddata(new)
