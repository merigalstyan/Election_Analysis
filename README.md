# Election_Analysis

## Purpose

The purpose of the election audit analysis  was to look at the given election data from several counties, analyze it and find outcomes. 
The first part of the analysis includes:

* Finding the total number of votes cast in the congressional election.
* Calculating each candidate’s total votes and percentage of those votes.
* Finding the winning candidate.

The second section of the analysis includes:

* Finding each county and its total vote count.
* Calculating each county's percentage of the total votes.
* Finding the county with the largest number of voters.



## Analysis

### Dependencies

The initial step of the analysis included adding dependencies **csv** and **os**. ***Csv** is necessary for spreadsheets and **os** would help finding the path to our election data.

**Here's how the code looks:**


<img width="553" alt="Screen Shot 2022-09-13 at 3 53 03 PM" src="https://user-images.githubusercontent.com/111609994/190023684-c2a3a743-06b1-4c5b-b8fd-edcc4d6502b8.png">

## Analysis: Section 1

The first part of the analysis was to open and read the **csv** data, loop through the rows of the spreadsheet and increment the total vote count by one to find * *the total number of votes* * which was equal to **369,711**. In order to find the names of the candidates and the votes they received, I initialized **candidate_options** as an empty list, then, inside the **for** loop each candidate_name was appended to candidate_options list. 

In addition, initializing the **candidate_votes** empty dictionary and asigning the already found candidate_name as a key I was able to increment **candidate_votes** by 1 every time the code found the name of the candidate in the spreadsheet. 

The formula to calculate the percentage of votes each candidate received is as follows:
* **(votes each candidate received / total votes) * 100)**

Using this formula and assigning them to variables resulted in the following outcome regarding the candidates, their votes and the percentage they received:

Election Results

Total Votes: 369,711

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

### A closer look:

<img width="611" alt="Screen Shot 2022-09-13 at 4 10 19 PM" src="https://user-images.githubusercontent.com/111609994/190024998-3860e18b-93ab-4a15-8472-f1a4f2128eaf.png">

<img width="606" alt="Screen Shot 2022-09-13 at 4 10 38 PM" src="https://user-images.githubusercontent.com/111609994/190025014-493ea2fc-b8bd-4a4c-b5f2-5794c95f89b5.png">

## The winner

Based on the resulting data winning_candidate = "", winning_count = 0, winning_percentage = 0 variables were initialized. Using an if statement to determine if the fist vote count is greater than 0 and if the candidates' vote percentage is greater than the winning percentage I was able pring the winning candidate: 
**Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8% **

<img width="601" alt="Screen Shot 2022-09-13 at 4 16 51 PM" src="https://user-images.githubusercontent.com/111609994/190025654-7c8824de-b014-420d-896b-ed82086ee5b7.png">

## The results

As we already saw above, the winning candidate based on the election_data.csv was the candidate Diana DeGette with overall votes of 272,892. 
Based on the analysis of the total vote count, this number was 73.8%.

#We can use this code to output all the information to a text file using the same method of opening the file and choosing the "w" mode. 




