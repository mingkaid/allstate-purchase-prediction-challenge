import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)

data = pd.read_csv('test_v2.csv')
id_grouped = data.groupby('customer_ID')
id_max_idx = id_grouped.shopping_pt.idxmax()
data_max_shopping_pt = data.iloc[id_max_idx]

df_list = []
for index, row in data_max_shopping_pt.iterrows():
    df_row = {}
    df_row['customer_ID'] = `int(row.customer_ID)`
    plan = ''.join([`int(row[char])` for char in char_range('A', 'G')])
    df_row['plan'] = plan
    #print df_row
    df_list.append(df_row)
    #print df_list
df = pd.DataFrame(df_list)

df.to_csv('prediction.csv', index=False)

winsound.Beep(500, 1000)