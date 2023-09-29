import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
import pandas as pd
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 12, 5, 8, 6]})

# Scatter plot with regression line
sns.regplot(x='x', y='y', data=data)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Regression Line')
plt.show()

