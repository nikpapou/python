import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['John', 'Maria', 'Steve', 'Sophia', 'Mike', 'Emma', 'Jake', 'Clara'],
    'Score': [30, 28, 35, 31, 27, 33, 29, 30],
    'Age': [15, 16, 15, 16, 17, 16, 15, 17],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)
sns.lmplot(x='Score', y='Age', data=df, hue='Gender', scatter=True, legend=False)

plt.legend(title='Gender', loc='upper left')
plt.title('Score vs Age')
plt.xlabel('Score')
plt.ylabel('Age')
plt.show()