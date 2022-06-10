import pandas as pd
# .txt
# .txt
# .xls
# .xlxs
# json
# and more
# text=pd.read_table("loadingfile.txt")
# print(text)
# #
# print(type(text))
# #
# print(text.columns)
# print(len(text.columns))
# #
# #
# text=pd.read_table("loadingfile.txt",sep=",")    #this makes a dataframe
# print(text)
# print(text.columns)
# print(len(text.columns))
# # # # #
# # # # #
# text.set_index('id',inplace=True)          ##make id as index
# print(text)
# print(text.values)
# # # # # # #
# #
# ###
# #
# # # #  ##
# df=pd.read_csv("loadingfile.txt") #if it is not coma seperated we should mention sep=";"
# print(df)
# print(type(df))
# #
# #
# df=pd.read_csv("txt1.txt",sep=";") #if it is not coma seperated we should mention sep=";"
# print(df)
# print(type(df))
# #
# #
# #



df=pd.read_csv("txt3.tsv")
print(df)
print(type(df))

# print("in\tdia")



































