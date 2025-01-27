import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r"C:\Users\willr\Downloads\Cleaned_Klima_DAO_Transactions_Data.csv"
data = pd.read_csv(file_path)

# Parse dates and ensure 'Token Amount' is numeric
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data['Token Amount'] = pd.to_numeric(data['Token Amount'], errors='coerce')
data = data.dropna(subset=['Date', 'Token Amount'])

# Define transaction size categories
def categorize_transaction(amount):
    if amount < 5:
        return 'Micro (under $5)'
    elif 5 <= amount < 20:
        return 'Small ($5-$20)'
    elif 20 <= amount < 100:
        return 'Medium ($20-$100)'
    else:
        return 'Large (over $100)'

# Apply the categorization
data['Size Category'] = data['Token Amount'].apply(categorize_transaction)

# Exclude the last week if incomplete
last_full_week = data['Date'].dt.to_period('W').max() - 1
data = data[data['Date'].dt.to_period('W') <= last_full_week]

# Group by week and transaction size
weekly_data = data.groupby([data['Date'].dt.to_period('W'), 'Size Category'])['Token Amount'].count().unstack(fill_value=0)

# Plot transaction size distribution over time (weekly) as line chart
plt.figure(figsize=(14, 7))
for category in weekly_data.columns:
    plt.plot(weekly_data.index.astype(str), weekly_data[category], label=category, marker='o')

plt.title("Transaction Size Distribution Over Time (Weekly)", fontsize=16)
plt.xlabel("Week", fontsize=12)
plt.ylabel("Number of Transactions", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend(title="Transaction Size", fontsize=10)
plt.tight_layout()
plt.show()
