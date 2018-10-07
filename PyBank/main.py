#Modules
import os
import csv

# Set path for file
budget_csv = os.path.join('budget_data.csv')

#Open and read csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvfile)

    totalNet = 0
    totalMonths = 0
    totalNetList = []
    changeValueList = []
    dateList = []
    currValue = 0
    priorValue = 0
    changeValue = 0
    totalChangeMonths = 0

    #Read through each row after header
    for row in csvreader:
        
        #Add '1' for each row
        totalMonths += 1

        #Calculates months for average change
        totalChangeMonths = totalMonths - 1
        
        #Set current profit/loss value
        currValue = float(row[1])
        
        #Appends current profit/loss value
        totalNetList.append(currValue)

        #Calculate change value from current and previous month
        changeValue = currValue - priorValue
        
        #Skips appending change of value from first month
        #Appends to list for change value and dates of change
        if totalMonths > 1:
            changeValueList.append(changeValue)
            dateList.append(row[0])

        #Sets value to be used in next loop
        priorValue = currValue

#Calculate outputs        
averageChange = "%.2f" % (sum(changeValueList)/totalChangeMonths)
totalNet = "%.f" % sum(totalNetList)
greatestIncrease = "%.f" % max(changeValueList)
greatestDecrease = "%.f" % min(changeValueList)

#Get the index value of the when greatest changes occur
greatestIncIndex = changeValueList.index(max(changeValueList))
greatestDecIndex = changeValueList.index(min(changeValueList))

#Get the month where greatest changes happen
greatestMonthIncrease = dateList[greatestIncIndex]
greatestMonthDecrease = dateList[greatestDecIndex]

#Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(totalNet)}")
print(f"Average Change: ${str(averageChange)}")
print(f"Greatest Increase in Profits: {greatestMonthIncrease} (${str(greatestIncrease)})")
print(f"Greatest Decrease in Profits: {greatestMonthDecrease} (${str(greatestDecrease)})")

#Create and write ouputs into a text file

output_txt = os.path.join('pybank_results.txt')
with open(output_txt, 'w') as writefile:
    writefile.write("Financial Analysis\n")
    writefile.write("----------------------------\n")
    writefile.write(f"Total Months: {str(totalMonths)}\n")
    writefile.write(f"Total: ${str(totalNet)}\n")
    writefile.write(f"Average Change: ${str(averageChange)}\n")
    writefile.write(f"Greatest Increase in Profits: {greatestMonthIncrease} (${str(greatestIncrease)})\n")
    writefile.write(f"Greatest Decrease in Profits: {greatestMonthDecrease} (${str(greatestDecrease)})\n")