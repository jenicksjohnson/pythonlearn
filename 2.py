#############################################################################################
# list

# a=[1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(type(a))

# a="this is a python program"
# print(list(a))
# print(type(a))

# a=(1,2,3,4,5,6,7)
# b=list(a)
# print(b)
# print(type(b))

# l=[1,2,3,4,5,6,7,8,9,0]
# print(l[::2])
# print(l[0:4])
# print(l[2:9:2])
# print(l[::])
# print(l[::-1])

# a="medam"
# b=list(a)
# b.reverse()
# print("".join(b))

# l=[1,2,3,4,5,[1,4,7]]
# print(l[5])
# print(l[5][0])
# print(l[-1][0])
# print(l[-1][-1])

# l=[1,2,3,4,5,6,7,8]
# k=["one","two"]
# l=k+l
# print(l)
# new=l+k
# print(new)

# l=[1,2,3,4,5,6,7,8,9,0]
# print(l)
# print(id(l))
# l[6]="five"
# print(l)
# print(id(l))
# l[3]="ern"
# print(l)

# l=[1,2,3,4,5,6,78,4]
# print(l)
# print(len(l))
# l.append("three")
# print(l)

# l=[2,3,4,5,6,7,8,9,0]
# l.insert(3,'three')
# print(l)
# print(l.index("three"))
# print(l.index(0))

# l=[1,2,3,4,5,6,7,8,9,0]
# del l
# print(l)

# l=[1,2,3,"three",4,5,6,7,8,90]
# l.remove('three')
# print(l)

# l=[1,2,3,"three",4,5,6,7,8,90]
# del l[5]
# print(l)

# l=[1,2,3,"three",4,5,6,7,8,90]
# print(l)
# a=l.pop()
# print(l)
# print(a)
# l.pop(5)
# print(l)

# a=[1,2,3,4,2,5,7,3,4]
# b=["two","three",'four']
# c=("q","w")
# a.extend(b)
# a.extend(c)
# print(a)
# a.append(b)
# print(a)

# L=[1,2,3,4,2,6,6,2,45,78,7,6,6]
# print(L.count(6))
# print(L.count(2))

# a=[1,2,3,4,2,5,7,3,4]
# h=a
# a.append(67)
# print(h)
# print(a)

# a=[1,2,3,4,2,5,7,3,4]
# s=a.copy()
# a.append(67)
# print(a)
# print(s)

###################################################################################################################
# membership operators

# l=[1,2,3,"three",4,5,6,7,6]
# if "three" in l:
#     print("it is")
# if 9 not in l:
#     print("its not")

# s=[1,2,3,4,5,6,7,8]
# s.sort()
# print(s)
# v=sorted(s,reverse=True)
# print(v)
# print(s)

# a="hello everyone this is python"
# t=a.split()
# print(t)

# create a new elements with list of the square of the first list
# k=[]
# s=[0,1,2,3,4,5,6,7,8,9,10]
# for i in s:
#     m=i*i
#     k.append(m)
# print(k)
# or
# for i in range(11):
#     k.append(i**2)
#     print(k)
# print(k)

# create a list with all positive numbers
# lst=[-10,20,10,-20,-15,30]
# k=[]
# for i in lst:
#     if i>0:
#         k.append(i)
# print(k)
# or
# for i in lst:
#     if i==0:
#         continue
#     elif i<0:
#         continue
#     else:
#         k.append(i)
# print(k)

# write the program to find to largest number from a list
# l=[12,5634,13,63,75,234,996,23]
# rev=sorted(l,reverse=True)
# print(rev)
# print("the largest is::",rev[0])
# or
# larg=l[0]
# print(larg)
# for i in l:
#     if i>larg:
#         larg=i
# print(larg)

# write a program to find first and last letter same
# L=["xyz","aba","abcd","1231","sdhbks"]
# k=[]
# count=0
# for i in L:
#     if i[0]==i[-1]:
#         k.append(i)
#         count=count+1
# print(count)
# print(k)

#program to remove duplicate items from a list
# L=[10,20,30,20,10,50,10,10]
# k=[]
# for i in L:
#     if i not in k:
#         k.append(i)
# print(k)

# or

# k=set(L)
# m=list(k)
# print(m)

# or

# for i in L:
#     if L.count(i)>1:
#         L.remove(i)
# print(L)

# duplicate elements


# aggrigate functions
# l=[1,2,3,4,5,2,4,6,7,34,57,59,2,4,5]
# print(max(l))
# print(sum(l))
# print(min(l))

# l=[[1,2,3],[4,8,9,8],[5,8]]
# print(l[1])
# print(l[1][1])
# print(l[2][1])

# list comprehension
# sqrs=[]
# for i in range(5):
#     sqrs.append(i**2)
# print(sqrs)
# or
# sqrs=[i**2 for i in range(5)]
# print(sqrs)

# positive numbers
# l=[-20,-10,10,50,-10]
# pstve=[i for i in l if i>0]
# print(pstve)

# finding trnsverse of a metrix

# m=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# x=[]
# for j in range (len(m[0])):
#     l=[]
#     for i in m:
#         l.append(i[j])
#     x.append(l)
# print(x)

# or
# x=[[(i[j]) for i in m] for  j in range (len(m[0]))]
# print(x)

# or
# result=[[m[j][i] for j in range (len(m))] for i in range (len(m[0]))]
# print(result)






