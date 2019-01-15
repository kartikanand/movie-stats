import csv
import requests

with open('watched.csv') as f:
    mreader = csv.DictReader(f)

    for row in mreader:
        name = row['Name']
        year = row['Year']
        break

