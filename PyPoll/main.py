#What is needed for Analysis
## The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

# Identifies file with poll data
file = os.path.join('../Resources/election_data.csv')

#Creates dictionary to be used for candidate name and vote count.
poll = {}
total_votes = 0

#gets data file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #skips header line
    next(csvread, None)

    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
    #create empty list for candidates and his/her vote count
candidates = []
num_votes = []

# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 3))

# zips candidates, num_votes, vote_percent into tuples
zip_data = list(zip(candidates, num_votes, vote_percent))

#create winner_list to put winners 
winner_list = []

for name in zip_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join('Analysis.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in zip_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())

