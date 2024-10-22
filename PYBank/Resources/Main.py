import pandas as pd

data = pd.read_csv(r'C:\Users\eddie\OneDrive\Desktop\Class_Requirements\UofM-VIRT-DATA-PT-09-2024-U-LOLC\03-Python\Homework\Starter_Code\PyBank\Resources\budget_data.csv')

total_months = len(data['Date'])

net_total = data['Profit/Losses'].sum()

data['Change'] = data['Profit/Losses'].diff()

average_change = data['Change'].mean()

greatest_increase = data.loc[data['Change'].idxmax()]

greatest_decrease = data.loc[data['Change'].idxmin()]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})")