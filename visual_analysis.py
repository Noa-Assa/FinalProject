from sentiment_analysis import sentiment_count, freeApps_polarity, paidApps_polarity
from app_data_analysis import aggregated_genre, std_for_vis
import matplotlib.pyplot as plt
import numpy as np


plt.title('Count of Application classified by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('number of applications')
ax = sentiment_count.plot(kind='bar', color='coral')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))
plt.show()


aggregated_genre.plot(kind='bar', x='Genres', y='Rating', color='darksalmon', width=0.3, figsize=(30, 6))
plt.title('The average Rating for each APP Genre')
plt.xlabel('Category')
plt.xticks(fontsize=8, rotation=90)
plt.ylabel('Rating Average')
plt.show()


plt.title('Comparison between Free & Paid by average of sentiment polarity:')
plt.ylim([-1, 1])
plt.xlim([-2,3])
plt.xticks(np.arange(2), ('Free Apps', 'Paid Apps'))
plt.scatter([0], freeApps_polarity, color='darkorchid')
plt.scatter([1], paidApps_polarity, color='mediumvioletred')
plt.legend(['difference is: ' + str(freeApps_polarity-paidApps_polarity)])
plt.show()


std_for_vis.plot(kind='scatter', x='Category', y=('Rating', 'std'), color='sandybrown')
plt.title('Scatter of std of Ratings values for each Category')
plt.xticks(fontsize=8, rotation=90)
plt.show()
