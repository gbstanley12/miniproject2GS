# INF601 - Advanced Programming in Python
# Gavin Stanley
# Mini Project 2

import pandas as pd

data = pd.read_csv('artists.csv', index_col='Artist')

print(data['Streams'].describe())
