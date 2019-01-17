import csv
import os
import re

import requests

from moviestats import MovieStats

OMDB_API_URL = 'https://www.omdbapi.com'
pattern = re.compile('([^\s\w]|_)+')

ms = MovieStats()

with open('watched.csv') as f:
    mreader = csv.DictReader(f)

    for row in mreader:
        # strip characters other than alpha-numeric
        # for some movies this has a better chance of a direct hit
        name = pattern.sub('', row['Name'])
        year = row['Year']

        payload = {
            't': name,
            'y': year,
            'apikey': os.getenv('OMDB_API_KEY', '')
        }

        r = requests.get(OMDB_API_URL, params=payload)

        # get json object from response object
        # this is then passed to a movie stats object
        movie_json = r.json()

        # add movie to movie stats object which will process
        # it internally
        ms.add_movie(movie_json)

ms.print_stats()

