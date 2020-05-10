from exploring_data_structure import apps_table, user_reviews_table
import numpy as np


def get_app_details_by_letter(letter):
    letter = str.upper(letter)
    return apps_table[apps_table['App'].str.upper().str.startswith(letter)].drop_duplicates()


def get_average_polarity(app_name):
    avg = user_reviews_table[user_reviews_table['App'] == app_name]['Sentiment_Polarity'].mean()
    if np.isnan(avg):
        return None
    return avg


def get_sentiment(app_name):
    avg_polarity = get_average_polarity(app_name)
    if avg_polarity < 0:
        return 'Negative'
    elif avg_polarity > 0:
        return 'Positive'
    elif avg_polarity == 0:
        return 'Neutral'
    else:
        return 'Error: Application ' + app_name + ' doesnt appear in this DataSet'



