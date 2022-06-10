########################################################################
# set- mutable but immutable

# u=set()
# print(type (u))

# a={1,2,3,4}
# print(type(a))

# a=set([1,2,3,4])
# print(a)
# print(type(a))

# adding an element in a set

# a={1,2,3,6,4,2,3,8,4}
# a.add("str")
# print(a)
# a.add(0)
# print(a)

# adding multiple elements in a set
# a={1,3,2,5,3,4,6,8,7,5}
# print(id(a))
# a.update({"ert","wds"})
# print(a)
# a.update({1,"sdr","sweh"})
# print(id(a))
# print(a)
# a.update(["d","g"])
# print(a)
# print(id(a))
# a.update(["bbg","nms"],{123,234,5667})
# print(a)

# removing an element
# a.discard(3)
# print(a)
# a.remove(2)
# print(a)

# a={1,2,3,4,5,6,7,8,9,10}
# print(a)
# a.pop()
# x=a.pop()
# print(x)
# print(a)
# a=a.pop()
# print(a)

# clear all elements
# a={1,2,3,4,45}
# a.clear()
# print(a)

# a={1,6,32,7,5,3,244}
# print(min(a))
# print(max(a))
# print(sum(a))
# print(sorted(a))

# a={1,2,3,4,5}
# b={4,5,6,7,8}

# print(a|b)
# print(a.union(b))

# print(a&b)
# print(a.intersection(b))
# print(b.intersection(a))

# print(b-a)
# print(a.difference(b))
# print(b.difference(a))

# print(a^b)

# a={1,2,3,45,6,7}
# x=frozenset(a)               #to make set to immutable
# print(type (x))

# d={"a","s","g"}
# for k in d:
#     print(k)




