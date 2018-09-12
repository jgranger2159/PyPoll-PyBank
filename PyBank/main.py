# Dependencies
import csv
import os

# Set path
file1 = os.path.join("budget_data.csv")

# Set variables
count = 0
net_profit = 0
monthly_changes = []
average_change = 0
last_row = 0

# Open csv
with open(file1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        
        # Count months
        count = count + 1
        
        # Calculate net profit
        net_profit = net_profit + row[1]

        # Calculate average change
        current_row = row[1]
        monthly_change = current_row - last_row
        monthly_changes.append(monthly_change)
        last_row = current_row

# Print results
print("Total Months: " + str(count))
print("Net Profit: " + str(net_profit))
average_change = sum(monthly_changes)/len(monthly_changes)
print("Average Change: " + average_change)