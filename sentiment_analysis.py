from exploring_data_structure import user_reviews_table, apps_table
import pandas as pd


# Creating an aggregated DataSet which maps apps to there calculated Total Sentiment:
aggregated_data = user_reviews_table.groupby('App').agg({'Sentiment_Polarity': "mean", 'Sentiment_Subjectivity': "mean"}).reset_index().dropna(axis=0)
aggregated_data['Sentiment'] = aggregated_data['Sentiment_Polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
sentiment_count = aggregated_data['Sentiment'].value_counts().sort_index(axis=0)

# Number of apps for each classification:
print("""
Applications classified by average Sentiment:
{} - Negative,
{} - Neutral,
{} - Positive.
""".format(sentiment_count[0], sentiment_count[1], sentiment_count[2]))


# Creating joined DataSet in which you can evaluate new data with application data:
joinedData = pd.merge(apps_table, aggregated_data, on='App')

# Sentiment of apps with the highest rating:
print("""
The Sentiment for the application rated most high from users review is {}
""".format(joinedData[joinedData['Rating'] == joinedData['Rating'].max()]['Sentiment'].drop_duplicates().tolist()))

# Average polarity for FREE applications:
paidApps_polarity = joinedData[joinedData['Type'] == 'Paid'].drop_duplicates()['Sentiment_Polarity'].mean()
freeApps_polarity = joinedData[joinedData['Type'] == 'Free'].drop_duplicates()['Sentiment_Polarity'].mean()
print("""
The average polarity of all Free applications is: {}
""".format(freeApps_polarity))

