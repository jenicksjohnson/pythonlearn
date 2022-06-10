# global variable
# x=10           ###global variable
# def test():
#     a=10
#     x=20          ### local variable
#     print(x)
# test()
# print(x)
# print(a)

##########################################################
# modify global variable
# x=10
# def tes():
#     x=x+10         """we cant modify global variable inside a def"""
#     print(x)
# tes()

############################################################
# x=10
# def tes():
#     global x
#     x=x+10
#     print(x)
# tes()

##############################################################
# x=10
# y=10
# def tes():
#     global x,y
#     y=y+100
#     x=x+10
#     print(x)
#     print(y)
# tes()
# print(x)
# print(y)

##################################################################
# fn inside a fn
# x=100
# def outer():
#     print(x)
#     def inner():
#         x=10
#         print("innerfn")
#         print(x)
#     inner()
#     print(x)
# outer()

#########################
# def outer(a,b):
#     x=100
#     print("outer side")
#     def add(y):
#         return a+b+x+y
#     sum=add(1)


########################
# x=10
# def outer():
#     x=100
#     def inner():
#         nonlocal x
#         x=x+10
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

############################
# x=100
# def outer():
#     x=111
#     print(x)
#     def inner():
#         nonlocal x
#         x=x+10
#         print(x)
#         def inner2():
#             global x
#             x=x+10
#             print(x)
#         inner2()
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

##########################
# show a list adding 5 number limit with 5
# def lists():
#     k=[]
#     for i in range (5):
#         z=int(input("enter a number::"))
#         k.append(z)
#     print("list is full\n",k)
#
# lists()

### or
# def lists():
#     k=[]
#     for i in range(5):
#         def inside():
#             nonlocal k
#             z=int(input("enter the number::"))
#             k.append(z)
#         inside()
#     print(k)
#
# lists()

#########################################################################




