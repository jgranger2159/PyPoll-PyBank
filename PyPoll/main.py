# Dependencies
import os
import csv

# Set file path
file1 = os.path.join("election_data.csv")

# Declare variables
count = 0
candidates = []
vote_count = 0

# Open csv
with open(file1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Loop through
    for row in csvreader:
        
        # Count votes
        count = count + 1

        # Generate list of candidates
        candidate = row[2]
        if candidate not in candidates:
            candidates.append([candidate])
        
# Print stuff
print("Election Results")
print("-"*20)
print("Total Votes: " + count)

# Count votes/% for each candidate
with open(file1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for x in range(len(candidates)):
        name = candidates[x]
        for row in csvreader:
            if name = row[2]:
                vote_count = vote_count + row[1]
        percent = vote_count / count * 100
        print(x + " " + vote_count + " %" + percent)
