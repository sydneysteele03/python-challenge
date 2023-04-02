import os, csv, math 
#pull csv file for analysis, path to collect data 
budget_csv = os.path.join("/Users/sydneysteele/Documents/python-challenge/PyBank/Resources/budget_data.csv")
total = 0 
total_months = 0 
greatest_inc = 0 
greatest_dec = 0 

# read in the csv file 
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total = total + int(row[1])
        total_months = total_months + 1
        
        #find greatest increase in profits 
        if int(row[1]) > int(greatest_inc):
            greatest_inc = row[1]
            inc_mo = row[0]
        
        #find greatest decrease in profits 
        if int(row[1]) < int(greatest_dec):
            greatest_dec = row[1]
            dec_mo = row[0]
        
    #calculate average change... need help on this! 
    average = total/total_months

# display results 
print(f'------------------------------')
print(f'Financial Analysis')
print(f'------------------------------')
print(f'Total Months:'+ str(total_months))
print(f'Total: $'+str(total))
print(f'Average Change: $'+str("{:.2f}".format(average)))
print(f'Greatest Increase in Profits: '+inc_mo+' '+str(greatest_inc))
print(f'Greatest Decrease in Profits: '+dec_mo+' '+str(greatest_dec))



