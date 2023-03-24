## PyBank Instructions
# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period
# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in profits (date and amount) over the entire period
# Your analysis should look similar to the following:
#   ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $22564198
#  Average Change: $-8311.11
#  Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)
#  ```
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# -------------------------------------------------------------------------------------------------------------------


# First we'll import the os module
# allows us to create file paths across operating systems & reading CSV files
import os
import csv

# declaring/reseting a # of months counter & profit/loss summistion counter & diffrence
MonthsCount = []
ProfitLossCount = []
ProfitlossDifference = []
Current_PrLs = []
Last_PrLs = []
Total_Change = 0
AverageChange = []
GreatestIncrease = 0
GreatestDecrease = 0

file = "Resources/Budget_Data.csv"

# identifying CSV file directory path
csvpath = os.path.join("Resources", "budget_data.csv")

# count & compare each line month to line before & after
with open(file, "r", encoding="utf-8") as csvhandler:
    csvreader = csv.reader(csvhandler, delimiter=',')
    csvhandler = next(csvreader)

    for row in csvreader:
        MonthsCount.append(row[0])                                      # Counting & appending number of months:
        ProfitLossCount.append(int(row[1])) 

        Total_Months = len(MonthsCount)                                 # Total Months # of rows:
        Total_ProfitLoss = sum(ProfitLossCount)                         # Total Profit & Loss column:

    for i in range(1, len(ProfitLossCount)):
        ProfitlossDifference.append(ProfitLossCount[i]-ProfitLossCount[i-1])

AverageChange = round(sum(ProfitlossDifference)/len(ProfitlossDifference),2)

# GreatestIncrease = max(ProfitlossDifferenc)
#  Greatest Profit & Loss Increase / decrease:
GreatestIncrease = max(ProfitlossDifference)
GreatestDecrease = min(ProfitlossDifference)

max_months = (MonthsCount[ProfitlossDifference.index(GreatestIncrease)+1])
min_months = (MonthsCount[ProfitlossDifference.index(GreatestDecrease)+1])

print(f"Total Months: {Total_Months}")
print(f"Total Profit or loss: $ {Total_ProfitLoss}")
print(f"Average Change: {AverageChange}")
print(f"Greatest Increase in Profits: {GreatestIncrease}")
print(f"Greatest Decrease in Profits: {GreatestDecrease}")
print({max_months})
print({min_months})

Analysis = (f"Financial Analysis" 
            "\n----------------------" 
            f"\nTotal Months: {Total_Months}" 
            f"\nAverage Change: $ {AverageChange}" 
            f"\nGreatest Increase in Profits: {max_months} $ ({GreatestIncrease})"
            f"\nGreatest Increase in Profits: {min_months} $ ({GreatestDecrease})"
            )
print(Analysis)


# print output to TXT file
txt_file_path = "analysis/analysis.txt"

with open(txt_file_path, 'w') as f:

    f.write(Analysis)
