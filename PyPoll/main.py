# import necessary modules
import os
import csv

# store path to raw data in a variable
election_data = os.path.join("raw_data", "election_data.csv")

# initialize a simple list of candidates
candidates = []

# iterate through the election data and populate the list of candidates
with open (election_data, newline='') as f:
    election_reader = csv.reader(f, delimiter=',')
    next(election_reader)
    for row in election_reader:
        candidates.append(row[2])
#For use to calculate percentages later
total_votes = len(candidates)
# Initialize vote count for each candidate
khan = 0
correy = 0
li = 0
otooley = 0

# Tally the votes for each candidate
for candidate in candidates:
    if candidate == "Khan":
        khan += 1
    elif candidate == "Correy":
        correy += 1
    elif candidate == "Li":
        li += 1
    else:
        otooley += 1
# Find out which candidate had the most votes
if (khan > correy and khan > li and khan > otooley):
    winner = "Khan"
elif (correy > khan and correy > li and correy > otooley):
    winner = "Correy"
elif (li > khan and li > correy and li > otooley):
    winner = "Li"
else:
    winner = "O'Tooley"

# Write the results to a text file in the same directory
with open("ElectionResults.txt", 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Khan: {round((khan/total_votes) * 100, 3)}% ({khan})\n")
    textfile.write(f"Correy: {round((correy/total_votes) * 100, 3)}% ({correy})\n")
    textfile.write(f"Li: {round((li/total_votes) * 100, 3)}% ({li})\n")
    textfile.write(f"O'Tooley: {round((otooley/total_votes) * 100, 3)}% ({otooley})\n")
    textfile.write("-------------------------------\n")
    textfile.write(f"Winner: {winner}")

# Print the same results to the console   
print("Election Results\n"
      "-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
print(f"Khan: {round((khan/total_votes) * 100, 3)}% ({khan})")
print(f"Correy: {round((correy/total_votes) * 100, 3)}% ({correy})")
print(f"Li: {round((li/total_votes) * 100, 3)}% ({li})")
print(f"O'Tooley: {round((otooley/total_votes) * 100, 3)}% ({otooley})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")