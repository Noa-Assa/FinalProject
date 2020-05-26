from data_analysis.apps import Apps
from data_analysis.user_reviews import UserReviews
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class AppStoreAnalysis:
    def __init__(self):
        self.apps = Apps()
        self.reviews = UserReviews()
        self.joinedData = pd.merge(self.apps.table, self.reviews.aggregation_for_sentiment_analysis(), on='App')

    def sentiment_of_high_rating(self):
        # Sentiment of apps with the highest rating:
        print("""
The Sentiment for the application rated most high from users review is {}
        """.format(
            self.joinedData[self.joinedData['Rating'] == self.joinedData['Rating'].max()]['Sentiment'].drop_duplicates()
                .tolist()))

    def free_apps_polarity(self):
        return self.joinedData[self.joinedData['Type'] == 'Free'].drop_duplicates()['Sentiment_Polarity'].mean()

    def paid_apps_polarity(self):
        return self.joinedData[self.joinedData['Type'] == 'Paid'].drop_duplicates()['Sentiment_Polarity'].mean()

    def sentiment_analysis(self):
        # Average polarity for FREE applications:
        freeApps_polarity = self.free_apps_polarity()
        paidApps_polarity = self.paid_apps_polarity()
        print("""
The average polarity of all FREE applications is: {}
        """.format(freeApps_polarity))
        print("""
The average polarity of all PAID applications is: {}
        """.format(paidApps_polarity))

        plt.title('Comparison between Free & Paid by average of sentiment polarity:')
        plt.ylim([-1, 1])
        plt.xlim([-2, 3])
        plt.xticks(np.arange(2), ('Free Apps', 'Paid Apps'))
        plt.scatter([0], freeApps_polarity, color='darkorchid')
        plt.scatter([1], paidApps_polarity, color='mediumvioletred')
        plt.legend(['difference is: ' + str(freeApps_polarity - paidApps_polarity)])
        plt.savefig('scatter_cost.png')
        print("""
*** You can now see a plot that present the difference between free and paid apps by their sentiment polarity,
 under 'scatter_cost.png'. ***""")

        self.reviews.sentiment_analysis()


