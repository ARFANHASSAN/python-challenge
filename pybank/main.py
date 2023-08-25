#import the modules
import os
import csv
#path for the csv file
budget_data = os.path.join("budget_data.csv")
#creating an object
total_months = 0
total_profit_loss = 0
value = 0
changes = 0
dates = []
profits = []
#opening/reading csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #to reade the header row 
    csv_header = next(csvreader)
    #reading the first row
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    #applied loop to go through each of the row 
    for row in csvreader:
        #tracking the dates
        dates.append(row[0])
        #finding the changes and adding to the list of changes
        changes = int(row[1])-value
        profits.append(changes)
        value = int(row[1])
        #calculating the total months
        total_months += 1
        #net profit and loss over the entire period
        total_profit_loss = total_profit_loss + int(row[1])
        #finding the greatest increase in profit
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]
        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]
        #average change in profit over the time period
        avg_change = sum(profits)/len(profits)
        #to print out the information with  the print function
        print("Financial Analysis")
        print("---------------------")
        print(f"Total Months: {str(total_months)}")
        print(f"Total: ${str(total_profit_loss)}")
        print(f"Average Change: ${str(round(avg_change,2))}")
        print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
        print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
        #to export the .txt file of the result 
        output = open("output.txt", "w")
        line1 = "Financial Analysis"
        line2 = "---------------------"
        line3 = str(f"Total Months: {str(total_months)}")
        line4 = str(f"Total: ${str(total_profit_loss)}")
        line5 = str(f"Average Change: ${str(round(avg_change,2))}")
        line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
        line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
        output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))