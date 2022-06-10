import pandas as pd
import numpy as np
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],columns=['id','age','mark'])
# print(df)
# # # # # # #
# print(df.columns)   ##to know column names
# print(df.keys())    ##columns
# print(df.values)    ##to get the values
# print(df.index)     ##to get the index range
# print(df.dtypes)    ##to get column wise data types
# ## # #
# print(df.shape)
# print(df.shape[0])  ##rows number
# print(df.shape[1])  ##column numbers
# # # # #
# a=df.shape[0]
# b=df.shape[1]
# # # # # # # # # # # # # # # # # # # # # #
# l=[[1,2,3,"ram"],[2,5,6,"manu"],[3,8,9,"sonu"],
#    [4,8,9,"aldrin"],[5,9,8,"amal"],[6,5,9,"jose"]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=['id','age','mark','name'])
# print(df)
# print(df.describe())  ##to see the summary
# """ 25^th percentile is 2.25means,25% of values in that column or list
#  are less than 2.25 and remaining 75% of values are greater than 2.25"""
# import numpy as np
# print(df['mark'])
# print(np.percentile(df['id'],25))
# print(np.percentile(df['id'],50))
# print(np.percentile(df['id'],75))
# print(np.percentile(df['id'],90))
# '''quartiles are 1^st quartile =25%
#                  2^nd quartile =50%
#                  3^rd quartile =75%'''
# # # # # # # # # # # # # # # # # # # #  #
### ##
# ## does not count nan values
# l=[[1,2,3],[2,5,6],[3,np.nan,9],[4,8,9],[5,9,8],[np.nan,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=["id","age","mark"])
# print(df)
# print(df.nunique())
# print(df.nunique(axis=0)) ###column wise
# print(df.nunique(axis=1)) ### row wise
##  # # # # # # # # # # # #
# l=[[1,2,3],[2,5,6],[3,np.nan,9],[4,8,9],[5,9,8],[np.nan,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=["id","age","mark"])
# print(df)
# # to consider nan
# print(df.nunique(dropna=False))
# # # # # # # # # # # # # # #
# # # # #to count values in a specific columns
# l=[[1,2,3],[2,5,6],[3,np.nan,9],[4,8,9],[5,9,8],[np.nan,5,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=["id","age","mark"])
# print(df['id'].value_counts())
# print(df['mark'].value_counts())
# print(df['age'].value_counts())
# ################ ############# ################# ################## ##########
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # important # # # # # # # # # # # # # # # # # # #
#  # ####dataframe slicing
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,8,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=["id","age","mark"])
# print(df)
# # print(df['id'])
# # print(df.id)         ##"""both are same"""
# # print(df.columns)  ###to knows the cols  name
# print(df[['id','age']])  ##inside to brackets we can specify 2 cols

# # # # # # # #slicing rows
# # ##.loc  ==use for custom index
# # ##.iloc ==used for default index
#
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,8,9]]
# df=pd.DataFrame(l,index=['a','b','c','d','e','f'],
#                 columns=["id","age","mark"])
# # to get a specific single row
# print(df.loc['b'])
# print(df.iloc[1])    ##for default row
#
# #for multiple rows
# print(df.loc[['d','f']])
# print(df.iloc[[3,5]])
# # # # #
# print(df.loc['b':'f'])
# print(df.iloc[1:6])
# # # #
# print(df.loc[:,['id','mark']])   # # #entire rows and specified cols
# print(df.iloc[:,[0,2]])
# print(df.loc['b',['id','age']])
# print(df.loc['b':,['id','age']])
# # # # #
# print(df.loc['b':'d',['id','age']])
# print(df.iloc[1:4,[0,1]])
# # # # #
# print(df.loc[['b','e'],['id','age']])
# print(df.iloc[[1,4],[0,1]])
# # # # #  # # # ## # # # # # # # # # # # #
# print(df)
# print(df.iloc[-1,-1])
# print(df.iloc[-5,-3])
# print(df.iloc[-1:, -1:])
# print(df.iloc[-3:, -2:])
# # # # # # # # # # # # # #
# To get a single value within a DataFrame, use df['col_name']['row_name']
# # # # # #
# print(df['id']['b'])
# print(df.loc['b', 'id'])
# print(df.iloc[1, 1])
#################################
# print(df.iloc[:, 1].idxmax())  # get the index of the max value from the slice of DataFrame
# print(df.iloc[:, 1].idxmin())  # get the index of the min value from the slice of DataFrame
# # # # ##  # # # # # # ## # # # # #
# #conditional slicing/filteration
# import pandas as pd
# l=[[1,2,3,'ajith','mech'],[2,5,6,'alex','mech'],[3,8,9,'john','cs'],
#    [4,8,9,'ann','ec'],[5,9,8,'smith','cs'],]
# df=pd.DataFrame(l,index=['a','b','c','d','e'],
#                 columns=['id','age','mark','name','dept'])
# # ## # # # # ##
# print(df)
# # # # # this will only returns boolean values
# print(df['age']>5)
# print(df.age>5)
# # # # # this will returns the values
# print(df[df['age']>5])
# print(df[df.age>5])
# # #
# print(df[df.mark==9])
# print(df[df['mark']==9])
# # # #using iloc
# print(df.loc[df['mark']==9])
# print(df.loc[df.mark==9])
# print(df[df.iloc[:,2]==9])
#
#
#with .loc we sliceing df,so here we can mention column as well
# print(df.loc[df.mark>6,'name'])
# print(df.loc[df.mark>6,['mark','name']])
# print(df.loc[df['mark']>6,['mark','name']])
# df1=df.loc[df.mark>6,'name']
# print(df1)
# # # # # # # # # # #
##adding two conditions
# print((df.mark<=6) & (df.dept=='mech'))  ##it only returns boolean value
# print(df[(df['mark']<=6) & (df.dept=='mech')])
# print(df[(df.mark<=6) & (df.dept=='mech')])
# print(df.loc[(df.mark<=6) & (df.dept=='mech')])
# print(df.loc[(df['mark']<=6) & (df['dept']=='mech'),'id'])

# # q:mark b/w 7 and 9
# print(df.loc[(df['mark']>7) & (df['mark']<9),['mark','name']])
# # # # # # # # #
# print(df.loc[(df.mark<=3) | (df.dept=='mech')])
# print(df.loc[(df.dept=='cs') | (df.dept=='mech') | (df.dept=='ec')])
# print(df[df.dept.isin(['cs','mech','ec','ic'])])
# print(df[df.dept.isin(['cs','mech','ec']) & (df.mark<9)])

# ##assign value
# df['age']+=2
# print(df)
# df['name']+=" xyz"
# print(df)
# df['mark']=100
# print(df)
# # #
# # # # #
# df.loc[:,'age']+=2
# print(df)
# df.iloc[:,1]+=10
# print(df)
# # #
# # # # row value changeing
# df.loc['b']=10
# print(df)
# # #
# df.iloc[1]=20
# print(df)
##############at specific condition changing the value of that
# df.loc[df.mark>6,'mark']=50
# print(df)

#
#
#
# import pandas as pd
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,8,9]]
# df=pd.DataFrame(l,index=['a','c','d','e','b','f'],
#                 columns=['id','age','mark'])
# print(df)

# adding new rows
# df2 = pd.DataFrame([[7,10,6],[8,12,8]],columns=['id','age','mark'])
# print(df2)
# df1=df.append(df2)
# print(df1)
# df.concat(df2)
# print(df)
#
# # # # delete a row
# df=df.drop(['f'])
# print(df)
# # # #multiple rows
# df=df.drop(['a','c'])
# print(df)
# # # # #
# # # #
# # #to add new columns with values same
# df['new']=12
# print(df)
# # #
# #
# df['new']=df['age']+df['mark']
# print(df)
# # # ##
#### to add new columns with different values
# df['new']=[1,3,5,6,3,4]
# print(df)

#### for del a col
#1. pop
# df1=df.pop('mark')
# print(df)
# 2. delete
# del df['age']
# print(df)
# 3.drop
# df1=df.drop(columns='age')
# print(df1)
# print(df)
# # df.drop(['id'],axis=1)
# # print(df)
# df1=df.drop(['id'],axis=1)
# print(df1)
#
#
# # dataframe membership, same as in series
# print(df.isin([2,4]))
# print(df[df.isin([2,4])])

# # ##   # # Transpose rows and columns
#  #create a dictionary of series
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# df=pd.DataFrame(d)
# # ####
# print(df)
# print(df.shape)
# dfnew=df.T ##caps t creates a new df as transpose
# print(dfnew)

# #statistics are two: descriptive and inferential statistics

# import pandas as pd
# d = {
#    'Age':pd.Series([25,26,25,23,30,29,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# # # # #creating dataframe
# df=pd.DataFrame(d)
# print(df)
# print(df.sum())
# print(df['Age'].sum())  ### for a specific row
# print(df.sum(1)) ##row wise
# ## ##to get the average value
# print(df.mean())
# #
## variance: avg.squre distance from mean
## standerd deviation: sqr root of variance
"""  -ie,avg.distance of points from mean value.
(if we know spread, we get an idea that how wide our points spread from 
 mean ,is it is around mean or not. 
 Numerical representation of spread is called sdt.dev"""
# To get the standard deviation
# print(df.std())
# print(df.median())
# print(df.mode())  #The most repeating number
# print(df.abs())  #+ve nums
# print(df.max())
# print(df.min())
# print(df.cumsum())  #adding each elemt to previous sum
# print(df.cumprod())
# print(df.count())
# print(df.sum()/df.count())  ####to find the mean

''' There are three types of function applications
1)Table wise Function Application: pipe()
2)Row or Column Wise Function Application: apply()
3)Element wise Function Application: applymap() '''

#1) Table wise Function Application: pipe()
''' to every element in the table / to the whole data frame 
we can perform a custom operation using pipe() operator.'''
#
# import pandas as pd
# import numpy as np
# def add(ele1,ele2):
#    print(ele1)
#    print(ele2)
#    return ele1+ele2
# # # # #
# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# print(df.pipe(add,2))    # # pipe is passing df and 2 as an arguments and calls the function

## #rows or column wise function application
"""
 Arbitrary functions can be applied along the axes of a Dataframe  
 using the aplly() method
"""
# we will get single values per cols/rows
#
# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# print(df.apply(np.mean))
# print(df.apply(np.mean,axis=1))
# print(df.apply(lambda x:x.max()-x.min()))
# print(df.apply(lambda x:x.max()-x.min(),axis=1))

##element wise function application(map,applymap)
# df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# print(df)
# #####functions
# print(df['col1'].map(lambda x:x*100))  ##for a single column
# print(df.col1.map(lambda x:x*100))  # # same as above
# print(df.loc[1].map(lambda x:x*100))  ##for a single row
# # # #  #
# print(df.applymap(lambda x:x*100))    ##for all data frames

##eg:-map
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#    'Age':pd.Series([25,26,25,23,30,29,23])}
# df=pd.DataFrame(d)
# print(df)
# print(df[df.Name.map(lambda x: x[0]=="S")])
# print(df[df.Name.map(lambda x: x.startswith("S"))])
#
#
#
#
#
# # # # # # indexing a dataframe
'''
it makes df indexes similar to the matching indexes
'''
# df=pd.DataFrame(np.random.randn(10,4),columns=['col1','col2','col3','col4'])
# print(df)
# df2=pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
# print(df2)
# df1=df.reindex_like(df2)
# print(df1)  ## df1 same as like df2
# # # #
# df1=df2.reindex_like(df)
# print(df1)
# # # # # #  #filling while ReIndexing
#
#
# df1=pd.DataFrame(np.random.randn(10,4),columns=['col1','col2','col3','col4'])
# print(df1)
# df2=pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
# print(df2)
# print(df2.reindex_like(df1,method='ffill'))  ## #fill the last rows and cols which is having NAN
# print(df2.reindex_like(df1,method='ffill',limit=1))  ##only fills 1 row and cols which is having nan
# #
# #
# #if the df is custom frames
# df=pd.DataFrame({"name":["ann","anu","jiss"],"age":[15,48,26],
#                  "marks":[45,78,25]},index=["D","E","A"])
# print(df)
# df1=pd.DataFrame({"name":["anju","kiran","amy"],
#                   "age":[15,14,19],
#                   "marks":[45,85,62]},index=["D","B","A"])
# df=df.reindex(["A","C","E","B"])  ##if the given index is alredy there,then it fills else it will be nan
# print(df)
# ###reindexing column wise(change position)
# df=df.reindex(columns=["age","marks","name"])
# print(df)
# ###to set dynamically as index or something like tis
# datedata=pd.date_range(start="10/1/2019",end="10/3/2019")
# print(datedata)
# df2=pd.DataFrame({"name":["anju","kiran","amy"],
#                   "age":[15,14,19],"marks":[45,85,62]},index=datedata)
# print(df2)
#
#
## renaming a dataframe
# import pandas as pd
# import numpy as np
# df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
# print(df1)
# print ("After renaming the rows and columns:")
# print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
#                 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))
#
# print(df1)
#
#
#
# # # #drop/deleting an element
#
# dframe = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'],
#                       columns=['ball','pen','pencil','paper'])
# print(dframe)
# print(dframe.drop(['red']))
# print(dframe)
# print(dframe.drop(['red','blue']))
# # #
# # # # #for columns
# df=dframe.drop(['pen','pencil'],axis=1)
# print(df)
# df=dframe.drop(columns="ball")
# print(df)
# #  # # # # # #
#
#
#
# # # #iterating a dataframe
# import pandas as pd
# d={'pid':[1,2,3],'name':['book','pen','pencle'],'price':[20,10,5]}
# df=pd.DataFrame(d,index=['a','b','c'])
# print(df)
#
# '''
# #To iterate over the rows of the DataFrame, we can use the following functions
# iteritems() − to iterate over the (key,value) pairs
# iterrows() − iterate over the rows as (index,series) pairs
# itertuples() − iterate over the rows as namedtuples
# '''
# for col in df:
#     print(col)
# for key,value in df.iteritems():    ##iteratingg colum wise
#     print(key)
#     print(value)
# for x in df.iteritems():  ## iterating column wise
#     print(x)
#
# ###row wise
# for i in df.iterrows():
#     print(i)        ##iterating rowwise
# for row_index,row in df.iterrows(): #iterating rowwise
#    print( row_index)
#    print(row)
#
# for row in df.itertuples():   #iterating rowwise as tuple
#     print(row)
#
#
#
########################################################
# sorting
# '''there are 2 kind of sorting available in the pandas
#
# '''
# import pandas as pd
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,8,9]]
# df=pd.DataFrame(l,index=['a','c','d','e','b','f'],
#                 columns=['id','age','mark'])
# print(df)
# ###we can sort by (index) labels
# dfnew=df.sort_index()        #default is ascending order
# print(dfnew)
# dfnew=df.sort_index(ascending=False)
# print(dfnew)
# # # # ##we can sort by label(column)
# dfnew=df.sort_index(axis=1)
# print(dfnew)
# # # # #we can sort by values,get new dataframe
# print(df.sort_values(by='age'))         ##must specify column names
# print(df.sort_values(by=['age','mark']))   # #we will not get the corrent sorting
# dfnew=df.sort_values(by='age',ascending=False)
# print(dfnew)
# #
# #
# #
# # # #  # # # # #
# #merge sort
# unsorted_df=pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
# print(unsorted_df)
# sorted=unsorted_df.sort_values(by='col1',kind='mergesort')
# print(sorted)
#
# l=[[1,2,3],[2,5,6],[3,8,9],[4,8,9],[5,9,8],[6,8,9]]
# df=pd.DataFrame(l,index=['a','c','d','e','b','f'],
#                 columns=['id','age','mark'])
# sorted=df.sort_values(by='age',kind='mergesort')
# print(sorted)
# # # # # # # # # # # # # # # # # # #  # #  #  # # # # # # # # #   # #  # # # #
# # #   # # # # #  ### # # # #  # # # # # # # # # # # # ## # #   # # ## # #### #