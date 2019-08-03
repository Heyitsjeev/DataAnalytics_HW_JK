import os
import csv
import numpy as p


csvBudget = os.path.join("Resources", "budget_data.csv")

months = []
secondCOl = []
totalMonths = 0
netTotal = 0.00
averageChange = []
diff = 0.0
totaldiff = 0

def average(numbers):
    length = len(numbers)
    totalAverage = 0.0
    for i in numbers:
        totalAverage = i + totalAverage

    return totalAverage/length

with open(csvBudget, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        if row[0] != None:
            totalMonths = totalMonths +1
            months.append(row[0])
        
        if row[1] != None:
            netTotal = float(row[1]) + netTotal
            secondCOl.append(float(row[1]))

for i in range(len(secondCOl)-1):
    diff = secondCOl[i+1] - secondCOl[i]
    averageChange.append(float(diff))


changeAverage = average(averageChange)
            
greatestIncrease = max(averageChange)
greatestDecrease = min(averageChange)

greatestIncreaseMonth = averageChange.index(max(averageChange))+1
greatestDecreaseMonth = averageChange.index(min(averageChange))+1

print("Financial Analysis")
print("----------------------------------------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${changeAverage}")
print(f"Greatest Increase in Profits: {months[greatestIncreaseMonth]} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {months[greatestDecreaseMonth]} (${greatestDecrease})")
print("--------------------------------------------------------------------")

file = open("output.txt", "w")
file.write("Financial Analysis\n")
file.write("--------------------------------------------------------------------\n")
file.write(f"Total Months: {totalMonths}\n")
file.write(f"Total: ${netTotal}\n")
file.write(f"Average Change: ${changeAverage}\n")
file.write(f"Greatest Increase in Profits:  {months[greatestIncreaseMonth]} (${greatestIncrease})\n")
file.write(f"Greatest Decrease in Profits: {months[greatestDecreaseMonth]} (${greatestDecrease})\n")
file.write("--------------------------------------------------------------------\n")
file.close

