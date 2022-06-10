###############################################################
### functions
# match()  :it used to test the input string starts with a specific pattern or not.
# search() : to test a specified pattern is present or not in string.
#           :it return a match object.
#           : we have diff. methods to display the result
#           :start()-starting position of occurrence
#           :end()-ending pos.
#           :span()-tuple of start and end pos.
#           :string()-actual string
# findall() :to find duplicates of specified pattern in the string.(how many times as a list).else empty list.
# split() : how we can split a string using an expression.
# sub() : to replace the sub string using a pattern.


###match():
# it used to test the input string starts with a specific pattern or not.
# on success, it return the match object with its position.
# on failure, it return None

####################### #eg
# import re
# line="python is an object-oriented programming language"
# r1=re.match('pyth',line)
# r2=re.match('pth',line)  ##it will not work because line not starts with pth
# print(r1)
# print(r2)

######################################
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# print(line)
# r1=re.match('Python',line)          #python with p caps is in the second line and match works only with the starting line of a string
# print(r1)
#
####                      #we can use if statement
# if r1:
#     print("yes we got a match from string")
# else:
#     print("nothing found")
#
#################################################################################
# 3.findall
# import re
# line="python is an object-oriented programming language \npython is interpreted"
# x=re.findall('pyth',line)
# print(x)

############################################################################
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.findall('o',line)
# print(x)

###########################################################################
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x1=re.findall('xyz',line)
# print(x)

###########################################################################
######################################################################
# 2.search
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.search('Pyth',line)
# print(x)
#
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.search('Pyth',line).start()
# print(x)
#
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.search('Pyth',line).end()
# print(x)
#
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.search('Pyth',line).group()
# print(x)
#
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x1=re.search('Pyth',line).span()
# print(x)

# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.search('Pyth',line)
# print(x.start())

#################################################################################
#4.split
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.split(' ',line)
# print(x)
#
# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.split('p',line)
# print(x)

# import re
# line="python is an object-oriented programming language \nPython is interpreted"
# x=re.split(' ',line,2)   ###2-maximum split required
# print(x)

#################################################################################
##sub
# import re
# line="python is an object-oriented programming language"
# x=re.sub('p','x',line)
# print(x)
#
# import re
# line="python is an object-oriented programming language"
# x=re.sub('p','x',line,1)    ##(word which need to be changed,word which is changeing,line,number of changes)
# print(x)

##########################################################################
# metacharacters
# ^   -cap symbol used for startswith
# $   - symbol used for endswith
# *   - 0 or more occurrences of a pattern
# +   - 1 or more occurrences of a pattern
# ?   - 0 or ONE occurrences of a pattern
# {n}  - strictly n times of occrnce
# {n,m}  - limit: min-n times & max. m times can  occr
# {,m}  - 0 to max. up to m times
# {n,}  - at least n times or more

# import re
# regex='^a...n$'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a...'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^(al)...'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a...'
# result=re.search(regex,"fgalaan")
# print(result)
#
# import re
# regex='al..'
# result=re.search(regex,"fgalaan")
# print(result)

##################################################
################################################
###############################################
# special sequences
# \w  - a-z,A-Z,0-9,_   it represents
# \W  - non chara. and digits (ie for special sybls)it represents
# \d  - 0-9   it represents
# \D  - non digit   it represents
# \s  - white space   it represents
# \S  - non white space chara.   it represents
# .   - any chara. except new line

# [] -it return a match if string contanin a character/pattern specified in the [].
#    -it used to represent a group of characters.
# [abc] - any one of these chara.
# [a-z] - any chara. in this range
# [0-9][0-9]- we can use combination also, here it means TWO digit no.
#
# import re
# regex='^a\w\w\wn$'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a\w+n$'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a[a-z]n$'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a[a-z]+n$'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='^a[a-z][a-z][a-z]n$'
# result=re.match(regex,"alaan")
# print(result)
##############################################################################
# import re
# regex='\w+'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='\w\w'
# result=re.match(regex,"alaan")
# print(result)
#
# import re
# regex='\w\w'
# result=re.search(regex,"alaan")
# print(result)
#
# import re
# regex='\w\w'
# result=re.findall(regex,"alaan")
# print(result)

###############################################################
# import re

# regex='\w+'
# result=re.search(regex,"alaan")
# print(result)
#
# regex='\w{3}'
# result=re.search(regex,'aaaaa')
# print(result)
#
# regex='\w{2}'
# result=re.findall(regex,'aaaaa')
# print(result)
#
# regex='\S'   ##caps s every charactersvother than white space
# result=re.findall(regex,'abcd ekjh')
# print(result)
#
# regex='\S+'   ##every words except white space
# result=re.findall(regex,'adsfjn asfnl')
# print(result)
#
# s="Hello, There, How"
# result=re.findall('[A-Z]',s)
# print(result)

# s="Hello, There, How"
# result=re.findall('[A-Z,]',s)
# print(result)
#
# s="HELLO, There, How"
# result=re.findall('[A-Z]+',s)
# print(result)
#
# s="Hello, There, How"
# result=re.findall('[A-Z]*',s)
# print(result)
#
# s="Hello,There,How"
# result=re.findall('[a-zA-Z,]+',s)
# print(result)
#
# s="Hello, There, How"
# result=re.findall('[A-Z]?[a-z]+',s)
# print(result)
#
# s="HELLO, There, How"
# result=re.findall('[A-Z]?[a-z]+',s)
# print(result)
#
#########################################################
##find phone number::
# s="""Its purpose is to allow the telephone number 9876543210458 and  9876543210 of
# a subscriber identified by name and address 46846 to be found. The rise of
# the Internet 565466 and 56545654651535 smart phones in the 21st
# Century greatly reduced the need for a paper phone book"""

# result=re.findall('[0-9]+',s)
# for i in result:
#     if len(i)==10:
#         print(i)
# print(result)

# cal='\s\d{10}\s'
# test=re.findall(cal,s)
# test1=test.split(" ")
# print(test1)

# import re
# s="9876543210 46846 5654665 98745654651"
# # number starts with 98
#
# nw='98\d+'
# nw1='\s?[9][8][7]\d{7}\s'
# test=re.findall(nw1,s)
# print(test)

import re
# s="9874565455 987654321056 46846 5654665 9874565465 7745654655"
# phone='.[0-9]{10}.'
# test=re.findall(phone,s)
# print(test)
# k=[]
# m=s.split(" ")
# 1.
# for i in m:
#     rs='^\d\d{8}\d$'
#     cal=re.findall(rs,i)
#     if len(cal)!=0:
#         k.append(i)
#
# print(k)
#
# or
# 2.
# l=[]
# for i in m:
#     regex = '^\d\d{8}\d$'
#     res=re.findall(regex,i)
#     print(res)
#     if len(res)!=0:
#         l.append(res[0])
# print(l)

##################################################
###############################
# s="""readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the things that was especially interesting was that there were no safety laws at work.
# Also, there was a big contrast between the rich and the poor. Some
# Readers may not like this book because it is very depressing, but it is an
# important event in history to remember."""
#
# regex='^R'
# result=re.search(regex,s,flags=re.MULTILINE)         #search function search the entire para
#
# s="""readers can gain knowledge of what it was like to work in New York City in the early 1900s.
# One of the things that was especially interesting was that there were no safety laws at work.
# Also, there was a big contrast between the rich and the poor. Some
# Readers may not like this book because it is very depressing, but it is an
# important event in history to remember."""
#
# regex='Read'
# result=re.findall(regex,s,flags=re.IGNORECASE)
# print(result)

# phone number validation
# s="9961637450"
# regex="^(996)\d{7}$"
# test=re.match(regex,s)
# print(test)

# email validation
# s="abcdef@gmail.com"
# regex='^\w+[@]\w+[.][a-z]{,3}'
# result=re.match(regex,s)
# print(result)

##################################################3
# ques
# # create classes PERSON as parent class, and USER as child class.
# # parent class instance variables are name,age,mob num.
# # child class instance variables are user name and passwd.
# # input all data from user and create a list.
# # using this list create an object user1 in which
# # user name must be  characters and passwd must digits or character.
# # create a main fn to check this conditions then if satisfy, create an object user1.
#####1.
# class PERSON:
#     def __init__(self, name,age, mob):
#         self.name=name
#         self.Age=age
#         self.mob=mob
#
# class USER(PERSON):
#     def list(self):
#         list=[self.name,self.Age,self.mob]
#         print(list)
#
# def input_value():
#     name=input("enter the name")
#     age=int(input("enter the age"))
#     mob=int(input("enter the number"))
#     user1=USER(name,age,mob)
#     user1.list()
#
# # input_value()
# class USERNAMEERROR(Exception):
#     pass
# class PASSWORDERROR(Exception):
#     pass
#
# import re
# try:
#     username=input("enter a user name: ")
#     usr='^[a-z]{5,10}$'
#     usrname=re.match(usr,username,flags=re.IGNORECASE)
#     if usrname:
#         try:
#             password = input("enter a password(password must contain characters and digits): ")
#             passw = '\w+\d+'
#             passwrd = re.match(passw, password, flags=re.IGNORECASE)
#             if passwrd:
#                 input_value()
#             else:
#                 raise PASSWORDERROR
#         except PASSWORDERROR:
#             print("Password is incorrect")
#     else:
#         raise USERNAMEERROR
# except USERNAMEERROR:
#     print("user name is incorrect")
#
#####################################################################################
##########or
###########################
# import re
# class person:
#     def __init__(self,name,age,mobileno):
#         self.name=name
#         self.age=age
#         self.mobileno=mobileno
# class user(person):
#     def __init__(self,name,age,mobileno,username,password):
#         super().__init__(name,age,mobileno)
#         self.username=username
#         self.password=password
#         print("details:",self.name,self.age,self.password,self.username,self.mobileno)
# def main():
#     a=[]
#     print("Enter name,age,mobile number,user name and password")
#     for i in range(0,5):
#         a.append(input())
#     print(a)
#     # regex = '[a-zA-Z]{5}'
#     # regex = '[a-zA-Z]+'
#     regex = '^[a-zA-Z][a-zA-Z]*[a-zA-Z]$'
#     # regex = '[a-zA-Z0-9]{5,15}'
#     test1 = re.match(regex,a[3])
#     print(a[3])
#     if test1:     # if user name is correct, check for pswd
#         reg='[\da-zA-Z]+[\da-zA-Z]$'
#         test2 = re.match(reg, a[4])
#         if test2:   # if passwd is correct create object
#             user1=user(a[0],a[1],a[2],a[3],a[4])
#         else:
#             print("password must be digits or alphabets")
#     else:
#         print("user name must be  alphabets")
# main()
############################################################################
#######################################################################
#############################################################################













