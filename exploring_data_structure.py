import files_functions as ff
import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# from eralchemy import render_er
# from sqlalchemy import (MetaData, Table, Column, Integer, ForeignKey, String, create_engine)

# Reading files:
apps_table = ff.load_csv_file('apps.csv')
user_reviews_table = ff.load_csv_file('user_reviews.csv')

# simple manipulation over columns to make is easier to work:
apps_table['Installs'] = apps_table['Installs'].str.replace('+', '')
apps_table['Installs'] = apps_table['Installs'].str.replace(',', '').astype('int64')
apps_table['Last Updated'] = pd.to_datetime(apps_table['Last Updated'])


# Basic Structure:
print("\n---Apps Table---")
print("There are {} rows".format(apps_table.shape[0]))
print("There are {} columns".format(apps_table.shape[1]))
print("The attributes in this Tables are as followed: {}".format(list(apps_table.keys())) + '\n')
print("---User Reviews Table---")
print("There are {} rows".format(user_reviews_table.shape[0]))
print("There are {} columns".format(user_reviews_table.shape[1]))
print("The attributes in this Tables are as followed: {}".format(list(user_reviews_table.keys())) + '\n')

# ERD - Creation of ERD model to present connectivity
# metadata = MetaData()
# engine = create_engine('sqlite:///cdb.db')
# app = Table('app', metadata,
#               Column('App', String()),
#               Column('Category'),
#               Column('Rating'),
#               Column('Reviews'),
#               Column('Size'),
#               Column('Installs'),
#               Column('Type'),
#               Column('Price'),
#               Column('Content Rating'),
#               Column('Genres'),
#               Column('Last Updated'),
#               Column('Current Ver')
#             )
# review = Table('User Reviews', metadata,
#                Column('App',  ForeignKey('app.App')),
#                Column('Translated_Review'),
#                Column('Sentiment'),
#                Column('Sentiment_Polarity'),
#                Column('Sentiment_Subjectivity')
#                )
# render_er(metadata, 'ERD-model.png')
# plt.imshow(mpimg.imread('ERD-model.png'))
# plt.rcParams["figure.figsize"] = (15,10)
# plt.show()
