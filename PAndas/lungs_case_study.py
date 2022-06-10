import pandas as pd
#
df=pd.read_csv("C:\\Users\\JENICKS\\Desktop\\Workspace\\pythonfiles\\lung.csv")
print(df)
print(df.columns)
print(df.shape)
#
"""
inst:	Institution code
time:	Survival time in days
status:	censoring status 1=censored, 2=dead
age:	Age in years
sex:	Male=1 Female=2
ph.ecog:	ECOG performance score (0=good 5=dead)
ph.karno:	Karnofsky performance score (bad=0-good=100) rated by physician
pat.karno:	Karnofsky performance score as rated by patient
meal.cal:	Calories consumed at meals
wt.loss:	Weight loss in last six months
"""
df.set_index("Unnamed: 0",inplace=True)
print(df)
#
# changeing 1 and 2 into male and female
#
# print(df.sex)
#
# df.loc[df.sex==1,"sex"]="Male"
# df.loc[df.sex==2,"sex"]="Female"
# print(df.sex)
# by replace function
# df["sex"]=df["sex"].replace([1,2],["Male","Female"])
# print(df.sex)
#
#
#
#
#
#
# removing selective items from a column
# creating selected indexs to a list
print(df.loc[df.status==1].index)
l=df.loc[df.status==1].index.tolist()
print(l)
df.drop(l,inplace=True) ##inplace = true maens assigning to the same dataframe
print(df)
print(df.status)

