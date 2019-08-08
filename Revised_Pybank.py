import csv
import os

os.chdir(os.path.dirname(__file__))
#files to be loaded
csvpath = os.path.join("Resources", "budget_data.csv")

#output file to be produced

pathout = os.path.join("Resources", "budget_analysis.txt")

#total month needs to be set to 0 in order to perform the count function
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease =["", 99999999999]

#Read the budget_data.csv file 
with open(csvpath) as revenueData:
    reader = csv.DictReader(revenueData)

#Loop through the data to collect the answers
    for col in reader:
    
#Totaling 
        totalMonth = totalMonth + 1
        totalRevenue = totalRevenue + int(col["Profit/Losses"])

#changes of revenue calculations
        revenue_change = int(col["Profit/Losses"]) - previousRevenue
        revenue_change_list.append(revenue_change)
        previousRevenue = int(col["Profit/Losses"])
        month_of_change = month_of_change + [col["Date"]]

#Greatest Increase value
if (revenue_change > greatestIncrease[1]):
    greatestIncrease[1] = revenue_change
    greatestIncrease[0] = col["Date"]

#average revenue
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

#print the outcomes
output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
)

print(output)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)
    