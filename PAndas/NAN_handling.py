import numpy as np
import pandas as pd
#
Df=pd.DataFrame([[1,3,2],[np.nan,2,5],[5,7,10],[4,8,3],[5,np.nan,6]],
                columns=['c1','c2','c3'])
print(Df)
# print(Df.isna())  ## show null values
# print(Df.notna())
# print(Df.isna().any())
# print(Df.isna().sum())         #shows number of nan values in a column
# print(Df[Df['c1'].isnull()])   ##to find the row which is having null in c1 column
# print(".....................")
# print(Df.iloc[4:])
# print(Df.iloc[4,:].isna())
# dfnew=Df.dropna()    # ##to drop value with value nan
# print(dfnew)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# dfnew=Df.fillna(10)  ###to fill nan position
# print(dfnew)
# #
# dfnew=Df.bfill()  ###to fill an nan value from the below pos
# print(dfnew)
# #
# dfnew=Df.ffill()  ###to fill an nan value from the upper pos
# print(dfnew)
# #
# dfnew=Df.interpolate()  ###to fill an nan value from random number
# print(dfnew)
# #
# dfnew=Df.replace(np.nan,2)  ###to fill 2 with nan values
# print(dfnew)
#
#
# change 5 value in 4th col into nan
# Df.loc[4,0]=np.nan    ## changes value in 4th row only
# print(Df)
#
# dfnew=Df['c1'].replace(5,np.nan)
# print(dfnew)
#or
# Df['c1']=Df['c1'].replace(5,np.nan)
# print(Df)
#or
# Df.loc[Df.c1==5,'c1']=np.nan
# print(Df)
#
# q: change "NaN" in 'c2' column nan value
#
#
# print(Df['c2'].mean())
# #
# D=Df.c2.fillna(Df.c2.mean())    # new data frame
# print(D)
# # # #
# Df.loc[Df.c2.isna(),'c2']=Df.c2.mean()
# print(Df)
# #
# print(Df['c2'].replace(np.nan,Df['c2'].mean()))
#
#
#
##
#### # # # # # # # # # #