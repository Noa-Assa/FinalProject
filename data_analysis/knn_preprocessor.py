import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from utilities import files_functions as ff


def is_none_free(df):
    if not df.isnull().values.any():
        return True
    else:
        print(df.isnull().sum())
        return False


def preprocessing():
    df1 = ff.load_csv_file('resources/apps.csv')
    df2 = ff.load_csv_file('resources/user_reviews.csv')
    df1 = df1[['App', 'Category', 'Rating', 'Size', 'Type', 'Price', 'Genres']]
    df2 = df2[['App', 'Sentiment', 'Sentiment_Polarity', 'Sentiment_Subjectivity']]

    # Organize data:
    df1['Size'] = df1['Size'].replace({'K': '*1e3', 'M': '*1e6', 'Varies with device': -99999, 'k': '*1e3'},
                                      regex=True).map(pd.eval).astype(int)
    df1['Price'] = df1['Price'].str.replace('$', '').astype(float)

    df = pd.merge(df1, df2, on='App')

    # Creating copies:
    x = df[['App', 'Category', 'Rating', 'Size', 'Type', 'Price', 'Genres', 'Sentiment_Polarity',
            'Sentiment_Subjectivity']].copy()
    y = pd.DataFrame(df['Sentiment'].copy().reset_index(drop=True), columns=['Sentiment'])

    # Exploring data categorical columns:
    print("Exploring data unique categorical columns:")
    for col_name in df1.columns:
        if x[col_name].dtypes == 'object':
            unique_cat = len(x[col_name].unique())
            print("{} has {}".format(col_name, unique_cat))

    # dealing nan values:
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    x[['Rating', 'Size', 'Price', 'Sentiment_Polarity', 'Sentiment_Subjectivity']] = imp.fit_transform(x[['Rating', 'Size',
                                                                                                          'Price',
                                                                                                          'Sentiment_Polarity',
                                                                                                          'Sentiment_Subjectivity']])
    print("is None Free? -")
    print(is_none_free(x[['Rating', 'Size', 'Price', 'Sentiment_Polarity', 'Sentiment_Subjectivity']]), '\n')

    # dealing with categorical columns:
    x_categorical = x.select_dtypes(include=['object']).copy()
    x_dummies = pd.get_dummies(x_categorical)
    x = x.drop(columns=['App', 'Category', 'Type', 'Genres'])
    x = x_dummies.merge(x, left_index=True, right_index=True)
    del (x_categorical, x_dummies)

    # for categorical dealing with nan values:
    imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    y_values = pd.DataFrame(imp.fit_transform(y), columns=['Sentiment'])

    if is_none_free(y_values):
        y = y_values
        del y_values
    else:
        print('error: There are still nan values')

    # dealing with Y labels:
    y = pd.get_dummies(y)
    y.columns = ['Negative', 'Neutral', 'Positive']

    return x, y

