import plotly.express as px
#
df=px.data.iris()
#
# print(df)
# fig=px.scatter(df,x='species',y='petal_width',size='petal_length',color='species')
# fig.show()
#
# 3d drawing plot
# fig=px.line_3d(df,x='sepal_width',y='petal_length',z='petal_width',color='species')
# fig.show()
#
#
# 3d scatter plot
fig=px.scatter_3d(df,x='sepal_width',y='petal_length',z='petal_width',color='species')
fig.write_html('first_figure.html',auto_open=True)
fig.show()



