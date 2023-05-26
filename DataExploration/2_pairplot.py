import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

korean = [90, 95, 85, 80, 75, 80, 75, 70, 65, 65]
english = [95, 90, 85, 80, 85, 70, 70, 60, 65, 55]
math = [95, 85, 80, 70, 60, 70, 85, 50, 95, 45]

scores = pd.DataFrame({'korean': korean, 'english': english, 'math': math})
sns.pairplot(data=scores)
plt.show()