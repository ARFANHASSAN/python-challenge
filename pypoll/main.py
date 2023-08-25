#importing the modules
import os
import csv
#path for the data csv file
election_data = os.path.join("election_data.csv")
# defining the variable
candidates = []
# defining the variable for  the number of votes each candidate received
number_votes = []
# defining the variable for the percentage of total votes each candidate received
percents_votes = []
#  counter for the total number of votes 
total_votes = 0
#open the csv file and reading it
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #reading the header row
    csv_header = next(csvreader)
#looping through each of the row
    for row in csvreader:
        # Adding the total number of votes 
        total_votes += 1 

        '''
       # If the candidate is not on our list, add name to the list, along with 
       # a vote in candidate  name.
       # If candidate is already on the list, we will simply add a vote in candidate
       # name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    # just to add  percent_votes list 
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percents_votes.append(percentage)
    
    # to find out the  winner
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

# print function to print out the result
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percents_votes[i])} ({str(number_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# to export the .txt result file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percents_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
                                                               
                           
