from exploring_data_structure import apps_table
from dist_analysis import aggregated_category

# Basic Exploring:
print("---Basic Explore and Analysis for Apps Table---")

print("Total count of apps categories: {} ".format(apps_table['Category'].drop_duplicates().count()) +'\n')

# To make sure that size would be the heaviest, and wasn't entered in a wrong way
maxM = 1024 * int(apps_table[apps_table['Size'].str.upper().str.endswith('M')].max()['Size'][:-1])
maxK = int(apps_table[apps_table['Size'].str.upper().str.endswith('K')].max()['Size'][:-1])
if maxM > maxK:
    max = str(int(maxM/1024)) + 'M'
    heaviest_app = apps_table[apps_table['Size'] == max]['App'].drop_duplicates()
else:
    max = str(maxK) + 'K'
    heaviest_app = apps_table[apps_table['Size'] == max]['App'].drop_duplicates()
print("""
    The heaviest size is: {}
    The Apps with that size are: {}
    """.format(max, heaviest_app.to_list()))

# the app with most installation:
print("""
    The Apps that have the most installations are : 
    {}
    """.format(list(apps_table[apps_table['Installs'] == apps_table['Installs'].max()]['App'].drop_duplicates())))

# most updated app:
print("""
    The most updated apps are:
    {}
    """.format(list(apps_table[apps_table['Last Updated'] == apps_table['Last Updated'].max()]['App'])))

# most popular app Genre:
popular_genre = apps_table.groupby('Genres')['Installs'].sum().reset_index().max()
print("""
    The most popular app-Genre is: {}
    It has {} installs
    """.format(popular_genre[0], popular_genre[1]))

# Number of Apps for each Genre:
print("""
The number of applications for each Genre are as followed:
{}
""".format(apps_table[['App', 'Genres']].drop_duplicates()['Genres'].value_counts()))

# FREE Apps:
free_apps = apps_table[apps_table['Type'] == 'Free'].drop_duplicates(subset='App')['App']
print("""
List of all FREE apps:
{}
""".format(free_apps.to_list))


free_installs = apps_table[apps_table['Type'] == 'Free'].drop_duplicates()['Installs'].sum()
paid_installs = apps_table[apps_table['Type'] == 'Paid'].drop_duplicates()['Installs'].sum()
print("""
Free installs are more popular
The number of downloads for free apps is: {}
in compare for paid apps, where there's only {} downloads.
""".format(free_installs, paid_installs))

# Built for visual purpose only, see usage under script 'visual.analysis'
aggregated_genre = apps_table[['App', 'Rating', 'Genres']].drop_duplicates()
aggregated_genre = aggregated_genre.groupby('Genres').agg({'Rating': 'mean'}).reset_index().dropna()
std_for_vis = aggregated_category[('Rating', 'std')].reset_index()

