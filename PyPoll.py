#Get the data from csv
#1.  Total number of votes cast
#2.  List of Canidates that received votes
#3.  % of votes cast for each canidate
#4.  Number of votes for each canidate
#5.  Winner of election by popular vote

# Add dependencies
import csv
import os



# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialzie variarble to 0
total_votes = 0

# Candidate options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

winning_candidate = 0
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Read each row in the CSV file
    for row in file_reader:
        total_votes += 1
        
        # Read each name from each row 
        candidate_name = row[2]
        
     
        if candidate_name not in candidate_options:
            
            
            # Add the candidate name to the candidate options list
            candidate_options.append(candidate_name)

           
 # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count
            votes = candidate_votes[candidate_name]
        
            # calculate the % of votes
            vote_percentage = float(votes) / float(total_votes) * 100

            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate_name}:  {vote_percentage:.1f} %  ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name



        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count:  {winning_count:,}\n"
            f"Winning Percentage:  {winning_percentage:.1f}%\n"
            f"------------------------------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)












