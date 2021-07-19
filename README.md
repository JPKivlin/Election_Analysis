# Election_Analysis

## Election Audit Overview
The board of elections in the state of Colorado would like an audit performed of their recent election.  In addition to the candidate information already provided to our client, additional analysis was requested regarding the data as follows:
1.  The voter turnout for each county
2.  the percentage of votes from each county out of the total count
3.  the county with the highest turnout

### Resources
- Data Source:  [election_results.csv](Resources/election_results.csv)
- Software:  Python 3.8.8, Visual Studio Code, 1.58.2

## Election-Audit Results:

- Total votes cast:  369,711
- [Breakdown of number of votes and percentage of total votes by County](Resources/breakdown_county.png)
- Denver had the largest number of votes (306,055)
- [Breakdown of number of votes and percentage of total votes by Candidate](Resources/breakdown_candidate.png)
- The winner of the election was Diana DeGette: 73.8% of the total vote (272,892)

## Electrion-Audit Smmary
The script used in this analysis can be used for most election analysis with very few modifications, making it an ideal choice for future use by the Colorado board of elections.  Two modifications that could be mode are:
1.  The variable used for county's can be renamed to allow for use however the voting is broken down
2.  The results could be filtered to not include a candidate that received less than a certain amount of votes
