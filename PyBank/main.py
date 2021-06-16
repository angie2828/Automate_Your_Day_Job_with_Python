import os
import csv
from pathlib import Path
budgetpath = Path("budget_data.csv")
total_months = 0
total_profits = 0
average_change = 0
max_change = -999999999
max_change_month = ""
min_change = 999999999
min_change_month = ""
prev_profit = 0
total_change = 0
change = 0
with open(budgetpath,"r") as budgetfile:

    csv_reader = csv.reader(budgetfile)
#     print(csv_reader)
    header = next(csv_reader)
    print(header, "<<<<<<<HEADER")

    for row in csv_reader:
        total_months +=1
        row[1] = int(row[1])
        total_profits += row[1]
        if total_months != 1:
            change = row[1] - prev_profit
            total_change += change
        if max_change < change:
            max_change = change
            max_change_month = row[0]
            
        if  min_change > change:
            min_change = change
            min_change_month = row[0]
            
        
        prev_profit = row[1]
# print(row)

print(f"""
Financial Analysis
----------------------------
    Total Months: {total_months}
    Total: ${total_profits:,.0f}
    Average Change: ${total_change/(total_months-1):,.2f}
    Greatest Increase in Profits: {max_change_month} (${max_change:,.0f})
    Greatest Decrease in Profits: {min_change_month} (${min_change:,.0f})
""")