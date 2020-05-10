from exploring_data_structure import apps_table

# Finding most STABLE category:
aggregated_category = apps_table[['App', 'Category', 'Rating']].drop_duplicates()
aggregated_category = aggregated_category.groupby('Category').agg(
    {'Rating': ['mean', 'std', 'median', lambda x: x.value_counts().index[0]]})
aggregated_category.rename(columns={'<lambda_0>': 'mode'}, inplace=True)
tempSort = aggregated_category.sort_values(by=[('Rating', 'std')])
print("""
This data set maps for each category its analysis, and is ordered from the most stable app (top)
to the least stable one (bottom)

{}""".format(tempSort))

print("""
The most stable category is {}
it has the smallest std value {}
and you can see the average {} the median {} and mode {} which are almost identical
""".format(tempSort.index[0], tempSort[('Rating', 'std')].head(1).tolist(),
           tempSort[('Rating', 'mean')].head(1).tolist(),
           tempSort[('Rating', 'median')].head(1).tolist(), tempSort[('Rating', 'mode')].head(1).tolist()))

# Finding Categories for them the data distributes normally:
# the difference between mode-median-mean should be less then 0.5 in order to consider it a Normal Dist.
tempSort.columns = tempSort.columns.droplevel(0)
tempSort['median-mean'] = tempSort.apply(lambda x: x['median'] - x['mean'], axis=1)
tempSort['median-mode'] = tempSort.apply(lambda x: x['median'] - x['mode'], axis=1)
tempSort['mode-mean'] = tempSort.apply(lambda x: x['mode'] - x['mean'], axis=1)
tempSort = tempSort.drop(tempSort.columns[[0, 1, 2, 3]], axis=1).abs()
tempSort['median-mode'] = tempSort['median-mode'].apply(lambda x: 'True' if x <= 0.5 else 'False')
tempSort['median-mean'] = tempSort['median-mean'].apply(lambda x: 'True' if x <= 0.5 else 'False')
tempSort['mode-mean'] = tempSort['mode-mean'].apply(lambda x: 'True' if x <= 0.5 else 'False')
tempSort = tempSort[tempSort['median-mode'] == 'True']
print("""
This are the Categories in which we have normality:
{}
""".format(tempSort.index))