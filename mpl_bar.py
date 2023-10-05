from matplotlib import pyplot as plt
import numpy as np 
from collections import Counter
import csv
import pandas as pd
# print(plt.style.available)
plt.style.use('fivethirtyeight')
# plt.xkcd()
language_counter = Counter()

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data.csv')
ids = data['Responder_id']
languages_responses = data['LanguagesWorkedWith']


for response in languages_responses:
    language_counter.update(response.split(';'))

# print(language_counter.most_common(15))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages , popularity)




# plt.xlabel("Programming Languages")
plt.title('Most Popular Languages')
plt.xlabel("Popularity (number of users)")
# plt.grid(True)
plt.tight_layout()
plt.show()