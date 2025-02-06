import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r"C:\Users\willr\Downloads\Cleaned_Klima_DAO_Transactions_Data.csv"
data = pd.read_csv(file_path)

# Ensure 'Token Amount' is numeric
data['Token Amount'] = pd.to_numeric(data['Token Amount'], errors='coerce')
data = data[data['Token Amount'] > 0]  # Keep only positive values

# Define transaction size bins and labels
bins = [0, 5, 20, 100, data['Token Amount'].max() + 1]  # Adjust bins
labels = ["<$5", "$5-$20", "$20-$100", ">$100"]

# Categorize transaction sizes into bins
data['Size Category'] = pd.cut(data['Token Amount'], bins=bins, labels=labels, right=False)

# Calculate the distribution of transaction sizes
size_distribution = data['Size Category'].value_counts(sort=False)

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(size_distribution, labels=size_distribution.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Transaction Size Distribution", fontsize=16)
plt.tight_layout()
plt.show()
