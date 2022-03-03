import array

import pandas as pd

df = pd.read_csv('rå/athlete_events.csv')
listetest = ['b', [1, 2, 3, 4, 5]]

sortert=df.stort_values("NOC")
for i in listetest:
    print(df.to_string())

for i in listetest:
    print(sortert.to_string())
