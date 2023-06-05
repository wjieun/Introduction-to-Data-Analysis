import pandas as pd

df = pd.read_csv('data/winequality-red.csv',dtype=float)
def encoding_quality(x):
	if x >= 3 and x <= 5: return 0
	elif x >= 6 and x <= 8: return 1

df['quality'] = df['quality'].apply(encoding_quality)
print(len(df.loc[df['quality'] == 0]))
print(len(df.loc[df['quality'] == 1]))