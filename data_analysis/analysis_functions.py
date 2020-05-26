import numpy as np


# This script was a part of the project, but i have decided not to implement it in my program.

def get_app_details_by_letter(letter, table):
    letter = str.upper(letter)
    return table[table['App'].str.upper().str.startswith(letter)].drop_duplicates()


def get_average_polarity(app_name, table):
    avg = table[table['App'] == app_name]['Sentiment_Polarity'].mean()
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



