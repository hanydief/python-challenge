## PyPoll Instructions

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# Your analysis should look similar to the following:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 369711
#   -------------------------
#   Charles Casper Stockham: 23.049% (85213)
#   Diana DeGette: 73.812% (272892)
#   Raymon Anthony Doane: 3.139% (11606)
#   -------------------------
#   Winner: Diana DeGette
#   -------------------------
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# -----------------------------------------------------------------------------------------------------------------

# First we'll import the os module
# allows us to create file paths across operating systems & reading CSV files
import os
import csv

# declaring/reseting a # of months counter & profit/loss summistion counter & diffrence
TotalVotes = 0
VotesCount = []
NumberOfCandidates = []
Candidates = {}
VotesPercentage = []


# identifying CSV file directory path
csvpath = os.path.join('Resources', 'election_data.csv')

# count & compare each line month to line before & after
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    TotalVotes = len(VotesCount)
    #print(TotalVotes)

    for row in csvreader:
        TotalVotes += 1
        if row[2] not in Candidates:

            Candidates[row[2]] = 1   # 1st column is the name 2nd is the count
        else:
            Candidates[row[2]] += 1

max_key = max(Candidates, key=Candidates.get)       # identifying candidates with maximum votes

# Printing as per required
print(f"\nElection Results") 
print(f"----------------------------" ) 
print(f"Total Votes: {TotalVotes}")
print(f"----------------------------" )  

# for loop createing a dectionery with key "Candidate" & votes value & percentage in the middle of print to get the exact required format
for key, value in Candidates.items():
        VotesPercentage.append(round(((value/TotalVotes)*100), 3))
        output = f"{key} : {round(((value/TotalVotes)*100), 3)}% ({value})"

        print(output)

# continue Printing as per required 
print(f"----------------------------" ) 
print(f"Winner:  {max_key}\n")
print(f"----------------------------" ) 


#print output to TXT file
txt_file_path = "analysis/ElectionResults.txt"

with open(txt_file_path, 'w') as f:

    f.write(f"\nElection Results\n" 
            f"----------------------------\n" 
            f"Total Votes: {TotalVotes}\n"
            f"----------------------------\n" 
            f"{output}\n"
            f"----------------------------\n"  
            f"Winner:  {max_key}\n"
            f"----------------------------" )
#print(Candidates)
#print(TotalVotes)
#print(key,value)
#print(VotesCount)
#print(VotesPercentage)
#print(max_key)