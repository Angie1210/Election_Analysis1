#open de data file
#retrieve the name of the candidates
#get the total number of votes per candiata
#percetange, total number of candidates, ?get the total of votes
#retrieve the name of candidates with more votes

#import datetime
#now=datetime.datetime.now()
#print (now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes=0
candidate_options=[]
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:


# To do: read and analyze the data here.
    file_reader= csv.reader(election_data)
# Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    headers=next(file_reader)
    # print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes=total_votes+1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
    
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
            votes=candidate_votes[candidate_name]
            vote_percentage=float(votes)/float(total_votes)*100
            
            candidate_results=(
                f"{candidate_name}: received {vote_percentage:.2f}% of the vote \n")
            print(candidate_results)
            txt_file.write(candidate_results)

            if (votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate= candidate_name
        #     print(f"Election results\n---------------\nTotal Votes: {total_votes}\n--------------")
    #     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

    # print(f"Winnin candidate is {winning_candidate} with {winning_count} votes and {winning_percentage}%")
# print (total_votes)
# print(candidate_options)
# print(candidate_votes)
# print (vote_percentage)


     
    
