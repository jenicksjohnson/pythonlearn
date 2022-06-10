# import pandas as pd
#
# # GitHub is a hosting platform for public and private software codes.
# diamond_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
# diamond_data = pd.read_csv('24_diamonds.csv')
# print(diamond_data)
# print(diamond_data.shape)
# print(diamond_data.columns)
# print(diamond_data.describe())
# print(diamond_data.nunique())
# # #
# # #
# # # Create a column "quality_color" by joining 'cut' and 'color'.
# # # Then, remove 'cut' and 'color' columns from the DataFrame.
# diamond_data['quality_color'] = diamond_data['cut'] + ' ' + diamond_data['color']
# diamond_data.drop(['cut', 'color'], axis=1, inplace=True)
# # # OR
# # diamond_data.pop('cut')
# # diamond_data.pop('color')
# print(diamond_data.head())
# #
# # # Bringing the 'quality_color' column to the second position.
# print(diamond_data.columns)
# print(diamond_data)
# new_diamond_data = diamond_data.reindex(
#     columns=['carat', 'quality_color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z'])
# print(new_diamond_data)
