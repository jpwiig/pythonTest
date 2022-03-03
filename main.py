import array

import pandas as pd

df = pd.read_csv('rå/athlete_events.csv')
listetest = ['b', [1, 2, 3, 4, 5]]
for i in listetest:
    print(df.to_string())
