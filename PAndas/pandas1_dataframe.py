# ## # # #data frame
#used for hetrogeneous data
# size is mutable
# #data also mutable
# #it have labeled axis
# #can load data from diff formats.

import pandas as pd
# # #1.list
# df1=pd.DataFrame([10,20,30])
# print(df1)
# # # # # # # # # #
# df2=pd.DataFrame([10,20,30],['a','b','c']) # #custom idexing
# print(df2)
# # # # # # #
# df3=pd.DataFrame([[10,20,30],[40,50,60]]) ##2rows
# print(df3)
# # # # # # # # # #
# ##custom indexing
# df4=pd.DataFrame([[10,20,30],[40,50,60]],['a','b'])  #giving indexes to rows
# print(df4)
# ##custom indexing to coloumns
# df5=pd.DataFrame([[10,20,30],[40,50,60]],['a','b']     ##indexes to rows
#                  ,columns=['id','age','mark'])  #giving indexes to cols
# print(df5)
# print(df5.shape)
# # # # # # # # # # # # #
# # # # # setting index number
# df5.set_index('id',inplace=True)  ##giving id number as index number
# print(df5)
# print(df5.shape)
# # # # # # # # #######  # # # #
# df6=pd.DataFrame([[1,'Ajith',30],[2,'Alex',60]]
#                  ,columns=['ID','NAME','MARK'])  #giving indexes to cols
# print(df6)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# #value from dictionary
#
# d={'pid':[1,2,3],'name':['book','pen','pencil'],'price':[10,5,4]}
# df7=pd.DataFrame(d)
# print(df7)
# ###
# df7.set_index('pid',inplace=True)
# print(df7)
# # # # # # # # # # # # # # # # # # # # # # #
# ##list of dictionry is passing
# #if there is no value then it will be nan(not a number)
# l=[{'A':'ann','B':'tom'},
#    {"C":"jerry","A":"kevin"}]
# df=pd.DataFrame(l)
# print(df)
# # #if its a dictionary of series
# data={'one':pd.Series([1,2,3]),'two':pd.Series([7,8,2,8])}
# df1=pd.DataFrame(data)
# print(df1)