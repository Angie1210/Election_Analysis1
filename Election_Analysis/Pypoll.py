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

# Open the election results and read the file.
with open(file_to_load) as election_data:


# To do: read and analyze the data here.
    file_reader= csv.reader(election_data)
# Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    headers=next(file_reader)
    print(headers)
