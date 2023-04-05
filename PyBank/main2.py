import os, csv, math 
#pull csv file for analysis, path to collect data 
budget_csv = os.path.join("/Users/sydneysteele/Documents/python-challenge/PyBank/Resources/budget_data.csv")
total = 0 
total_months = 0 
previous_mo = 0 
previous_neg = 0
PosChanges = {}
poschanges = []
negchanges = []
positive_mos = []
greatest_inc = 0 
prevloss = 0
prevgain = 0
greatest_dec = 0 
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
            #positive_mos.append(row[0])
            previous_mo = int(row[1])
            
           
        #greatest decreases 
        if (int(row[1])-previous_mo) < 0:
            negchanges.append(int(row[1])-previous_mo)
            previous_mo = int(row[1])       

    average = (sum(poschanges) + sum(negchanges))/(len(poschanges)+len(negchanges))

#print(negchanges)
# display results 
print(f'------------------------------')
print(f'Financial Analysis')
print(f'------------------------------')
print(f'Total Months:'+ str(total_months))
print(f'Total: $'+str(total))
print(f'Average Change: $'+ str(average))
#print(f'Average Change: $'+str("{:.2f}".format(average)))
print(f'Greatest Increase in Profits: ' + ' $' + str(max(poschanges)))
print(f'Greatest Decrease in Profits: ' + ' $' + str(min(negchanges)))



