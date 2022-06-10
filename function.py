# Functions

###############################################################
# def function_name():
#     """To print an Output"""
#     print("Hai")
#     print("Hai")
# print("Outside")
# function_name()
#
################################################################
# To print doc string on the program
# print(function_name.__doc__)

# print(len.__doc__)

#################################################################
# return and no argument
# def add():
#     a=5
#     b=3
#     sum=a+b
#     ### print("hello")
#     return sum
#     ### print("hello")
# x=add()
# print(x)
# print("result",add())

###############################################################
#  arguments but no returns
# def avg_number(x,y):
#     print("average of",x,"and",y,"is :",(x+y)/2)
#     print(x+y)
#     print(x-y)
#     print((x+y)/2)
# avg_number(10,3)
# avg_number(20,10)
# a=90
# b=50
# avg_number(a,b)

##################################################################
# def elements_in_list(a):
#     for i in a:
#         print(i)
#
# l=[1,2,3,4,5,6,7,89]
# elements_in_list(l)

##################################################################
# return and print squares of the sum of 2 & 3
# def sqre(y,x):
#     return (x*x +2*x*y + y*y)
#
# a=2
# b=3
# sqre(a,b)
# print("the square of the sum of the 2 numbers is",sqre(a,b))

# or
# def square():
#     s=(3+2)**2
#     return s
#
# print("squre of the sum is",square())

##################################################################
# type of arguments

# 1.required arguments/position arguments
# def avg(x,y):
#     sum=(x+y)/2
#     print(sum)
# avg(3,4)

##################################################################
# 2.default arguments
# def mn(name,letter,cd="Good Morning"):
#     print(name)
#     print(letter)
#     print(cd)
# mn("akhil","jkl")
##
# def mnb(name,msge="good  morning"):
#     print(msge)
#     print(name)
#     print(name,msge)
# mnb("akhil","msj")
##
# def man3(name,msge1="Good Morning",msge2="morning"):
#     print(msge1)
#     print(name)
#     print(name,msge2)
# man3("akhil","abc")

#################################################################
# 3.Keyword arguments/Named arguments
# def display(x,y):
#     print(x)
#     print(y)
# display(x=10,y=20)
##
# def display2(a,b):
#     print(a)
#     print(b)
# display2(b=34,a=56)

#################################################################
# 4.Variable length arguments(Arbitrary arguments)
# def amd(*args):
#     print("good morning",args)
#     print("Hai all")
# amd("krishna","rohit","manuel")
# ##
# def das(*name):
#     print("Good Morning")
#     print("Hai",name)
# das("rohit","mukesh","sithara")
# ##
# def ert(*args):
#     for name in args:
#         print("Hai",name)
# ert("rohit","max","rakesh")
###################################################################
# finding n  number of functions
# def sum(*args):
#     sum=0
#     for num in args:
#         sum=sum+num
#     return sum
#
# x=sum(1,2,3,4,5)
# print("the sum is ",x)

####################################################################
# 5.Variable length keyword argument
# def man(**kwargs):
#     print(kwargs)
#     print(kwargs['msg3'])
#     print(kwargs["name"])
#     print(kwargs['msg1'])
#     print(kwargs['msg2'])

# man(name="Jeena",msg1="Good Morning",msg2="Have a good day",msg3="Hai")
##
# def man(**value):
#     print(value)
#     print(value['msg3'])
#     print(value["name"])
#     print(value['msg1'])
#     print(value['msg2'])
#
# man(name="Jeena",msg1="Good Morning",msg2="Have a good day",msg3="Hai")

################################################################
# def man(**values):
#     for i,j in values.items():
#         print(i)
#         print(j)
#
# man(name="Jeena",msg1="Good Morning",msg2="Have a good day",msg3="Hai")
##
# def man(**values):
#     for i in values.keys():
#         print(i)
#
# man(name="Jeena",msg1="Good Morning",msg2="Have a good day",msg3="Hai")
##
# def man(**values):
#     for i in values.values():
#         print(i)
#
# man(name="Jeena",msg1="Good Morning",msg2="Have a good day",msg3="Hai")

###################################################################
# q:enter 3 input 3rd one is operator
# def result(x,y,z):
#     if z=="+":
#         results=x+y
#     elif z=="-":
#         results=x-y
#     elif z=="*":
#         results=x*y
#     elif z=="/":
#         results=x/y
#     else:
#         results=x%y
#     return results

# a=int(input("Enter a number"))
# b=int(input("enter the number"))
# c=input("enter the operator(+,-,/,%,*)")
# result(a,b,c)
# print(a,c,b,"=",result(a,b,c))

########################################################################
# rock paper scissor
# def result():
#     x=input("enter the value from player 1\n")
#     y=input("enter the value from player 2\n")
#     if x=="rock" and y== "scissors":
#         print("congratulatons player 1 wins")
#     elif x=="scissors" and y== "paper":
#         print("congratulatons player 1 wins")
#     elif x=="paper" and y== "rock":
#         print("congratulatons player 1 wins")
#     elif y=="rock" and x== "scissors":
#         print("congratulatons player 2 wins")
#     elif y=="scissors" and x== "paper":
#         print("congratulatons player 2 wins")
#     elif y=="paper" and x== "rock":
#         print("congratulatons player 2 wins")
#     else:
#         print("Rematch")
# result()
##or
# def result():
#     x=input("enter the value from player 1\n")
#     y=input("enter the value from player 2\n")
#     if x=="rock" and y== "scissors"or x=="scissors" and y== "paper" or x=="paper" and y== "rock":
#         print("congratulatons player 1 wins")
#     elif y=="rock" and x== "scissors" or y=="scissors" and x== "paper" or  y=="paper" and x== "rock":
#         print("congratulatons player 2 wins")
#     else:
#         print("Rematch")
# result()
# while True:
#     z=input("enter Yes if you want to continue or type No::")
#     if z.lower() == "no":
#         break
#     else:
#         result()


###########################################################################################################
# def add(x,y):
#     return x+y
# def add1(*a):
#     sum=0
#     for i in a :
#         sum=sum+i
#     return sum
# def add2(**a):
#     sum=0
#     for a,b in a.items():
#         sum=sum+b
#     return sum
#
# def add3(x,y,*a,**b):
#     sum=0
#     sum=sum+add(x,y)
#     print(sum)
#     sum=sum+add1(*a)
#     print(sum)
#     sum=sum+add2(**b)
#     print(sum)
#     return sum
#
# sum=add3(10,20,30,40,50,60,70,80,num1=10,num2=20,num3=10,num4=1120)
# print(sum)

##############################################################################################














































