#Get NFL Team Stats

import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "http://www.espn.com/nfl/statistics/team/_/stat/total"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

stats_table = soup.find('table', class_='tablehead')

list_of_rows = []
for row in stats_table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)


for item in list_of_rows:
    #print(' '.join(item))
    print(item)

with open('nfl_stats.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(list_of_rows)