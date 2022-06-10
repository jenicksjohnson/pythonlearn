# # # # # #other functions
import numpy as np
#
# # # # # #transpose of a matrix
# x=np.array([[1,1,3],[2,2,5]])
# print(x)
# print(x.T)   ###transpose
# # #
##flattening
# x=np.array([[1,1,3],[2,2,5]])
# print(x)
# print(x.ravel())
# print(np.ravel([[1,2],[3,4]]))
# # # # # #
##reshape
# a=np.arange(24)
# print(a)
# print(a.reshape(6,4))  ##convert the above into 6 rows and 4 columns
# b=a.reshape(6,2,2)    ##convert into 3d matrix
# print(b)
# c=b.reshape(6,4)
# print(c)
##resize
# a=np.arange(4)
# print(a)
# a.resize(8)
# print(a)     ##remaining values will be 0
###
# # b=a
# # a.resize(8)   ##if we use a object to another object we cannot resize that obj
##sorting
# a=np.array([[5,4,6],[2,3,2]])
# print(a)
# b=np.sort(a)   ##this will be row wise sorting
# print(b)
# ####
# b=np.sort(a,axis=0)  ##this will sort column wise
# print(b)
##argsort
# a=np.array([40,30,10,20])
# print(a)
# d=np.argsort(a)
# print(d)     ##shows positions to be sorted
#################################################