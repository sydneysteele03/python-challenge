import os, csv, math 
#pull csv file for analysis, path to collect data 
budget_csv = os.path.join("/Users/sydneysteele/Documents/python-challenge/PyBank/Resources/budget_data.csv")
total = 0 
total_months = 0 
previous_mo = 0 
poschanges = []
pos_months = []
neg_months = []
negchanges = []


# read in the csv file 
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total = total + int(row[1])
        total_months = total_months + 1

        #greatest increases 
        if (int(row[1])-previous_mo) > 0: 
            poschanges.append(int(row[1])-previous_mo)
            pos_months.append(row[0])
            previous_mo = int(row[1])
            
            
        #greatest decreases 
        if (int(row[1])-previous_mo) < 0:
            negchanges.append(int(row[1])-previous_mo)
            neg_months.append(row[0])
            previous_mo = int(row[1])       
    
    #remove first month's value to accurately calculate the monthly average change 
    average = (sum(poschanges[1:len(poschanges)]) + sum(negchanges))/(len(poschanges)+len(negchanges)-1)

# display results 
print(f'Financial Analysis')
print(f'------------------------------')
print(f'Total Months:'+ str(total_months))
print(f'Total: $'+str(total))
print(f'Average Change: $'+str("{:.2f}".format(average)))
print(f'Greatest Increase in Profits: ' + pos_months[poschanges.index(max(poschanges))] +' ($' + str(max(poschanges))+')')
print(f'Greatest Decrease in Profits: ' + neg_months[negchanges.index(min(negchanges))] +' ($' + str(min(negchanges))+')')


