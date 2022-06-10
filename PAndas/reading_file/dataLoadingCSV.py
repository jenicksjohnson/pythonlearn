import pandas as pd
#
# data=pd.read_csv("C:\\Users\\JENICKS\\Desktop\\Workspace\\pythonfiles\\Salary_Data.csv")
# print(data)
# # #
# ##
# print(type(data)) #save as data frame
# print(data.describe())# to know basic fn values to get a summery
# print(data.head())  # first 5 rows
# print(data.tail())  #last 5 rows
# print(data.head(10))    #first 10 rows
# print(data.columns)
# print(data.Salary.describe())
# # # # print(data.describe())
# print(data.Salary.mean())
# print(data.Salary.std())
# print(data.Salary.sum())
# #
# #
# #
# # salary>60000
# data.loc[data.Salary>60000,'Salary']=70000
# print(data)
# #
# #
# #
# #converting a data to csv
# #
# #
# data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
#         'Age':[28,34,29,42]}
# df = pd.DataFrame(data)
# print(df)
# #
# #
# #
# # convertion
# # df.to_csv("data.csv")
# df.to_csv("data.csv",index=False)
# #
# # from csv to python
# s=pd.read_csv("data.csv")
# print(s)
# #
# #
# #
# #diff loading method
# # by using os modues
# import os
# print(os.getcwd())
# os.chdir("C:\\Users\\JENICKS\\Desktop\\Workspace\\pythonfiles")
# print(os.getcwd())
# print(os.listdir())
# df=pd.read_csv("Salary_Data.csv")
# print(df)
# #
# #
# #
# #
# #
# #
df1=pd.read_csv("C:\\Users\\JENICKS\\Desktop\\Workspace\\pythonfiles\\mtcars1.csv")
# print(df1)
# #
# print(df1.columns)
#
df1.set_index("Unnamed: 0",inplace=True)
print(df1)
#
# [, 1]	mpg	Miles/(US) gallon
# [, 2]	cyl	Number of cylinders
# [, 3]	disp	Displacement (cu.in.)
# [, 4]	hp	Gross horsepower
# [, 5]	drat	Rear axle ratio
# [, 6]	wt	Weight (1000 lbs)
# [, 7]	qsec	1/4 mile time
# [, 8]	vs	Engine (0 = V-shaped, 1 = straight)
# [, 9]	am	Transmission (0 = automatic, 1 = manual)
# [,10]	gear	Number of forward gears
# [,11]	carb	Number of carburetors
#
#
#
# mileage greter than 15 and less than 20
# print(df1.loc[(df1.mpg>15)&(df1.mpg<20)])
#
#
# manual tye car details with 6 cylinder engine
# print(df1.loc[(df1.cyl==6)& (df1.am==1)])
# #
# #
# change automatic car parameter from 0 to 2 in the same df
# df1.loc[df1.am==0,"am"]=2
# print(df1)
# #
# print(df1["am"].replace(0,2))
# print(df1)
#
#
# adding 2 to every data in cs column
# df1.loc[:,"vs"]+=2
# print(df1.vs)
# df1["vs"]+=2
# print(df1.vs)





