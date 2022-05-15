# Import modules.
import datetime as dt
import csv
import random
import numpy
import os

# Initiate variables
#Total vote counter.
total_votes = 0
#List for candidate names
candidate_options = []
#Dictionary for vote counts per candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 1. Open the data file.
file = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
# 2. Read each row in table to add a total vote count and a count for each candidate.

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
    # Print the candidate name from each row
        candidate_name = row[2]
    # Add each new candidate option to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add vote count for each candidate
        candidate_votes[candidate_name] += 1
        
# 3. Write down the names of all the candidates.
print(f"The candidates running for office are: {candidate_options}")


# Save the results to our text file.
#with open(file_to_save, "w") as txt_file:


# 4. Get the total votes cast for the election.
print(f"Total votes cast in the election: {total_votes}\n")


# 5. Determine the percentage of votes for each candidate by looping through the counts.
print("Final results by percent and total votes counted:")
# 5a) Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 5b) Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 5c) Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 5d) Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# 6. Determine winning vote count and candidate
    # 6a) Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 6b) If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 6c) Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
# Report winner summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

"""""
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")

"""""

# Close the file.
election_data.close()
