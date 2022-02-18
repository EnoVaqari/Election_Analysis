# Election_Analysis

## Overview of Election Audit

### PURPOSE

The purpose of this project is to write a Python script for the election audit to deliver information for Colorado Board of Elections. The needed information is the following:

* Calculation of total number of votes casted.
* A complete of candidates who received votes.
* Total number of votes each candidate received.
* Percentage of votes each candidate won.
* The winner of election based on popular vote.


## Election-Audit Results
Outcome

![](https://github.com/EnoVaqari/Election_Analysis/blob/main/txt.png)

Terminal Outcome

![](https://github.com/EnoVaqari/Election_Analysis/blob/main/terminal_screenshot.png)

* There were a total of 369,711 votes cast in the congressional election.
* The total county votes were:
	* Jefferson with 38,855 votes (10.5%)
	* Denver with 306,055 votes (82.8%)
	* Arapahoe with 24,801 votes (6.7%). 

```
# Write a repetition statement to get the county from the county dictionary that was created
    for county_name in county_votes:
        # get county vote count
        county = county_votes.get(county_name)
        # percentage of votes for county.
        county_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({county:,})\n")

        # print the results of county to the terminal
        print(county_results, end="")
        # save county votes to txt
        txt_file.write(county_results)
        if (county > winning_county) and (county_percentage > winning_county_percentage):
            winning_county = county
            winning_county_candidate = county_name
            winning_county_percentage= county_percentage
	    
```

* Denver was the county with the largest number of 306,055 votes (82.8%).

```
# print largest turnout to terminal
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county_candidate}\n"
        f"-------------------------\n\n"
        f"Candidate Percentage of Votes:\n")
    print(winning_county_summary)

    # save the largest turnout to txt
    txt_file.write(winning_county_summary)

```

* Total votes each candidate received were:
	* Charles Casper Stockham with 85,213 votes (23.0%)
	* Diana DeGette with 272,892 votes (73.8%)
	* Raymon Anthony Doane with 11,606 votes (3.1%).

```
for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print results
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)


```

* The winner candidate was Diana DeGette with 272,892 votes (73.8%).

```
# Determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #  Print out the winning candidate, vote count and percentage of votes to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the wining candidate's results to the txt file
    txt_file.write(winning_candidate_summary)


```

### Election-Audit Summary

The script is successful as it accurately provides information on each are needed for analysis as listed above. The script can be used again with slight modifications to it. For example, we can use the same unchanged script for various counties by simply changing the csv dataset or we can use the same script with slight modifications for other election audit processes such as countries and cities.
