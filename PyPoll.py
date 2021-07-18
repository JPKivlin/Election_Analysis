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
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:

    #To do:  Perform analysis
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)
    print(headers)
    

# Create a filename variable to a direct or indirect path to the file

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")





