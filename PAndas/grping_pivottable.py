'''pivot table'''
"""
pivot table is used to summerize and
aggregate data inside dataframe
"""

import numpy as np
import pandas as pd
#
data=pd.read_excel("C:\\Users\\JENICKS\\Desktop\\Workspace\\pythonfiles\\SaleData.xlsx")
print(data)
# print(data.columns)
# print(data.nunique())
#
# # ###grouping by region and manager
# df=pd.pivot_table(data,index=['Region','Manager'])
# print(df)
# # #
# # #
# # ##group by condition
# print(data.query('Region==["West"]'))
# #
# df=pd.pivot_table(data,index=["Region","Manager"])
# print(df)
# print(df.keys())
# print(df.columns)
# print(df.index)
# print(df.values)
# #
# #
# #setting with specific values  by detail seperation
# print(pd.pivot_table(data,index=["Region","Manager","SalesMan"],
#                      values="Sale_amt"))
#
#
# # can use aggregate fn using aggfunc. (mean,sum,std..)
# print(pd.pivot_table(data,index="Region",aggfunc="mean"))
#
# ##q:: find unit price of each sales man and their managers and region
# print(pd.pivot_table(data,index=["Region","Manager","SalesMan"],
#                      values="Unit_price"))
# #
# #
# # Q: find itemwise unit sold(average value)
#
# print(pd.pivot_table(data,index=["Item"],
#                      values="Units",aggfunc="mean"))
# #
# print(pd.pivot_table(data,index=["Item"],
#                      values="Units"))    ##its an average value
# #
# #
# Q:: Find item wise unit sold(total number)
# print(pd.pivot_table(data,index="Item",values="Units",aggfunc="sum"))
#
#
# #Q: find regionwise total sale amount
# print(pd.pivot_table(data,index=["Region"],values="Sale_amt",aggfunc="sum"))
#
#
# #Q: find region wise and item-wise total sale amount
# print(pd.pivot_table(data,index=["Region","Item"],values="Sale_amt",aggfunc="sum"))
#
#
# #Q: count manager wise sale orders and total sale amount for each manager
# print(pd.pivot_table(data,index=["Manager"],values="Sale_amt",aggfunc=["sum",len]))
# or........................
# print(pd.pivot_table(data,index=["Manager"],values="Sale_amt",aggfunc=[np.sum,len]))
#
#
# Q: Find total sale of each sales man and manager and print the actual total amount
# of all the sales at bottom
# print(pd.pivot_table(data,index=["Manager","SalesMan"],values="Sale_amt",aggfunc=[np.sum],margins=True))
# margins =trues gives total of all at the bottom
#
#
# Q:: Find the total sale amount of region-wise,manager-wise,sales-man wise
# result=(pd.pivot_table(data,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc=[np.sum]))
# print(result)
#
##from the result find the sale amount if manager is dougles
# group by condition
# print(result.query("Manager==['Douglas']"))
# if we take datas from data we get it by with out sorting
# print(data.query("Manager==['Douglas']"))
#
#
#
##q: find region wise no of Televison and home theatre sold
# result=pd.pivot_table(data,index=["Region","Units","Item"],
#                       values="Sale_amt",aggfunc=[np.sum])
# print(result)
# print(result.query('Item==["Television"]  | Item==["Home Theater"]'))
# print(result.query('Item==["Television","Home Theater"]'))
# print(result.query('Item in ["Television","Home Theater"]'))
# #
#
# Q: find the max min sale amount of the items
result=pd.pivot_table(data,index=["Item"],
                      values="Sale_amt",aggfunc=["max","min"])
print(result)
#












