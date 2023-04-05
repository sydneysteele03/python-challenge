# python-challenge (PyBank on line 2, PyPoll on line 50)
## PYBANK CHALLENGE 
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


## --------------------------------------------------------------------------------------------------------------------------
## PYPOLL CHALLENGE 

import csv, os, math

election_csv = os.path.join("/Users/sydneysteele/Documents/python-challenge/PyPoll/Resources/election_data.csv")
#initialize variables 
total_votes = 0
candidate1 = 'Charles Casper Stockham'
candidate2 = 'Diana DeGette'
candidate3 = 'Raymon Anthony Doane'
c1_total = 0
c2_total = 0
c3_total = 0 

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #count votes for each candidate 
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] == candidate1: 
            c1_total = c1_total + 1
        if row[2] == candidate2:
            c2_total = c2_total + 1
        if row[2] == candidate3:
            c3_total = c3_total + 1 

#calculate percentage of votes for each candidate 
percent1 = "{:.3f}".format((c1_total/total_votes)*100)
percent2 = "{:.3f}".format((c2_total/total_votes)*100)
percent3 = "{:.3f}".format((c3_total/total_votes)*100)

#compare votes and determine winner 
if c1_total > c2_total and c3_total:
    winner = candidate1
elif c2_total > c1_total and c3_total:
    winner = candidate2
elif c3_total > c1_total and c2_total:
    winner = candidate3
    
#display results 
print(f'----------------------------')
print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes: '+str(total_votes))
print(f'----------------------------')
print(candidate1+': '+str(percent1)+'% ('+str(c1_total)+')')
print(candidate2+': '+str(percent2)+'% ('+str(c2_total)+')')
print(candidate3+': '+str(percent3)+'% ('+str(c3_total)+')')
print(f'----------------------------')
print(f'Winner: '+ winner)
print(f'----------------------------')