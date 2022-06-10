import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#
#
# df=pd.read_csv("C:\\Users\\Jenicks\\Desktop\\Workspace\\pythonfiles\\mtcars1.csv")
# print(df)
#
# import seaborn as sns
# sns.boxplot(x='cyl',y='mpg',data=df)
# plt.show()
#
#
#
#
# df=pd.DataFrame([[5.1,3.5,0],[4.9,3.0,0],
#                  [7.0,3.2,1],[6.4,3.2,1],[5.9,3.0,2]],
#                 columns=['length','width','species'])
#
# print(df)
# #
# sns.scatterplot(x='length',y='width',hue='species',data=df,
#                 palette=['green','orange','brown'])
# plt.show()
#
#
#
# data=sns.load_dataset('iris')
# ### ### ###
# print(data)
# print(type(data))
# print(data.columns)

### ### ###
# sns.lineplot(x='sepal_length',y='sepal_width',data=data)
# plt.title("Iris_Data")
# plt.show()

# ### ### ###
# sns.lineplot(x='sepal_length',y='sepal_width',data=data)
# plt.title("Iris_Data")
# plt.xlim(5)          ###set x starting point
# plt.show()

# ### ### ###
# sns.scatterplot(x='sepal_length',y='sepal_width',data=data,
#                 hue='species',palette=['red','yellow','black'])
# plt.show()
#
#
# sns.relplot(x='sepal_length',y='sepal_width',data=data,
#                 hue='species')
# plt.show()
# #
# #
# #
# ### ### ####
# sns.violinplot(x='sepal_length',y='species',data=data)
# plt.show()










