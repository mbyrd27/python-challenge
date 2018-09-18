#import necessary modules
import os
import csv

#save path to csv file in a variable
raw_data = os.path.join("raw_data", "budget_data.csv")

#open the csv file and create a reader object
with open(raw_data, newline = '') as f:
    reader = csv.reader(f, delimiter = ',')
    #iterate the reader once to ignore the csv headers
    next(reader)
    #initialize counter for number of months and total profit/losses
    #create empty lists for further calculations
    months = 0
    total = 0
    prof_loss = []
    date = []
    #get total months and prof/losses. populate lists with csv data.
    for row in reader:
        months += 1
        total += int(row[1])
        prof_loss.append(int(row[1]))
        date.append(row[0])
#now that lists have been populated, iterate through them to make
#remaining calculations
change = []
for i in range(len(prof_loss)):
    if i > 0:
        change.append(prof_loss[i] - prof_loss[i-1])
#store these calculations in variables
av_change = round((sum(change)/len(change)), 2)
greatest_increase = round(max(change), 2)
greatest_decrease = round(min(change), 2)
date_max = (change.index(max(change))) + 1
date_min = (change.index(min(change))) + 1
total = round(total, 2)
#print final outputs to the console and write to .txt file
with open("FinancialAnalysis.txt", 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-------------------\n")
    textfile.write("Total Months: " + str(months) + "\n")
    textfile.write("Total: $" + str(total) + "\n")
    textfile.write("Average Change: $" + str(av_change) + "\n")
    textfile.write("Greatest Increase in Profits: " + str(date[date_max]) + " $" + str(greatest_increase) + "\n")
    textfile.write("Greatest Decrease in Profits: " + str(date[date_min]) + " $" + str(greatest_decrease) + "\n")
    textfile.close()
print("Financial Analysis\n"
      "----------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${av_change}")
print(f"Greatest Increase in Profits: {date[date_max]} ${greatest_increase} ")
print(f"Greatest Decrease in Profits: {date[date_min]} ${greatest_decrease} ")


