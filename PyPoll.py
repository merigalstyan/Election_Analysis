
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#Create empty dict
candidate_votes = {}


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        print(total_votes)

#2. A complete list of candidates who received votes
# Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
print(candidate_votes)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#3. The percentage of votes each candidate won
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#cd Desktop/"Bootcamp Modules"/"MODULE 3"/"Election_analysis"/"Resources"/"Election_results.csv"
# File to save for writing