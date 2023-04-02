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