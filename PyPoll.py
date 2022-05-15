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
#County variables
county_options = []
county_votes = {}
top_county = ""
winning_county = 0
winning_county_percentage = 0

# 1. Open the data file.
file = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


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
        county_name = row[1]
    # Add each new candidate option to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
    #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    # Add vote count for each candidate
        candidate_votes[candidate_name] += 1
    # Add each new candidate option to list
        if county_name not in county_options:
            county_options.append(county_name)
    #Begin tracking that candidate's vote count.
            county_votes[county_name] = 0
    # Add vote count for each candidate
        county_votes[county_name] += 1
        
# 3. Write down the names of all the candidates.
#print(f"The candidates running for office are: {candidate_options}")


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # 4. Get the total votes cast for the election.
    #print(f"Total votes cast in the election: {total_votes}\n")


    # 5. Determine the percentage of votes for each candidate by looping through the counts.
    #print("Final results by percent and total votes counted:")
    print("Candidate Results")
    txt_file.write("Candidate Results\n")
    # 5a) Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 5b) Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 5c) Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 5d) Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
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
    txt_file.write(winning_candidate_summary)

# 7. Election Results by County
    print("Results by County")
    txt_file.write("Results by County\n")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # 7a) Iterate through the county list.
    for county_name in county_votes:
        # 7b) Retrieve count of each county.
        county_count = county_votes[county_name]
        # 7c) Calculate the percentage of votes per county.
        county_percentage = float(county_count) / float(total_votes) * 100
        # 7d) Print the county name and percentage of votes.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county_count:,})\n")
        # Print each county, their voter count, and percentage to the terminal.
        print(county_results)
#  Save the county results to our text file.
        txt_file.write(county_results)
 # 8. Determine top county count
        # 8a) Determine if the votes are greater than the winning count.
        if (county_count > winning_county) and (county_percentage > winning_county_percentage):
            # 8b) If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_county = county_count
            winning_county_percentage = county_percentage
            # 8c) Set the winning_candidate equal to the candidate's name.
            top_county = county_name
    top_county_summary = (
        f"-------------------------\n"
        f"Top County: {top_county}\n"
        f"Top County Vote Count: {winning_county:,}\n"
        f"Top County Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(top_county_summary)
    txt_file.write(top_county_summary)


# Close the file.
election_data.close()
