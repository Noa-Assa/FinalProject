from utilities import files_functions as ff
import matplotlib.pyplot as plt


class UserReviews:
    def __init__(self):
        self.table = ff.load_csv_file('resources/user_reviews.csv')

    def structure(self):
        print("\n---User Reviews Table---")
        print("There are {} rows".format(self.table.shape[0]))
        print("There are {} columns".format(self.table.shape[1]))
        print("The attributes in this Tables are as followed: {}".format(list(self.table.keys())) + '\n')

    def aggregation_for_sentiment_analysis(self):
        # Creating an aggregated DataSet which maps apps to there calculated Total Sentiment:
        aggregated_data = self.table.groupby('App').agg(
            {'Sentiment_Polarity': "mean", 'Sentiment_Subjectivity': "mean"}).reset_index().dropna(axis=0)
        aggregated_data['Sentiment'] = aggregated_data['Sentiment_Polarity'].apply(
            lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
        return aggregated_data

    def sentiment_count(self):
        sentiment_count = self.aggregation_for_sentiment_analysis()['Sentiment'].value_counts().sort_index(axis=0)
        return sentiment_count

    def sentiment_analysis(self):
        sentiment_count = self.sentiment_count()
        # Number of apps for each classification:
        print("""
Applications classified by average Sentiment:
    {} - Negative,
    {} - Neutral,
    {} - Positive.
        '""".format(sentiment_count[0], sentiment_count[1], sentiment_count[2]))

        plt.title('Count of Application classified by Sentiment')
        plt.xlabel('Sentiment')
        plt.ylabel('number of applications')
        ax = sentiment_count.plot(kind='bar', color='coral')
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))
        plt.savefig('sentiment_count.png')
        print("""
*** You can now see a plot that present how many applications exists in each sentiment, under 'sentiment_count.png""")
