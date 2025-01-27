import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r"C:\Users\willr\Downloads\Cleaned_Klima_DAO_Transactions_Data.csv"
data = pd.read_csv(file_path)

# Parse dates
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Group transactions by day
daily_activity = data.groupby(data['Date'].dt.date).size()

# Plot the transaction activity
plt.figure(figsize=(12, 6))
plt.bar(daily_activity.index, daily_activity.values, color='skyblue')
plt.title("Transaction Activity Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Transactions", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
