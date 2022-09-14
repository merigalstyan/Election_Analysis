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

An initial and important step of the analysis included adding dependencies **csv** and **os**. ***Csv** is necessary for spreadsheets and **os** would help finding the path to our election data.

**Here's how the code looks:**


<img width="553" alt="Screen Shot 2022-09-13 at 3 53 03 PM" src="https://user-images.githubusercontent.com/111609994/190023684-c2a3a743-06b1-4c5b-b8fd-edcc4d6502b8.png">

## Analysis: Section 1

The first section of the analysis was to open and read the **csv** data, loop through the rows of the spreadsheet and increment the total vote count by one to find * *the total number of votes* * which was equal to **369,711**. In order to find the names of the candidates and the votes they received, I initialized **candidate_options** as an empty list, then, inside the **for** loop each candidate_name was appended to candidate_options list. 

In addition, initializing the **candidate_votes** empty dictionary and asigning the already found candidate_name as a key I was able to increment **candidate_votes** by 1 every time the code found the name of the candidate in the spreadsheet. 

The formula to calculate the percentage of votes each candidate received is as follows:
* **(votes each candidate received / total votes) * 100)**

Using this formula and assigning them to variables resulted in the following outcome regarding the candidates, their votes and the percentage they received:

**Election Results**

**Total Votes: 369,711**

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

**A closer look:**

<img width="611" alt="Screen Shot 2022-09-13 at 4 10 19 PM" src="https://user-images.githubusercontent.com/111609994/190024998-3860e18b-93ab-4a15-8472-f1a4f2128eaf.png">

<img width="606" alt="Screen Shot 2022-09-13 at 4 10 38 PM" src="https://user-images.githubusercontent.com/111609994/190025014-493ea2fc-b8bd-4a4c-b5f2-5794c95f89b5.png">

### The winner

Based on the resulting data winning_candidate = "", winning_count = 0, winning_percentage = 0 variables were initialized. Using an if statement to determine if the fist vote count is greater than 0 and if the candidates' vote percentage is greater than the winning percentage I was able pring the winning candidate: 

**Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8% **

<img width="601" alt="Screen Shot 2022-09-13 at 4 16 51 PM" src="https://user-images.githubusercontent.com/111609994/190025654-7c8824de-b014-420d-896b-ed82086ee5b7.png">

### The results

As we already saw above, the winning candidate based on the election_data.csv was the candidate Diana DeGette with overall votes of 272,892. 
Based on the analysis of the total vote count, this number was 73.8%.

**We can use this code to output all the information to a text file using the same method of opening the file and choosing the "w" mode.**

## Analysis: Section 2

The second part of the analysis included a breakdown of the votes and the percentage of total votes for each county, and the largest number of votes from counties.

Let's break down this section.

Following the same path as the first section, **county** list, **county_votes** dictionary, **largest_county** empty string and **turnout_votes** variables were initialized and ready for analysis. In the same for loop, **county_name** from the first list of the spreadsheet was appended to the **county** list to find all the counties in the congressional elections. Their number was incremented by 1 each time the county appeared in the spreadsheet rows. This was done to calculate total votes for each counties. 

<img width="527" alt="Screen Shot 2022-09-14 at 2 41 31 PM" src="https://user-images.githubusercontent.com/111609994/190267904-f0b534b9-4928-4e40-972b-3ce03b071d9c.png">

Next, looping through **county_votes** dictionary, the percentage of total votes for each county was solved using the same formula mentioned above, this time dividing * *the total number of votes for each county* * by **Total votes * 100**.

<img width="686" alt="Screen Shot 2022-09-14 at 2 45 17 PM" src="https://user-images.githubusercontent.com/111609994/190268426-bed8cd4c-7c3d-426a-86f9-a388c4067230.png">

### The results

The results of these analysis are as follows:

County Votes:
-----------------------------

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

-------------------------------
Largest County Turnout: Denver


We can see that Denver had the largest number of votes winning with 82.8 %.

* ***All these outputs were saved in a text file.*** *

## Election_Audit Summary

The election analysis was used to find several data points regarding the congressional elections. We were able to see the winner candidate and the winning county with their percentage and total votes. This gives us a lot of information regarding the candidates and what people prefer. This script can be used for future elections to not only find out the winners and percentages, but with some modifications we can use this code to find population preferences. If we have enough survey data, for example, we could use this script to find future winners or social preference of nominated candidates. 

In addition, seeing which counties have the largest turnout, not only we can encourage these counties to participate in elections in the future, but we may use this information to organize events and campaigns in order to push passive counties take part in elections and vote. 





