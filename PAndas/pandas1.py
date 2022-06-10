# import pandas as pd
#
# s1=pd.Series(10)
# print(s1)
# print(type(s1))
# #########################
# s1=pd.Series(10,dtype='int32')  ##change datatype
# print(s1)
# ##########################
# s2=pd.Series(10,index=[1,2,3,4])  ##custom indexing
# print(s2)
# ##########################
# s2=pd.Series(10,index=['a','b','c'])   ##custom indexing
# print(s2)
# ###########################
# s1=pd.Series([10,20,30,40])
# print(s1)
# #############################
# ##############################
# s2=pd.Series([10,20,30],index=['a','b','c'])
# print(s2)
#
# ##################################
# # ##from dictionary
# d={'x':21,'y':45,'z':55}
# s1=pd.Series(d)
# print(s1)
##################################
# import pandas as pd
# import numpy as np
#
# a=np.array([4,5,6])
# # s1=pd.Series(a)
# # print(s1)
# # # #
# s1=pd.Series(a,index=['a','b','c'])
# print(s1)
# # # # #
# print(s1[0])
# print(s1[1])
# print(s1[:])
# print(s1[-1])
# print(s1[-2])
# print(s1[:-1])
# print(s1[::2])
# print(s1['a'])
# s1['a']=100
# print(s1[0])
# s1[1]=10
# print(s1)
# # # #
### ##attributes
# import pandas as pd
# s1=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print(s1)
# print(s1.dtype)
# print(s1.size)
# print(s1.shape)
# print(s1.ndim)
# ######## #######
# sorting
#######
# import pandas as pd
# s1=pd.Series([10,30,15,20],index=['a','c','b','d'])
# print(s1)
# #### we can sort it by index
# s=s1.sort_index()
# print(s)
# s=s1.sort_index(ascending=False)
# print(s)
# ####we can sort by values
# s=s1.sort_values()
# print(s)
###########################################
################################
import pandas as pd
# ser = pd.Series(range(6), index=['white','white','blue','green','green','yellow'])
# print(ser)
# print(ser['white']) #will get a Series in place of a single element
# # # #  to check any duplicate in index
# print(ser.index.is_unique)
# #####filtering
# # #many operations applicable to NumPy arrays are extended to the Series
# s = pd.Series([12,-4,7,9,7], index=['a','b','c','d','e'])
# print(s)
# print(s > 8)
# print(s[s > 8])
# k=s[s > 8]
# print(k)
# # # # #Unique values
# print(s.unique())
# # # print(type(s.unique()))
# # # # # # To count values
# print(s.value_counts())
# # # # #evaluates the membership
# print(s.isin([12,7,30]))
# print(s[s.isin([12,7,30])])
# # # ## # # # # # # # # #
##NaN(Not a Number) is used within pandas data structures to indicate the
# # #presence of an empty fieldor not definable numberically
import numpy as np
import pandas as pd

# s2=pd.Series([5,-3,np.NaN,14])
# print(s2)
# # # isnull() and notnull() functions are very useful to identify the
# # # indexes without a value
# print(s2.isnull())
# print(s2.notnull())
# # #
# print(s2[s2.notnull()])    # # # gives the resut which is having values
# print(s2[s2.isnull()])     # # # gives the resut which is not having values
# # # # # # # #  # # # #  #   # ## # # # ##
# # # # #filtering from series using keys
# mydict={'red':2000,'blue':1000,'yellow':500,'orange':1000}
# myseries=pd.Series(mydict)
# print(myseries)
# # # # #
# colors=['red','orange','blue','green']
# myseries1=pd.Series(myseries, index=colors)
# print(myseries1)
# # # # #
# colors=['red','orange']
# myseries1=pd.Series(myseries, index=colors)
# print(myseries1)
# # # #
###### adding 2 series
# mydict1={'red':2000,'blue':1000,'yellow':500,'orange':1000}
# myseries1=pd.Series(mydict1)
# print(myseries1)
# mydict2={'red':2000,'yellow':500,'black':700}
# myseries2=pd.Series(mydict2)
# print(myseries2)
# print(myseries1 + myseries2)
# # # # # # # #  # # #   # # # # # # # # ##
# # # ##### # #
# ##### #attributes
# mydict1={'red':2000,'blue':1000,'yellow':500,'orange':1000,
#          'red1':2000,'blue1':1000}
# s=pd.Series(mydict1)
# print(s)
# print(s.axes)
# print(s.dtype)
# print(s.ndim)
# print(s.size)
# print(s.values)
# print(s.head()) ##print first 5 rows if no index is set
# print(s.head(2))
# print(s.tail())  ##print last five rows
# print(s.tail(2))
# print(s.empty)  ###to check empty fields
# ## # # # # #   # #
# # ### # # #for deleting a value
# del s['red']
# print(s)