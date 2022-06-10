# inheritance

# class A():
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B(A):                                       #inherit method
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# a=A()
# a.Feature1()
# a.Feature2()
#
# b=B()
# b.Feature3()
# b.Feature4()
# b.Feature1()                            ##object can access class A features as well
# b.Feature2()


######################################################################################
# We can call A as super class/parent class
# we can call B as child class
# this is a single level inheritance

#########################################################################################
# Multi-level inheritance

# class A():
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B(A):                                       #inherit method
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# class C(B):                                       #inherit method
#     def Feature5(self):
#         print("Feature 5 is working")
#     def Feature6(self):
#         print("Feature 6 is working")
#
# a=A()
# a.Feature1()
# a.Feature2()
#
# b=B()
# b.Feature3()
# b.Feature4()
# b.Feature1()                            ##object can access class A features as well
# b.Feature2()
#
# c=C()                                           ##we can access both A and B classes
# c.Feature1()
# c.Feature2()
# c.Feature3()
# c.Feature4()
# c.Feature5()
# c.Feature6()

####################################################################
# 3.Multiple inheritance

# class A:
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B:                                       #inherit method
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# class C(A,B):                                       #Multiple method by coma seperation
#     def Feature5(self):
#         print("Feature 5 is working")
#     def Feature6(self):
#         print("Feature 6 is working")
#
# a=A()
# a.Feature1()
# a.Feature2()
#
# b=B()
# b.Feature3()
# b.Feature4()
#
# c=C()                                           ##we can access both A and B classes
# c.Feature1()
# c.Feature2()
# c.Feature3()
# c.Feature4()
# c.Feature5()
# c.Feature6()

########################################################################################
# passing init vaiables from A to B

# class A():
#     def __init__(self):
#         print("in A init")
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B(A):                                       #inherit method
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# a=A()
# a.Feature1()
# a.Feature2()
#
# b=B()           ##in creating object init in A will be initiated
# b.Feature3()
# b.Feature4()
# b.Feature1()                            ##object can access class A features as well
# b.Feature2()

###################################################################################
# while both having init constructor

# class A():
#     def __init__(self):
#         print("in A init")
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B(A):                                       #inherit method
#     def __init__(self):
#         super().__init__()                  ##we can't use this if there is multiple parent class and it calls onle
#                                                   the first class in input
#         print("in B init")
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# b=B()           ##in creating object init in A will be initiated

#########################################################
# while having more than 1 parent class with init

# class A:
#     def __init__(self):
#         print("in A init")
#     def Feature1(self):
#         print("Feature 1 is working")
#     def Feature2(self):
#         print("Feature 2 is working")
#
# class B:
#     def __init__(self):
#         print("in B init")
#     def Feature3(self):
#         print("Feature 3 is working")
#     def Feature4(self):
#         print("Feature 4 is working")
#
# class C(A,B):                             #Multiple method by coma separation
#     def __init__(self):
#         A.__init__(self)                   ##while having more than one parent, class.init(self) will only work
#         B.__init__(self)
#         print("in C init")
#     def Feature5(self):
#         print("Feature 5 is working")
#     def Feature6(self):
#         print("Feature 6 is working")
#
# c=C()
# print(C.mro())

#################################################################
# class A:
#     def __init__(self):
#         print("in A init")
#     def Feature(self):
#         print("Feature A is working")
#
# class B:
#     def __init__(self):
#         print("in B init")
#     def Feature(self):
#         print("Feature B is working")
#
# class C(A,B):                             #Multiple method by coma separation
#     def __init__(self):
#         super().__init__()                  ##while having more than one parent,class.init(self) will only work
#         B.__init__(self)
#
# c=C()
# c.Feature()                                     #only th first feature will work
# print(C.mro())

######################################################################
# Example

# class school:
#     name="ABC"
#     def Display1(self):
#         print("Its a high school")
#
# class student(school):
#     def __init__(self,rno):
#         self.RollNo=rno
#     def Display2(self):
#         print("NAme:",self.name)
#         print("ROLLNO:",self.RollNo)
#
# std=student(15)
# std.Display2()
# std.Display1()

####################################################################################
# both having init constructor

# class school:
#     def __init__(self,name):
#         self.name = name
#     def Display1(self):
#         print("Its a high school")
#
# class student(school):
#     def __init__(self,rno,x):
#         super().__init__(x)
#         self.RollNo=rno
#     def Display2(self):
#         print("NAme:",self.name)
#         print("ROLLNO:",self.RollNo)
#
# std=student(15,"XYZ")
# std.Display2()
# std.Display1()

#############################################################################################
# create a a parent class "student" instant variable name,class,rollno
# child class marksheet marks in list
# create a method to print details and total marks

# class student:
#     def __init__(self,name,clss,rollno):
#         self.name = name
#         self.clss=clss
#         self.rollno=rollno
#
# class marksheet(student):
#     def __init__(self,marks,name,cls,rollno):
#         self.marks=marks
#         super().__init__(name,cls,rollno)
#     def display(self):
#         print("name:",self.name,"\nrollno:",self.rollno,"\nClass:",self.clss,"marks:",self.marks,"total marks:",
#                           sum(self.marks))
#
# std=marksheet([12,18,20,10],"Jenicks",10,456)
# std.display()
#
###############################################################################
# another method

# class student:
#     def __init__(self,name,clss,rollno):
#         self.name = name
#         self.clss=clss
#         self.rollno=rollno
#     def display1(self):
#         print("name:", self.name, "\nrollno:", self.rollno, "\nClass:", self.clss)
# class marksheet(student):
#     def __init__(self,marks,name,cls,rollno):
#         self.marks=marks
#         super().__init__(name,cls,rollno)
#     def display(self):
#         self.display1()
#         print("marks:",self.marks,"\ntotal marks:",sum(self.marks))
#
# std=marksheet([12,18,20,10],"Jenicks",10,456)
# std.display()

##########################################################################
# Q create a bank application.
#          : "Account"-parent class, with a "BankName: ABC bank,IFSCcode :
#          45154,Balance" as class variables. inital balace "10000"common
#          to all customer.
#         :"AccountHolder"-child class, with instance variables "name,AccNo"
#          and functions "Deposit,widrow,Balacecheck" .
#         : if the user use any of these method by passing an amount,
#          we want to get full bank details and  current balance .
#         : for balance checking no need to pass any amount.
#         : provided min balance required is limited to 1000.

# ### ANS::

# class Account:
#     BankName="Abc"
#     IFSCcode=45154
#     InitBalance=10000

# class AccountHolder(Account):
#     def __init__(self,Name,AccNo):
#         self.name=Name
#         self.accno=AccNo
#     def Deposit(self,amount):
#         self.InitBalance=self.InitBalance+amount
#         print("amount deposited:",amount)
#         print("Balance Amount:",self.InitBalance)
#     def Widraw(self,amount):
#         x=self.InitBalance-amount
#         if x>1000:
#             print("amount",amount,"has wihdrawed")
#             self.InitBalance = self.InitBalance - amount
#         else:
#             print("insufficient balance")
#     def Balance(self):
#         bal=self.InitBalance
#         print("The Balance is ",bal)
#


# bnk=AccountHolder("alen",1546468)
# bnk.Deposit(1200)
# bnk.Widraw(1000)
# bnk.Balance()


# polymorphism::  2 tyoes 1. method overriding 2.operator overriding

# 1. method overriding: in case of inheritance,when parent method is redefined by child case

# example
# class A:
#     def test(self):
#         print("inside A")
# class B(A):
#     def test1(self):
#         print("inside B")
#
# b=B()
# b.test()
#
#
#
# class A:
#     def test(self):
#         print("inside A")
#
# class X:
#     def test(self):
#         print("inside X")
#
# class B(A):
#     def test1(self):
#         print("inside B")
#
# class C(X):
#     def test(self):
#         print("inside C")
# class D(B,C):
#     pass
#
# x=D()
# x.test()               #it shows the statement in A  ##it first check in d thengo to b then a and
#                               at last in c if other not available
#
# print(D.mro())
#
#
#
#######################################################################
# class Account():
#     def __init__(self,cId,accountNo,Name):
#         self.customerid=cId
#         self.accountNo=accountNo
#         self.Name=Name
#
#     def display(self):
#         print("Customer Id:",self.customerid)
#         print("Account Number:",self.accountNo)
#         print("Name:",self.Name)
#
# class Savingsaccount(Account):
#     def __init__(self,cId,accountNo,Name,amount,intRate):
#         super().__init__(cId,accountNo,Name)
#         self.amount=amount
#         self.intRate=intRate
#     def display(self):
#         super().display()
#         print("Amount:",self.amount)
#         print("Interest Rate:",self.intRate)
#
# c1=Savingsaccount(111,22222,"anoop",25000,8.5)
# c1.display()


#################################################
# 2.operator overloading
#

# a=5
# b=6
# print(int.__add__(a,b))
# c="hai"
# d=" hello"
# print(str.__add__(c,d))

# example::
# class Marks:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self, other):   ##adding function on a class
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         Ob= Marks(m1,m2)              #created an object
#         return Ob
# s1=Marks(10,25)
# s2=Marks(5,20)
#
# s3=s1+s2
# print(s3.m1)
# print(s3.m2)

##############################
# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#
#     def __gt__(self, other):
#         if (sum(self.marks)>sum(other.marks)):
#             return self.name+" has scored more marks"
#         else:
#             return other.name+" has scored more marks"
#
# s1=student("akhil",12,[98,70,80])
# s2=student("alen",15,[98,70,85])
# print(s1>s2)

#########################################################################
# abstraction
# from abc import ABC,abstractmethod         #step 1: from abc import ABC,abstractmethod
# class computer(ABC):                       #step2: we have to inherit ABC to a class
#     @abstractmethod           #step3: we have to make atleast one function inside abstract method to use the function
#     def process(self):
#         pass
#     def dis(self):
#         print("hi")
#
# class Laptop(computer):
#     def process(self):        #if we want to use a function in abstraction method we have to use the same
#                                       #function name on another class
#         print("it is running")
#
# com=Laptop()
# com.process()
# com.dis()


###############################################################
# from abc import ABC,abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def nSide(self):
#         pass
#     def display(self):
#         print("non-abstract method")
#
# class square(Polygon):
#     def nSide(self):
#         return "4 sides"
#
# class triangle(Polygon):
#     def nSide(self):
#         return "3 sides"
#
# obj=square()
# print(obj.nSide())
# obj.display()
#
# obj=triangle()
# print(obj.nSide())
# obj.display()

#######################################################################
#####################################################################
##########################################################################################################
###############################################################################################

# Exception handling
# we have normal as well as critical statements
# if any statements have chance of error then this statement is called critical statements
# a=5
# b=0
# print(a/b)   ###this is a critical statement

# a=5
# b=0
# try:
#     print(a/b)
# except Exception:
#     print("you cant divide by 0")
# print("hai")
#
# ######################################################
# a=5
# b=0
# try:
#     print(a/b)
# except Exception as e:              ##if we want to know what type of error it is we have to
#                                          #assign exception into a letter and print that
#     print(e)
#     print("you cant divide by 0")
# print("hai")

########################################################
# a=5
# b=0
# try:
#     print("resources were opened")
#     print(a/b)
# except Exception as e:
#     print("you cant divide by 0: ",e)
# finally:                                     ##if have to add some statement after the error statement
#     print("resources were closed")
# print("hai")

##############################################################
# a=5
# b=2
# try:
#     print("resources were opened")
#     print(a/b)
#     k=int(input("enter a number"))
#     print(k)
# except ZeroDivisionError as e:                         #we can give errors instead of exception class
#     print("a number cannot be divided by 0:: ",e)
# except ValueError as e:
#     print("type error:: ",e)
# except Exception as e:
#     print("Something went wrong...:: ",e)
# finally:                                     ## If have to add some statement after the error statement
#     print("resources were closed")
# print("hai")

#########################################################################
# def div():
#     try:
#         a=int(input("enter a number:"))
#         b=int(input("enter a number:"))
#         result=a/b
#         print(result)
#     except ValueError as e:
#         print("enter a numeric value.",e)
#     except ZeroDivisionError as e:
#         print("number cannot be divided by 0",e)
#     except Exception as e:
#         print("something went wrong...",e)
#     else:
#         print("no error")
#     finally:
#         print("final part")
#
# div()

###################################################################################
# class AccountNumberError(Exception):
#     pass
# class NotEnoughBalanceError(Exception):
#     pass
#
# accInfo={"111":1000,"222":2000}
# def call(a,m):
#     try:
#         amount=m
#         accountNumber=a
#         print("amount recieved is",m)
#         print("account no:",a)
#         if accountNumber not in accInfo:
#             raise AccountNumberError()
#         if amount >accInfo[accountNumber]:
#             raise NotEnoughBalanceError()
#     except AccountNumberError:
#         print("account number is incorrect")
#     except NotEnoughBalanceError:
#         print("not having enough balance")
#     except Exception as e:
#         print("something went wrong:: ")
#         print(e)
#     else:
#         print("it works")
#
# call("111",5000)

##########################################################################
##############################################################################
###############################################################################
# accInfo={}
# class AccountNumberError(Exception):   #declearing its an error
#     pass
# class NotEnoughFundError(Exception):
#     pass
#
# class Account:
#     BankName= "ABC Bank"
#     IFSCcode="ABC00260"
#     Balance = 10000
# class AccountHolder(Account):
#     def __init__(self,name,accno):
#         self.Name=name
#         self.Accno=accno
#     def info(self):
#         print("Bank :",self.BankName)
#         print("IFSC :",self.IFSCcode)
#         print("Name :",self.Name)
#         print("Accno. :",self.Accno)
#     def Deposit(self,amountD):
#         self.Balance+=amountD
#         accInfo[self.Accno]=self.Balance
#         self.info()
#         print("your current balance is: ",accInfo[self.Accno])
#         print("..........Thank you...........")
#
#     def widrow(self, amountW):
#         try:
#             amount = amountW
#             accountNumber = self.Accno
#             print("account no is: ", accountNumber)
#             print("amount received is: ", amountW)
#             if accountNumber not in accInfo:
#                 raise AccountNumberError()
#             if amount > accInfo[accountNumber] - 1000:
#                 raise NotEnoughFundError()
#         except AccountNumberError:
#             print("account no incorrect")
#         except NotEnoughFundError:
#             print("insufficient fund")
#             self.info()
#             print("your current balance is: ", accInfo[accountNumber])
#             print("..........sorry...........")
#         except Exception as e:
#             print(e)
#             print("sorry, something wrong !!")
#         else:
#             print ("No exception !!!!")
#             self.Balance-=amountW
#             accInfo[accountNumber]=self.Balance
#             self.info()
#             print("your current balance is: ", accInfo[accountNumber])
#             print("..........Thank you...........")
#     def balanceCheck(self):
#         self.info()
#         print("current balance is : ",accInfo[self.Accno])
#         print("..........Thank you...........")
# AccHolder={}
# def addCustomer(name,num):
#     c1=AccountHolder(name,num)
#     AccHolder[c1.Accno] = c1
#     accInfo[c1.Accno] = c1.Balance
#     print(accInfo)
#     print(AccHolder)
# def transaction():
#     NUM = int(input("Enter your acc Number:"))
#     try:
#         if NUM not in AccHolder:
#             raise AccountNumberError()
#     except AccountNumberError:
#         print("account no incorrect")
#     else:
#         c = AccHolder[NUM]
#         x = int(input("Enter 1 for balance,2 for Deposit,3 for widrow,0 for exit : "))
#
#         if x == 1:
#             c.balanceCheck()
#         elif x == 2:
#             a = int(input("enter amount to dpost: "))
#             c.Deposit(a)
#         elif x == 3:
#             a = int(input("enter amount to widrw: "))
#             c.widrow(a)
# while True:
#     value=int(input("Enter a number, 1 for Create an account, 2 for Existing user,0 for exit : "))
#     if value==1:
#         name=input("Enter your name: ")
#         num=int(input("Enter a new account number: "))
#         addCustomer(name,num)
#     elif value==2:
#         transaction()
#     else:
#         break
#
# print("hii")
# print(accInfo)
#
#
####################################################################################################
################################################################################################
# AccountDetails={}
# class AccountNumberError(Exception):
#     pass
# class NotEnoughBalanceError(Exception):
#     pass
#
# class Account:
#     BankName="Abc"
#     IFSCcode=45154
#     InitBalance=10000
#
# class AccountHolder(Account):
#     def __init__(self,Name,AccNo):
#         self.name=Name
#         self.accno=AccNo
#     def Deposit(self,amount):
#         self.InitBalance=self.InitBalance+amount
#         print("amount deposited:",amount)
#         print("Balance Amount:",self.InitBalance)
#     def Widraw(self,amount):
#         x=self.InitBalance-amount
#         if x>1000:
#             print("amount",amount,"has wihdrawed")
#             self.InitBalance = self.InitBalance - amount
#         else:
#             print("insufficient balance")
#     def Balance(self):
#         bal=self.InitBalance
#         print("The Balance is ",bal)
#
#
# def CreateAccount():
#
#

# bnk=AccountHolder("alen",1546468)
# bnk.Deposit(1200)
# bnk.Widraw(1000)
# bnk.Balance()
#
#
#
#####################################################################
#######################################################################
# class Top:
#     def __iter__(self):       ##it gives the object of the iterator
#         self.num=1
#         return self
#     def __next__(self):         ##it will gives next value/object
#         if self.num<=5:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration      # if statement is not used in there will be infinite
# 
# values=Top()
# for i in values:
#     print (i)

############################################################
# create an iter object with increment 2,starting from 1 and end with the number user gives
#
# class New:
#     def __init__(self,number):
#         self.number=number
#     def __iter__(self):
#         self.num=0
#         return self
#     def __next__(self):
#         if self.num<=self.number:
#             val=self.num
#             self.num+=2
#             return val
#         else:
#             raise StopIteration
#
# number=int(input("enter a number: "))
# values=New(number)
# for i in values:
#     print (i)
##############################################################
#or
######################################
# class NumSeries:
#    def __init__(self,start , end, inc):
#        self.max = end
#        self.num = start
#        self.inc = inc
#    def __iter__(self):
#        return self
#    def __next__(self):
#        self.num = self.num + self.inc
#        if (self.num <= self.max):
#            return self.num
#        else :
#            raise StopIteration()
# a=int(input("enter a num: "))
# b=int(input("enter a num: "))
# c=int(input("enter step: "))
# # # #
# val=NumSeries(a,b,c)
# for i in val:
#     print(i)

####################################################################
################################ # object attributes
######################
# class Student:
#     """its a student class"""
#     school="abc"
#     def __init__(self,name,id,age):
#         self.name = name
#         self.id = id
#         self.age = age
# # # # #
# s = Student("John",101,22)
# s1 = Student("Johnson",102,28)
# print(s.__doc__)    #for doc string
# print(s.__dict__)   # for creating an object to a dict
# print(s1.__dict__)   # for creating an object to a dict
# print(s.__getattribute__("name")) # to get instance variable/attribute value
# print(s.__getattribute__("id")) # to get instance variable/attribute value

###########################################################
#########################################################
######################## property decorater
# class Student:
#     def __init__(self,no,name,mark):
#         self.rollno=no
#         self.name=name
#         self.marks=mark
#     @property
#     def msg(self):
#         return self.name+" obtained "+str(self.marks)
# obj=Student(1,"alan",90)
# print(obj.name)
# print(obj.marks)
# print(obj.msg)
# obj.name="anju"
# print(obj.name)
# print(obj.msg)

## if we use @property - this decorater allow the function act like an attribute same as values inside init constructors
















