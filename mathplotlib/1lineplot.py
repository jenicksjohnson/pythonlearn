import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# plt.plot([10,15,25,18])
# plt.show()
#
# if there is 2 sequence of data
# plt.plot([10,15,25,30],[2,4,6,8])
# plt.show()
# # plt.plot([x-axis values],[y-axis values])
#
# plt.plot([10,15,25,30],[2,4,6,8])
# # # #
# plt.xlabel("numbers")
# plt.ylabel("index")
# plt.title("myplot")
# plt.show()
# #
# #
# x1=[10,15,25,30]
# y1=[2,4,6,8]
# x2=[15,17,25,32]
# y2=[2,5,7,10]
# x3=[10,20,30,40]
# y3=[4,3,6,12]
# plt.plot(x1,y1,'g8',label='lineone',linewidth=3)
# plt.plot(x2,y2,'r^',label='line two',linewidth=5)
# plt.plot(x3,y3,'r--',label='line one',linewidth=5)
# plt.plot(x3,y3,'yo',label='line one',linewidth=5)
# plt.plot(x3,y3,'ys',label='line one',linewidth=5)
# # # #
# plt.xlabel("numbers")
# plt.ylabel("index")
# plt.title("myplot")
# plt.grid()  ###giving grids
# plt.legend() ###shows line details
# plt.show()
# #
# #
###using dataframe
# df = pd.DataFrame({
#    'pig': [20, 18, 489, 675, 1776],
#    'horse': [4, 25, 281, 600, 1900]
#   }, index=[1990, 1997, 2003, 2009, 2014])
# print(df)
# df.plot.line(subplots=True)   ##convertion
# plt.savefig("file.png")  ##saving it into png
# plt.show()
# #
#
# df = pd.DataFrame({
#    'pig': [20, 18, 489, 675, 1776],
#    'horse': [4, 25, 281, 600, 1900],
#     'x':[5,38,51,100,200]
#   }, index=[1990, 1997, 2003, 2009, 2014])
# print(df)
#
# horizontally
# #we can specify each subplot
# plt.subplot(3,1,1)  ##(no of plots,below/side,which plot)
# plt.plot(df.pig,df.horse,'y--')
# plt.subplot(3,1,2)
# plt.plot(df.pig,df.x,'gd')
# plt.subplot(3,1,3)
# plt.plot(df.horse,df.x,'rs')
# plt.show()
#
# plt.subplot(1,2,1)  ##(no of plots,below/side,which plot)
# plt.plot(df.pig,df.horse,'y--')
# plt.subplot(1,2,2)  ##(no of rows,number of columns,place of figure)
# plt.plot(df.pig,df.x,'gd')
# plt.show()
# #
# #
# #
# #
# #
# # Bar plots
# plt.bar([1,3,5,7,9],[5,2,7,8,2])  ##(x,y)
# plt.show()
#
#
# plt.bar([1,3,5,7,9],[5,2,7,8,2],label="example")  ##(x,y)
# plt.legend()
# plt.xlabel("bar number")
# plt.ylabel("bar height")
# plt.title("bar graph")
# plt.show()
# #
# #
# # bar graph for a data frame
# #
# df = pd.DataFrame({
#     'name':['john','mary','peter','jeff','bill','lisa','jose'],
#     'age':[23,78,22,19,45,33,20],
#     'gender':['M','F','M','M','M','F','M'],
#     'state':['california','dc','california','dc','california','texas','texas'],
#     'num_children':[2,0,0,3,2,1,4],
#    'num_pets':[5,1,0,5,2,2,3]
# })
# print(df)
#bar plot for single column/field
# df['age'].plot.bar()
# plt.show()
# #
# # bar plot by 2u columns/fields
# df.plot.bar(x='age',y='num_pets')
# plt.show()
# #
# # if we want to change label
# df.plot.bar(x='age',y='num_pets',label="Numofpets")
# plt.show()
#
# # if we want to change x-axis and y-axis label
# df.plot.bar(x='age',y='num_pets',label="Numofpets",xlabel="Age",ylabel="pets",title="Age VS no.of pets")
# plt.show()
#
# # if we want to change the color of graph
# df.plot.bar(x='age',y='num_pets',label="Numofpets",xlabel="Age",ylabel="pets",title="Age VS no.of pets",color="lightblue")
# plt.show()
#
#
# plt.bar(df.age,df.num_pets,label="NumOfPets",color="orange",width=3)
# plt.legend()
# plt.title("Age vs pets")
# plt.xlabel("Age")
# plt.ylabel("Pets")
# plt.show()