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
# Open the election results and read the file
with open(file) as election_data:

 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    headers = next(file_reader)
    print(headers)

# 2. Write down the names of all the candidates.


# 3. Add a vote count for each candidate.


# 4. Get the total votes for each candidate.


# 5. Get the total votes cast for the election.

# Close the file.
#election_data.close()
