from utilities import files_functions as ff
import pandas as pd
import matplotlib.pyplot as plt


class Apps:
    def __init__(self):
        self.table = ff.load_csv_file('resources/apps.csv')
        self.table['Installs'] = self.table['Installs'].str.replace('+', '')
        self.table['Installs'] = self.table['Installs'].str.replace(',', '').astype('int64')
        self.table['Last Updated'] = pd.to_datetime(self.table['Last Updated'])

    def structure(self):
        print("\n---Apps Table---")
        print("There are {} rows".format(self.table.shape[0]))
        print("There are {} columns".format(self.table.shape[1]))
        print("The attributes in this Tables are as followed: {}".format(list(self.table.keys())) + '\n')

    def aggregation_for_category_analysis(self):
        aggregated_category = self.table[['App', 'Category', 'Rating']].drop_duplicates()
        aggregated_category = aggregated_category.groupby('Category').agg(
            {'Rating': ['mean', 'std', 'median', lambda x: x.value_counts().index[0]]})
        aggregated_category.rename(columns={'<lambda_0>': 'mode'}, inplace=True)
        return aggregated_category

    def rating_std_for_agg_category(self):
        # Built for visual purpose only, see usage under script 'visual.analysis'
        rating_std = self.aggregation_for_category_analysis()[('Rating', 'std')].reset_index()
        return rating_std

    def aggregation_for_genre_analysis(self):
        # Built for visual purpose only, see usage under script 'visual.analysis'
        aggregated_genre = self.table[['App', 'Rating', 'Genres']].drop_duplicates()
        aggregated_genre = aggregated_genre.groupby('Genres').agg({'Rating': 'mean'}).reset_index().dropna()
        return aggregated_genre

    def category_analysis(self):
        print("""
*** You can now see a plot that shows scatter of categories std's, under 'std_scatter.png'. ***""")

        print("There are {} categories in our Dataset.".format(self.table['Category'].drop_duplicates().count()) + '\n')

        # Finding most STABLE category:
        category_dist = self.aggregation_for_category_analysis().sort_values(by=[('Rating', 'std')])
        print("""
This data set maps each category to its analysis, and is ordered from the most stable category (top)
to the least stable one (bottom)

        {}""".format(category_dist))

        stable = category_dist.index[0]
        std_value = category_dist[('Rating', 'std')].head(1).tolist()
        average = category_dist[('Rating', 'mean')].head(1).tolist()
        median = category_dist[('Rating', 'median')].head(1).tolist()
        mode = category_dist[('Rating', 'mode')].head(1).tolist()

        print("""
The most stable category is {}
it has the smallest std value {}
and you can see the average {} the median {} and mode {} which are almost identical
        """.format(stable, std_value, average, median, mode))

        # Finding Categories for them the data distributes normally:
        # the difference between mode-median-mean should be less then 0.5 in order to consider it a Normal Dist.
        category_dist.columns = category_dist.columns.droplevel(0)
        category_dist['median-mean'] = category_dist.apply(lambda x: x['median'] - x['mean'], axis=1)
        category_dist['median-mode'] = category_dist.apply(lambda x: x['median'] - x['mode'], axis=1)
        category_dist['mode-mean'] = category_dist.apply(lambda x: x['mode'] - x['mean'], axis=1)
        category_dist = category_dist.drop(category_dist.columns[[0, 1, 2, 3]], axis=1).abs()
        category_dist['median-mode'] = category_dist['median-mode'].apply(lambda x: 'True' if x <= 0.5 else 'False')
        category_dist['median-mean'] = category_dist['median-mean'].apply(lambda x: 'True' if x <= 0.5 else 'False')
        category_dist['mode-mean'] = category_dist['mode-mean'].apply(lambda x: 'True' if x <= 0.5 else 'False')
        category_dist = category_dist[category_dist['median-mode'] == 'True']
        print("""
These are the Categories in which we have Normal Distribution:
{}
        """.format(category_dist.index))

        self.rating_std_for_agg_category().plot(kind='scatter', x='Category', y=('Rating', 'std'), color='sandybrown')
        plt.title('Scatter of std of Ratings values for each Category')
        plt.xticks(fontsize=8, rotation=90)
        plt.savefig('std_scatter.png')

    def popularity_analysis(self):
        # the app with most installation:
        print("""
The Apps that have the most installations are : 
{}
            """.format(
            list(self.table[self.table['Installs'] == self.table['Installs'].max()]['App'].
                 drop_duplicates())))

        # most updated app:
        print("""
The most updated apps are:
{}
            """.format(list(self.table[self.table['Last Updated'] == self.table['Last Updated'].
                            max()]['App'])))

        # Number of Apps for each Genre:
        print("""
The number of applications for each Genre are as followed:
{}
        """.format(self.table[['App', 'Genres']].drop_duplicates()['Genres'].value_counts()))

        # most popular app Genre:
        popular_genre = self.table.groupby('Genres')['Installs'].sum().reset_index().max()
        print("""
The most popular app-Genre is: {}
It has {} installs
            """.format(popular_genre[0], popular_genre[1]))

        self.aggregation_for_genre_analysis().plot(kind='bar', x='Genres', y='Rating', color='darksalmon', width=0.3,
                                                   figsize=(30, 6))
        plt.title('The average Rating for each APP Genre')
        plt.xlabel('Category')
        plt.xticks(fontsize=8, rotation=90)
        plt.ylabel('Rating Average')
        plt.savefig('average_rating.png')
        print("""
*** You can now see a plot that shows average rating for each Genre, under 'average_rating.png'. ***""")

        free_installs = self.table[self.table['Type'] == 'Free'].drop_duplicates()['Installs'].sum()
        paid_installs = self.table[self.table['Type'] == 'Paid'].drop_duplicates()['Installs'].sum()
        print("""
Free installs are more popular
The number of downloads for free apps is: {}
in compare for paid apps, where there's only {} downloads.
        """.format(free_installs, paid_installs))

        self.free_app_to_list()

    def free_app_to_list(self):
        free_apps = self.table[self.table['Type'] == 'Free'].drop_duplicates(subset='App')['App']
        print("""
List of all FREE apps:
{}
        """.format(free_apps.to_list))

    def extra_info(self):
        maxM = 1024 * int(self.table[self.table['Size'].str.upper().str.endswith('M')].max()['Size'][:-1])
        maxK = int(self.table[self.table['Size'].str.upper().str.endswith('K')].max()['Size'][:-1])
        if maxM > maxK:
            max = str(int(maxM / 1024)) + 'M'
            heaviest_app = self.table[self.table['Size'] == max]['App'].drop_duplicates()
        else:
            max = str(maxK) + 'K'
            heaviest_app = self.table[self.table['Size'] == max]['App'].drop_duplicates()
        print("""
The heaviest size is: {}
The Apps with that size are: {}
            """.format(max, heaviest_app.to_list()))

