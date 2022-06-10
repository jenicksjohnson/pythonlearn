import pandas as pd
import numpy as np
# s=pd.Series(['Tom','William Rick','John','Alber@t',np.nan,'1234',' SteveSmith'])
# print(s)
# print(s.str.lower())
# print(s.str.upper())
# print(s.str.len())
# s1=s.str.strip()
# print(s1.str.len())
# # print(s.str.len())
# print(s.str.cat(sep="/")) #to join using a seperate optr
# print(len(s[6]))
#
"""
we have Label Encoding and One Hot Encoding for string.
In label encoding we gives 1,2,3..for unique string.
(in LE, machine may find out any relation between digits, like 1+2=3, 1<3 etc. So we follows OHE)
In One hot encoding we follow binary numbers.
(it forms a vector, its length = no of unique strings)
###if the no of categories increases, vector became sparse. 

designation            teacher  student  office staff
  teacher                   1       0           0    
  teacher                   1       0           0
  student                   0       1           0
  student                   0       1           0
  student                   0       1           0
  office staff              0       0           1
  office staff              0       0           1 #this extra variable are
                                                    called dummy variables.
"""
# #
# #
# print(s.str.get_dummies())
# print(s.str.contains(' '))
# print(s.str.replace('@','$'))
# print(s.str.count('m'))
# print(s.str. startswith ('T'))
# print(s.str.endswith('t'))
# print(s.str.find('e'))   #-1 if not matching
# print(s.str.findall('e'))
# print(s.str.swapcase())
# print(s.str.islower())
# print(s.str.isupper())
# print(s.str.isnumeric())
#
#
#
#
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#  'Sex':pd.Series(['male','female','male','male','male','male','female']),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# df = pd.DataFrame(d)
# print(df)
# print(df['Name'].str.lower())
# df['Name']=df['Name'].str.upper()  ##this will print back entire tables with caps as replaced
# print(df)
# print(df['Name'].str.len())
# new=df['Sex'].str.get_dummies()
# print(pd.concat([df,new],axis=1))
# #
# newdf=pd.get_dummies(df)
# print(newdf)
# print(newdf.columns)
#
#
#
#Arithmetic operations
import pandas as pd
import numpy as  np
# # #
# df1 = pd.DataFrame(np.array([1,2,3,4]).reshape(2,2),
#                    index=[1,2], columns=[1,2])
# df2 = pd.DataFrame(np.array([7,8,5,6]).reshape(2,2),
#                    index=[1,2], columns=[1,2])
# print(df1)
# print(df2)
# print(df1+df2)
# print("sum is : ",df1.add(df2))
# # # # # ##if the index changes matching indexes get added and remainging NaN
# df3 = pd.DataFrame(np.array([7,8,5,6]).reshape(2,2),
#                    index=[1,3], columns=[1,2])
# print(df3)
# print(df1+df3)
# ## #  # # # # # # # # #  # # # # # # # # # # #
# # # # # #merging
# df1=pd.DataFrame({'Id':[1,2,3,4,5],
#                   'Name':['Alex','Amy','Allen','Alice','Ayoung'],
#                   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
# print(df1)
# df2=pd.DataFrame({'Id':[1,2,3,4,5],
#                   'Name':['Billy','Brian','Bran','Bryce','Betty'],
#                   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(df2)
# print(pd.merge(df1,df2))   ##will give empty
#
# print(pd.merge(df1,df2,on='Id'))
# print(pd.merge(df1,df2,on='subject_id'))
#
# # #merging data frames using multiple varibles
# print(pd.merge(df1,df2,on=['Id','subject_id']))
#
#
# # basis onleft
# print(pd.merge(df1,df2,on='subject_id',how='left'))
# # basis on right
# print(pd.merge(df1,df2,on='subject_id',how='right'))
#
# full outer
# print(pd.merge(df1,df2,on='subject_id',how='outer'))
#
#
#
#
# # # # # # # # # # # # # # # # # # #  # # # # # ##
# # melt and pivot
#
'''Melting in pandas reshape data frame from wide format
to long format
'''
# # #it reduces the columns and increases rows
# df=pd.DataFrame(data={
#     "Day":['MON','TUE','WED','THU','FRI'],
#     'Google':[1129,1132,1134,1152,1152],
#     'Apple':[191,192,190,190,188],
#     'Amazon':[210,524,430,325,551]
# })
# print(df)
# ## here we can use "Day"  as a variable/identifier because it is common to other fields
# ##sd on 'day' basis we cando reshape
# ## that we want to mention as "id_vars['col_names']"
#
# df1=df.melt(id_vars=["Day"])
# print(df1)
# #
# df1=pd.melt(df,id_vars=["Day"])
# print(df1)
'''this generate 2 columns,
variable-it contain actual column names.
value-it contains actual values'''
# # to rename the columns
# df1=df.melt(id_vars=["Day"],var_name="company",value_name="sales")
# print(df1)
# #
# # #value_vars: from the result if we need only specific variable values
# df1=df.melt(id_vars=["Day"],value_vars=['Google','Amazon'],var_name="company",value_name="sales")
# print(df1)
###########################
########## # # #pivot
'''
pivot: reverse melt(opp. concept of melting)
'''
#
#
# index-what we need as rows
# columns-what we need as columns
#
#
# originaldata=df1.pivot(index='Day',columns="company")["sales"].reset_index()
# originaldata.columns.name=None
# print(originaldata)
#
#
#
#
#
#
#
# # # # # # #concatination
'''Concatination:
Pandas provides various facilities for easy coombining together series,
DataFram, and Panel objects
'''
one=df1=pd.DataFrame({'Id':[1,2,3,4,5],
                  'Name':['Alex','Amy','Allen','Alice','Ayoung'],
                  'subject_id':['sub1','sub2','sub4','sub6','sub5'],
                  'Marks_scored':[98,90,87,69,78]},index=[1,2,3,4,5])
two=pd.DataFrame({'Id':[1,2,3,4,5],
                  'Name':['Billy','Brian','Bran','Bryce','Betty'],
                  'subject_id':['sub2','sub4','sub3','sub6','sub5'],
                  'Marks_scored':[89,80,79,97,88]},index=[1,2,3,4,5])
print(one)
print(two)
# # # # #
df1=pd.concat([one,two])  ##combine with both index
print(df1)
# # # #
df1=pd.concat([one,two],ignore_index=True)  ###default index
print(df1)
# # # #columnwise add
print(pd.concat(objs=[one,two],axis=0))    ##under the same columns
print(pd.concat(objs=[one,two],axis=1))     ##under the same rows(rowwise)






