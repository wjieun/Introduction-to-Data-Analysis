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
columns = ['activity_score', 'station_name', 'date_time']
df['activity_score_bin'] = df['activity_score'] > 0
print(df.corr()['activity_score_bin'])

train_X = df_train.drop(columns, axis=1)
train_Y = df_train['activity_score'] > 0

test_X = df_test.drop(columns, axis=1)
test_Y = df_test['activity_score'] > 0

lr = LogisticRegression()
lr.fit(train_X, train_Y)

###############################################

def calculate_score(train_score, test_score):
    print(f"Train Score: {train_score:.4f}, Test Score: {test_score:.4f}  -  ", end="")

calculate_score(
    lr.score(train_X, train_Y),
    lr.score(test_X, test_Y)
)

cheat_lr = LogisticRegression().fit(
    np.concatenate((train_X, test_X), axis=0),
    np.concatenate((train_Y, test_Y), axis=0)
)

if (lr.coef_ == cheat_lr.coef_).all():
    print('.', end="")