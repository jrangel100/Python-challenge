import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# What information is needed for Analysis
## The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

with open(budget_data_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #create empty lists to add the csv values to 
    month_count = []
    profit = []
    change_profit = []
    
                      
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#using the index, 
Greatest_increase = change_profit.index(max(change_profit))+1
Greatest_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[Greatest_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[Greatest_decrease]} (${(str(decrease))})")      

#output to txt file
output = os.path.join(".", 'Analysis.txt')
with open(output,"w") as Analysis:
    Analysis.write("Financial Analysis")
    Analysis.write("\n")
    Analysis.write("------------------------")
    Analysis.write("\n")
    Analysis.write(f"Total Months:{len(month_count)}")
    Analysis.write("\n")
    Analysis.write(f"Total: ${sum(profit)}")
    Analysis.write("\n")
    Analysis.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    Analysis.write("\n")
    Analysis.write(f"Greatest Increase in Profits: {month_count[Greatest_increase]} (${(str(increase))})")
    Analysis.write("\n")
    Analysis.write(f"Greatest Decrease in Profits: {month_count[Greatest_decrease]} (${(str(decrease))})")