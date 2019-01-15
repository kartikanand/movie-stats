import csv
import os
import re

import requests

OMDB_API_URL = 'https://www.omdbapi.com'
pattern = re.compile('([^\s\w]|_)+')

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


