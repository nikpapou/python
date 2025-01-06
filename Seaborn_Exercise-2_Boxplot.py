import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dictionary containing data
data = {
    "Category": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A"],
    "Values": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a boxplot using seaborn to visualize the distribution of scores by category
plt.figure(figsize=(12, 6))  # Set the figure size
sns.boxplot(x="Category", y="Values", data=df, palette="Set2")  # Create the boxplot
plt.title("Boxplot of Values by Category")  # Add a title to the plot
plt.show()  # Display the plot