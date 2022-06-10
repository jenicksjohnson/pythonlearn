
# properties- variables
# method- function

# in inheritance::
# everything will be defined in parent class
# super class and child class

# abstraction :: hiding some methods and properties from user

# polymorphism :: same properties but change its behaviour/same method with different forms


# to define a class::
# class <nameofclass> :
#     statements-variables ==properties
#                 -functions    =method

# class name should start with caps in first letter
# eg:
# class Car:
#     def Spec(self):
#         print("1000cc, hatchback")

# syntax for creating a object::
# object_name=class_name()

# car1= Car()
# print(type(car1))

# to use a function from a class to an object::
# class_name.function_name()
# eg::
# Car.Spec

# car2=Car()
# car2.Spec()


# class Car:
#     def Spec(self):
#         print("1000cc, hatchback")
#
# car1=Car()
# car1.colour="yellow"
# car2=Car()
#
# car1.Spec()
# print (car1.colour)
#
# car2.Spec()
# print (car2.color) ## we havnt defined defined color in colour if we want we have to assign colour in car2 or should be assigned inside th class

# class Car:
#     model="TATA"
#     def Spec(self):
#         print("1000cc, hatchback")
#
# car1=Car()
# car1.Spec()
# print(car1.model)

# in we class we can individually define a variable or string,only in outside
# if we used a function or variable inside a class it will work on every object

# class Car:
#     model="TATA"
#     def Spec(self):
#         print("1000cc, hatchback")
#         print("this is a model of :",self.model)                    #on a function inside a class,if we want to use a varibale given inside a class to a function we have to use self.variabe
#
# car1=Car()
# car1.Spec()
#
# car2=Car()
# car2.model="BMW"
# car2.Spec()
#
# car3=Car()
# car3.Spec()

# qa:: create a class person with function named display
# class Person:
#     age=22
#     name="Jenicks Johnson"
#     def Display(self):
#         print("Name is :",self.name)
#         print("Age::",self.age)
#
# name=Person()
# name.Display()


# p1=Person()
# p1.name="Alen"
# p1.Display()

############################################
# class Person:
#     age=22
#     name="Jenicks Johnson"
#     def Display(self):
#         place="Kochi"
#         print("Name is :",self.name)
#         print("Age::",self.age)
#         print("Place::",place)
#
# name=Person()
# name.Display()

# create a class "student" with properties "rollno,name,age,mark"
# marks input through object
# function-name
# print total marks in it

# class Student1():
#     Rollno=0
#     Name=""
#     Age=0
#     Marks=[]
#     def Properties(self):
#         print("\nDetails of",self.Name,"::\n\nRoll No: ",self.Rollno,"\nName: ",self.Name,"\nAge: ",self.Age,"\nMarks: ",self.Marks,"\nTotal MArks: ",sum(self.Marks))
#
# New1=Student1()
# New1.Rollno=12
# New1.Name="Jenicks"
# New1.Age=22
# New1.Marks=[12,45,18,100]
# New1.Properties()


# __init__() - used to input values from outside

# class Student():
#     def __init__(self,Rollno,Name,Age,Marks):
#         self.Rollno=Rollno
#         self.Name=Name
#         self.Age=Age
#         self.Marks=Marks
#         self.Schoolname="Choice School"
#     def Properties(self):
#         print("\nDetails of",self.Name,"::\n\nSchool Name:",self.Schoolname,"\nRoll No: ",self.Rollno,"\nName: ",self.Name,"\nAge: ",self.Age,"\nMarks: ",self.Marks,"\nTotal MArks: ",sum(self.Marks))
#
#
# New=Student(12,"Jenicks",22,[10,12,18,20])
# New.Properties()
#
# New2=Student(13,"Alen",21,[11,13,26,20])
# New2.Properties()

########################################################################
# class Student():
#     def __init__(self):
#         self.Rollno=int(input("enter the Roll no:"))
#         self.Name=input("enter the Name")
#         self.Age=int(input("enter Age"))
#         # self.Marks=[int(input("enter the marks"))]
#         self.Schoolname="Choice School"
#     def Properties(self):
#         print("\nDetails of",self.Name,"::\n\nSchool Name:",self.Schoolname,"\nRoll No: ",self.Rollno,"\nName: ",self.Name,"\nAge: ",self.Age,"\nMarks: ",self.Marks,"\nTotal MArks: ",sum(self.Marks))
#
#
# New=Student()
# New.Properties()

########################################################################
# class Car():
#     Wheel=4                              ##Wheel is class variable/static variable which is common to use and fixed
#     def __init__(self,x,y):
#         self.Name=x
#         self.Mil=y                    ## name and mil are instance variables. it gives what we input

# Car1=Car("TATA",68)
# print(Car1.Name,Car1.Mil,Car1.Wheel)

# we can call the Class directly
# print(Car.Wheel)

#
# Car.Wheel=6
# Car2=Car("Maruti",78)
# print(Car2.Name,Car2.Mil,Car2.Wheel)
# Car3=Car("BMW",88)
# print(Car3.Name,Car3.Mil,Car3.Wheel)

##############################################################################################################
# Type of methods:
# 1-instance method
# 2-static method
# 3-class method

# 1-instance method:
# inside a method we are passing self,so it is called instance method.
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#
# Student1= student("Alen",12)
# Student1.Id()

# or we can pass values directly
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self,phone):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#         print("Phone Number",phone)
#
# Student1= student("Alen",12)
# Student1.Id(9744480041)

# there are 2 ttypes of instance method
    # 1. Accesor methods - fetch the value of the instance variblles
    # 2. Mutator methods - modify th evalues of varibles

## accessor method
#Example::
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     def get_Name(self):
#         return self.Name
#     def get_Age(self):
#         return self.Age
# Student1= student("Alen",12)
# # Student1.Id()
# print(Student1.get_Name())
# print(Student1.get_Age())        ##- this method to get a value is called accessor method
#
# print(Student1.Name,"\n",Student1.Age)  #- Can use this method also

## Mutator
#Example::
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     def set_Name(self,Value):              ##it set values
#         self.Name=Value
#     def get_Name(self):                    ##it get the values
#         return self.Name
# Student1= student("Alen",12)
# Student1.Id()
# Student1.set_Name("Ajith")
# Student1.Id()
# print(Student1.get_Name())



##2. Class Method     ##fro creating a class mething -- @classmethod
## Example::
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     @classmethod
#     def SchoolInfo(cls):
#         print("\nSchool: ",cls.Schoolname)
#
# Student1= student("Alen",12)
# Student1.Id()
#
## we can call it only by class name
# student.SchoolInfo()


####################################################
# By Passing Values
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     @classmethod
#     def SchoolInfo(cls,x):
#         print("\nSchool: ",cls.Schoolname)
#         print("Student Name :",x)
#
# Student1= student("Alen",12)
# Student1.Id()
#
# ## we can call it only by class name
# student.SchoolInfo("Dev")
# student.SchoolInfo(Student1.Name)          ##We can pass values to class by this method

#                                            ###class method also have another name called factory method

# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     @classmethod
#     def SchoolInfo(cls):
#         x="Dibin"
#         y=23
#         return cls(x,y)           ##class method returns class objects. we can return class values like this
#
# Student1= student("Alen",12)
# Student1.Id()
#
#
# obj3=student.SchoolInfo()
# print(obj3.Name)
# print(obj3.Age)
#
# obj3.Id()



##################################################################
# Static  method::
                               # we cannot use both class and instance method
                               # if we want to perform any specific programs we  use static method
                               # this is called utility tasks


# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     @staticmethod
#     def Info(x,y):
#         print("Location: ",x)
#         print("Age : ",y)
#
# student.Info("Alen",12)


##############################
# class student():
#     Schoolname="Choice School"
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     def Id(self):
#         print("School Name:",self.Schoolname)
#         print("Student Name:",self.Name)
#         print("Student Age",self.Age)
#     @staticmethod
#     def Info(x,y):
#         print("Name: ",x)
#         print("Age : ",y)
#
# Stud1=student("Alen",12)
#
# student.Info(Stud1.Name,Stud1.Age)

###by using static method check a person is eligible for vote or not  by passing values
# class Vote():
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     @staticmethod
#     def Eligible(x,y):
#         if y>=18:
#             print(x,"is Eligible")
#         else:
#             print(x,"is not Eligible")
#
# num1=Vote("Jenicks",19)
# Vote.Eligible(num1.Name,num1.Age)

###########################################################
# from datetime import date
# print(date.today())
# print(date.today().year)
# print(date.today().month)

### by using class and static method find out a person is eligible for vote by inputing birth year

# class Vote():
#     def __init__(self,Name,Age):
#         self.Name=Name
#         self.Age=Age
#     @classmethod
#     def year(cls,a,b):
#         from datetime import date
#         Nam=a
#         Ag=date.today().year-b
#         return cls(Nam,Ag)
#     @staticmethod
#     def Eligible(x,y):
#         if y >= 18:
#             print(x,"is Eligible")
#         else:
#             print(x,"is not Eligible")
#
#
# Name1=Vote.year("Jenicks",2015)
# Vote.Eligible(Name1.Name,Name1.Age)

##############################################################
# WOrkArea
# from datetime import datetime
# def CurrentTime():
#     Now=datetime.now()
#     current_time=Now.strftime("%H:%M:%S")
#     return current_time
#
# x=CurrentTime()
# print(x)
# m=(x.split(":")
# print(m)

# l=["12","23","15"]
# hr1=l[0]
# hr11=int(hr1)
# min1=l[1]
# min11=int(min1)
# m=["13","28","13"]
# hr2=m[0]
# min2=m[1]
# print(hr11)
# print(min11)
# sub=hr11-min11
# print(sub)

































































































































































































