# this script searches by entered keyword and scrapes a maximum of 10_000 tweets between Sept 1, 2021 and Oct 31, 2021 (end is non-inclusive) within 160km of Napa, CA coordinates
# then saves it as a csv file named after the keyword
# idea from https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25

import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

keyw = input('enter a keyword to search by: ')
filepath = './' + keyw + '.csv'

# Napa Valley, 160km radius
loc = '38.502500, -122.265400, 160km'

df_coord = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(keyw + ' geocode:"{}", since:2020-09-01 until:2020-11-01'.format(loc)).get_items(), 10000))[['user', 'date','content']]

df_coord['user_location'] =  df_coord['user'].apply(lambda x: x['location'])

df_coord.to_csv(filepath)
