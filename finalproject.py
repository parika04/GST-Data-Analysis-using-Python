import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the data
data = pd.read_excel('finaldata.xlsx')

print("\nEXPLORATORY DATA ANALYSIS-----------------------------------------------------")
# Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Check the shape of the dataset
print("\nDataset dimensions (rows, columns):", data.shape)

# Check column names and data types
print("\nColumn information:")
print(data.info())

# Check for missing values
print("\nMissing values per column:")
print(data.isnull().sum())

# Basic statistical summary
print("\nStatistical summary:")
print(data.describe())

print("Column Names:\n", data.columns, "\n")
data = data.fillna(0)

data['Total_Registered'] = data['GST ( Goods and Service Tax ) Payers registered before due date'] + data['GST ( Goods and Service Tax ) Payers registered after due date']


#Objective 1-----------------------------------------------------------
plt.figure(figsize=(10, 6))
state_eligible = data.groupby('srcStateName')['Payer eligible for GST ( Goods and Service Tax ) registration'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=state_eligible.values, y=state_eligible.index, hue=state_eligible.index, palette='pastel', legend=False)
plt.title("Top 10 States/UTs by Eligible GST Payers")
plt.xlabel("Number of Eligible Payers")
plt.ylabel("State/UT")
plt.show()
print("\nSummary: The top states/UTs, like Maharashtra and Uttar Pradesh, have the highest number of eligible GST payers, showing strong regional variation. Jammu and Kashmir's data indicates moderate eligibility compared to larger states.")


#Objective 2------------------------------------------------------------
plt.figure(figsize=(10, 6))
time_trends = data.groupby('srcMonth').agg({
    'Payer eligible for GST ( Goods and Service Tax ) registration': 'sum',
    'Total_Registered': 'sum'
})
time_trends.plot(kind='line', marker='o')
plt.title("GST Payers Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Payers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("\nSummary: GST payer eligibility and registrations fluctuate over time, with peaks in certain months, suggesting seasonal or policy-driven trends.")


#Objective 3-------------------------------------------------------------
plt.figure(figsize=(8, 6))
return_counts = data.groupby('GST ( Goods and Service Tax ) Return Type')['Total_Registered'].sum()
sns.barplot(x=return_counts.index, y=return_counts.values, hue=return_counts.index, palette='coolwarm', legend=False)
plt.title("Total Registered GST Payers by Return Type")
plt.xlabel("Return Type")
plt.ylabel("Total Registered Payers")
plt.show()

print("\nHigh-Value Payers by Return Type:")
return_summary = data.groupby('GST ( Goods and Service Tax ) Return Type').agg({
    'Payer eligible for GST ( Goods and Service Tax ) registration': 'sum',
    'Total_Registered': 'sum'
})
print(return_summary)
print("\nSummary: GSTR-3 return type has more registered payers (501M) than GSTR-1 (344M), indicating GSTR-3 filers contribute significantly to GST registrations.")

#Objective 4-------------------------------------------------------------
numeric_cols = ['Payer eligible for GST ( Goods and Service Tax ) registration', 
                'GST ( Goods and Service Tax ) Payers registered before due date', 
                'GST ( Goods and Service Tax ) Payers registered after due date', 
                'Total_Registered']
print("\nCorrelation Matrix:\n", data[numeric_cols].corr())

plt.figure(figsize=(8, 6))
sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap of GST Metrics")
plt.tight_layout()
plt.show()
print("\nSummary: Eligible payers and total registered payers are highly correlated (0.99), suggesting that higher eligibility strongly predicts more registrations.")

#Objective 5-------------------------------------------------------------
plt.figure(figsize=(8, 6))
reg_data = pd.melt(data, 
                   id_vars=['srcStateName'], 
                   value_vars=['GST ( Goods and Service Tax ) Payers registered before due date', 
                               'GST ( Goods and Service Tax ) Payers registered after due date'],
                   var_name='Registration_Type', 
                   value_name='Count')
sns.barplot(x='Registration_Type', y='Count', hue='Registration_Type', data=reg_data, palette='muted')
plt.title("Before vs After Due Date GST Registrations")
plt.xlabel("Registration Type")
plt.ylabel("Number of Payers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("\nSummary (Before vs After Due Date Registrations): Before-due-date registrations significantly outnumber after-due-date registrations, indicating timely compliance among most GST payers.")
