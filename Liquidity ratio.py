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
        return 'Micro'
    elif 5 <= amount < 20:
        return 'Small'
    elif 20 <= amount < 100:
        return 'Medium'
    else:
        return 'Large'

# Apply the categorization
data['Size Category'] = data['Token Amount'].apply(categorize_transaction)

# Exclude the last week if incomplete
last_full_week = data['Date'].dt.to_period('W').max() - 1
data = data[data['Date'].dt.to_period('W') <= last_full_week]

# Group by week and transaction size
weekly_data = data.groupby([data['Date'].dt.to_period('W'), 'Size Category'])['Token Amount'].count().unstack(fill_value=0)

# Calculate liquidity ratio: (Micro + Small) / (Medium + Large)
weekly_data['Liquidity Ratio'] = (weekly_data['Micro'] + weekly_data['Small']) / (weekly_data['Medium'] + weekly_data['Large'])

# Plot liquidity ratio over time
plt.figure(figsize=(14, 7))
plt.plot(weekly_data.index.astype(str), weekly_data['Liquidity Ratio'], marker='o', color='blue', label='Liquidity Ratio')
plt.title("Liquidity Ratio Over Time (Weekly)", fontsize=16)
plt.xlabel("Week", fontsize=12)
plt.ylabel("Liquidity Ratio", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
