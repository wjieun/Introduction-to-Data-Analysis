import warnings
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

warnings.filterwarnings('ignore')

df = pd.read_csv('22_fall_final_train.csv')

df = df.drop(['new_snowfall_3hr', 'cloud_type', 'lowest_cloud', 'ground_condition', 'wind_direction'], axis=1)
df = df.fillna(0)

df_train = df[150:]
df_test = df[:150]

###############################################