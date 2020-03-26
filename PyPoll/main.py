import os
import csv

os.chdir(os.path.dirname(__file__))
PyPollcsv = os.path.join("Data","election_data.csv")

candidate_votes = {}
candidate_percentages ={}
most_votes = 0
votes = []

with open(PyPollcsv, 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvread)

    for row in csvread:
        votes.append(row[0])
        total_votes = (len(votes))   
        #votes/candidate
        if row[2] in candidate_votes:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        else:
            candidate_votes[row[2]] = 1
#candidate vote% & winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > most_votes:
        most_votes = vote_count
        winner = person

Analysistxt = os.path.join("Analysis","Results_txt")

with open(Analysistxt, 'w') as text:
    text.write('Election Results\n')
    text.write('----------------------------\n')
    text.write(f"Total Votes: {(len(votes))}" + "\n")
    text.write('----------------------------\n')
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count}) \n")
    text.write('----------------------------\n')
    text.write(f"Winner: {winner}" + "\n")

with open(Analysistxt, 'r') as readfile:
    print(readfile.read())