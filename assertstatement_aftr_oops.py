# assert statement is used to check whether the condition is wrong
# def get_age(age):
#     assert age>0 , "age cant be negative"
#     print("your age is:",age)
# #
# get_age(10)
#
#######################
# a=int("enter a number: ")
# print(a)
# assert a>0,"its a negative number"
# print("value is :",a)                   #this will only work if the assert statement is wrong
########################
# write a user defined function to find the avg of list
# a=[1,2,2,5]
###ssert function : the list should not be empty
# def list_1(a):
#     total = len(a)
#     assert total > 0 ,"empty list"
#     sum1=sum(a)
#     print("avg:",sum1/total)
#
# list_1([1,2,2,5])
#
#
#
###############################################
## generator functions if we use return it will get only 1 value so we have to use yeild instead of return
# def getSeries():
#     for i in range(10):
#         print("value:",i)
#         yield i    ##yield can preserve its state
#
# a=getSeries()
# print(a)
#
# for i in a:
#     print(i)

######################################################
# def prt():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# a=prt()
# for i in a:
#     print(i)
































































