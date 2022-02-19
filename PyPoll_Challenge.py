# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary
candidate_votes = {}

# create county list and county votes dictionary
county_options = []
county_votes = {}

# Track Winning Candidate and Winning vote count and percentage 
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county = 0
winning_county_percentage = 0

# track the largest county and county voter turnout.
large_turnout_county = ""
largest_turn_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   
    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add votes to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Get the county name
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            # Tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # if statement to check that county fors not match any existing county in the list
        if county_name not in county_options:

            # add the candidate name to list.
            county_options.append(county_name)

            # track county's vote count
            county_votes[county_name] = 0

        # Add a vote to the count
        county_votes[county_name] += 1


# save result to txt file
with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results) 

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
    
    # print largest turnout to terminal
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county_candidate}\n"
        f"-------------------------\n\n"
        f"Candidate Percentage of Votes:\n")
    print(winning_county_summary)

    # save the largest turnout to txt
    txt_file.write(winning_county_summary)


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
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
