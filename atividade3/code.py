import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats.stats import pearsonr

all_data = pd.read_csv("data/eleicoes_2006_a_2010.csv")

train = all_data[all_data["ano"] == 2006]
test = all_data[all_data["ano"] == 2010]

found = 0
for index, row in train[train['total_receita'].isnull()].iterrows():
    for index_test, row_test in test[test['nome'] == row['nome']].iterrows():
        if row_test['nome'] == row['nome'] and row_test['uf'] == row['uf']:
            all_data.loc[index, 'total_receita'] = row_test['total_receita']
            all_data.loc[index, 'media_receita'] = row_test['media_receita']

print(found)
