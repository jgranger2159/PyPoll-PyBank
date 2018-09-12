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
max_increase = 0
max_decrease = 0

# Open csv
with open(file1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter="\t")
    for row in csvreader:
        
        # Count months
        count = count + 1
        
        # Calculate net profit
        net_profit = net_profit + int(row[1])

        # Calculate average change
        current_row = int(row[1])
        monthly_change = current_row - last_row
        monthly_changes.append(monthly_change)
        last_row = current_row

        # Check for greatest/least change
        if monthly_change > max_increase:
            max_increase = monthly_change
            increase_date = str(row[0])
        elif monthly_change < max_decrease:
            max_decrease = monthly_change
            decrease_date = str(row[0])


# Print results
print("FINANCIAL ANALYSIS")
print("-"*20)
print("Total Months: " + str(count))
print("Net Profit: " + str(net_profit))
average_change = sum(monthly_changes)/len(monthly_changes)
print("Average Change: " + str(average_change))
print("Greatest Increase in Profits: " + str(increase_date) + " " + str(max_increase))
print("Greatest Decrease in Profits: " + str(decrease_date) + " " + str(max_decrease))

# Export results to Financial_Analysis.txt
f = open("Financial_Analysis.txt", "x")
f.write("FINANCIAL ANALYSIS")
f.write("-"*20)
f.write("Total Months: " + str(count))
f.write("Net Profit: " + str(net_profit))
f.write("Average Change: " + str(average_change))
f.write("Greatest Increase in Profits: " + str(increase_date) + " " + str(max_increase))
f.write("Greatest Decrease in Profits: " + str(decrease_date) + " " + str(max_decrease))