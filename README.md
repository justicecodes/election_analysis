# Election Analysis
Module 3: Python

## Overview of Election Audit: Explain the purpose of this election audit analysis.
The purpose of this analysis is to certify a vote count report for a US congressional race from Colorado. Mail in ballots, punch cards, and DRE ballots are combined for this count and analyzed using Python. Although it is more common to use Excel, Python code can be automated and replicated for producing a report for each candidate and county in similar races in the future.

## Election-Audit Results: 
- 369,711 total votes cast
### Voter turnout by county, in descending order:
- Denver : 306,055 votes, 82.8%
- Jefferson : 38,855 votes, 10.5%
- Arapahoe : 24,801 votes, 6.7%
- Denver County confirmed with the most votes with the following code:
<img width="607" alt="topcounty" src="https://user-images.githubusercontent.com/103595718/168487981-6596bc95-eda6-4686-9f6e-749392a5adbe.png">
 
### Winning Candidate: 
- Diana DeGette
- 73.8% of the total votes
- 272,892 votes received
- Other candidates: Charles Casper Stockham: 23.0% (85,213 votes), Raymon Anthony Doane: 3.1% (11,606)
<img width="719" alt="votecountbycandidate" src="https://user-images.githubusercontent.com/103595718/168488277-01ce021e-dcfe-42aa-bf65-2161d610a29a.png">
(This code snippet reads each row in the table and adds one count for the candidate each time their name appears)

## Election-Audit Summary: 
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
The code used to provide the report for this election can be modified for other similar counts. The complete set of votes must be provided as a CSV, and the following highlighted code must be altered to match the file path of the new file. 
<img width="573" alt="readcsv" src="https://user-images.githubusercontent.com/103595718/168489139-3f734d8e-130e-4989-9561-a3fa1736b08d.png">
The code provided may be used to count any number of candidates or counties since the code reads each row and only adds new values to the list. Modifications could be made to the headers to count a vote by city or region number. In addition, other columns could be added to denote the party or a second election on the same ballot. The column number read would need to be changed and variable names to better describe what is being counted. The code that counts the candidate votes and votes by county could be copied and reused if the variable names are changed appropriately. 
<img width="456" alt="pypollmodifications" src="https://user-images.githubusercontent.com/103595718/168489475-edf64b8d-703c-4ef3-8552-135a66bbf46f.png">
---
Further research was completed to consider the total population of each county in relation to how many votes were included in the report. Although each county has a similar population size, the number of voters from the three counties included in the report vary greatly. Differences could be attributed to different zoning for this particular race (only incorporating parts of some counties or areas with high pop. density). This report may not include all votes or a certain type of ballot, such as leaving out the hand-counted ballots which may be higher in areas without funding to provide electronic voting options. More information and analysis would need to be provided to determine the reason for this discrepancy.  
##### Voter turnout by county, as of 2018 US Census Bureau population
Denver co: 306,055/693,417 = 44.1% 
---
Arapahoe co: 24,801/636,671 = 3.9%
---
Jefferson co: 38,855/570,427 = 6.8%
