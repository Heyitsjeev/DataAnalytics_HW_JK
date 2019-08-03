import os
import csv

cvsElection = os.path.join("Resources", "election_data.csv")
totalVotes = 0
candidates = []
candidatesVotes = []
outputList = []

with open(cvsElection, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        if row[0] != None:
            totalVotes = totalVotes + 1

        if row[2] != None:
            candidates.append(row[2])

candidatesList = list(set(candidates))
candidatesList.sort()

for x in candidatesList:
    candidatesVotes.append(candidates.count(x))

print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {totalVotes}")
file = open("output.txt", "w")
file.write("Election Results\n")
file.write("------------------------------------------\n")
file.write(f"Total Votes: {totalVotes}\n")

for i in range(len(candidatesList)):
    #outputList.append({candidatesList[i]}: {'{:.2%}'.format(candidatesVotes[i]/len(candidates))} ({candidatesVotes[i]})
    print(f"{candidatesList[i]}: {'{:.2%}'.format(candidatesVotes[i]/len(candidates))} ({candidatesVotes[i]})")
    file.write(f"{candidatesList[i]}: {'{:.2%}'.format(candidatesVotes[i]/len(candidates))} ({candidatesVotes[i]})\n")

print("-------------------------------")
print(f"Winner: {candidatesList[candidatesVotes.index(max(candidatesVotes))]}")
print("------------------------------\n")

file.write("-------------------------------\n")
file.write(f"Winner: {candidatesList[candidatesVotes.index(max(candidatesVotes))]}\n")
file.write("------------------------------\n")








