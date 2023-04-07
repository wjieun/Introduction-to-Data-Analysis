import pandas as pd
import numpy as np

classes = ['국어', '영어', '수학']
df = pd.DataFrame(np.zeros((4, 3)), columns=classes)

print(type(df))
print(df)