import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

### Analyzing Ad Sources ###
print(ad_clicks.head())

# Count of website views per click source
utm_source_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_source_views)

# New boolean column for clicks
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

# Clicks per source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()
# print(clicks_pivot)

clicks_pivot['percent_clicked'] = round(
  clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]), 3
  )
print(clicks_pivot)


### Analyzing an A/B Test ###
experimental_group_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(experimental_group_count)

# More people clicked on Ad A
experimental_group_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
experimental_group_clicks = experimental_group_clicks.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id'
).reset_index()
print(experimental_group_clicks)

# A/B per day of week
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index(drop=True)
print(a_clicks)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index(drop=True)
print(b_clicks)

# Calculating A-group click percentage
a_clicks = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(a_clicks)

a_clicks_pivot = a_clicks.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

a_clicks_pivot['click_percentage'] = round(
  a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False]), 3
)
a_clicks_pivot = a_clicks_pivot.rename(columns={
  'day': 'day',
  False: 'Not a click',
  True: 'Is click',
  'click_percentage': 'Click percentage'
})
print(a_clicks_pivot)

# Calculating B-group click percentage
b_clicks = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
print(b_clicks)

b_clicks_pivot = b_clicks.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

b_clicks_pivot['click_percentage'] = round(
  b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False]), 3
)
b_clicks_pivot = b_clicks_pivot.rename(columns={
  'day': 'day',
  False: 'Not a click',
  True: 'Is click',
  'click_percentage': 'Click percentage'
})
print(b_clicks_pivot)

# Based on results of the above, I would recommend that Marketing proceed with Ad A.


