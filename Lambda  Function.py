# for single time use
# double= lambda x:x*2
# print(double(5))
#
# sum = lambda x,y:x+y
# print(sum(5,10))
#
# printMsg =lambda msge1,msge2: print("output is : {},{}".format(msge1,msge2))
# printMsg("hello","how are you")

###################################################################
# map function
# def add(n):
    # return n+10
# l=[1,2,3,4,5,6,7,8,9]
# new=list(map(add,l))
# print(new)

### by using lambda function
# l=[1,2,3,4,5,6,7,8,9]
# new =list(map(lambda x:x+10,l))
# print(new)

######################################################################
# l=[10,20,30,40]
# new=list(map(lambda x:x*10,l))
# print(new)

##################################################################
## filter function
### filter is used to filter a data from a sequence order
# l=[1,2,3,4,5,6,7,8,9]
# def iseven(m):
#     if m%2==0:
#         return m
# even=list(filter(iseven,l))
# print(even)
### or
# for i in even:
#     print(i)

# by using lambda function
# l=[1,2,3,4,5,6,7,8,9]
# even=list(filter(lambda x:x%2==0,l))
# print(even)

#############################################################
# words=("hi","hello","how","are","you")
# h=list(filter(lambda x:x[0]=="h",words))
# print(h)
## or use startswith

###########################################################
# filter vowels
# letters=["a","b","d","e","i","j","o"]
# v=list(filter(lambda x:x=="a"or x=="e" or x=="i"or x=="o"or x=="u",letters))
# print(v)

############################################################



































































