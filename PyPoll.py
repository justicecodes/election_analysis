# Import modules.
import datetime as dt
import csv
import random
#import numpy
import os

"""""
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
"""
# 1. Open the data file.
file = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
"""""
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")

"""""
#Initialize a total vote counter.
total_votes = 0
#List for candidate names & counter
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
    # Print the candidate name from each row
        candidate_name = row[2]
    # If the candidate does not match any existing candidate add name to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add vote count for each candidate
        candidate_votes[candidate_name] += 1
        
# 2. Write down the names of all the candidates.
print(f"The candidates running for office are: {candidate_options}")

# 3. Add a vote count for each candidate.


# 4. Get the total votes cast for the election.
print(f"Total votes cast in the election: {total_votes}\n")


# Determine the percentage of votes for each candidate by looping through the counts.
print("Final results by percent and total votes counted:")
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Close the file.
election_data.close()
