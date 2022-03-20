#import poll
import os
import csv

#working directory
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Declaring variables
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
  

    # read each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #VOTE COUNT
    total_votes = (len(votes))
    print(total_votes)

    #Votes by Person
    for candidate in candidates:
        if candidate == "Charles_Casper_Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana_DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
    print(Charles_Casper_Stockham_votes)
    print(Diana_DeGette_votes)
    print(Raymon_Anthony_Doane_votes)
    
    
    #Percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 2)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 2)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 2)
    print(Charles_Casper_Stockham_percent)
    print(Diana_DeGette_percent)
    print(Raymon_Anthony_Doane_percent)

    
    #Winner 
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        winner = "Diana_DeGette"  
    else:
        winner = "Raymon_Anthony_Doane"

        #Print Statements

print(f"Election Results")
print(f"-----------------------------------")
print(f"Total Votes: {total_votes}"
print(f"-----------------------------------")
print(f"Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent_percent}% ({Charles_Casper_Stockham_percent_votes})")
print(f"Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})")
print(f"Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})")
print(f"-----------------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------------")


