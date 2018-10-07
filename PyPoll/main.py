#Modules
import os
import csv

# Set path for file
poll_csv = os.path.join('election_data.csv')

#Open and read csv
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    totalVotes = 0
    totalKhan = 0
    totalCorrey = 0
    totalLi = 0
    totalOTooley = 0

    #Read through each row after header
    for row in csvreader:

        #Add '1' for each row
        totalVotes += 1

        #Add '1' for each candidate for each vote
        if str(row[2]) == "Khan":
            totalKhan += 1

        elif str(row[2]) == "Correy":
            totalCorrey += 1

        elif str(row[2]) == "Li":
            totalLi += 1

        else:
            totalOTooley += 1

# Find the candidate with the most votes
if totalCorrey > totalKhan and totalLi and totalOTooley:
    winner = "Correy"

elif totalLi > totalKhan and totalOTooley:
    winner = "Li"

elif totalKhan > totalOTooley:
    winner = "Khan"

else:
    winner = "O'Tooley"

#Calculate the percentage of votes for each candidate
percentKhan = "%.3f" % (totalKhan/totalVotes*100)
percentCorrey = "%.3f" % (totalCorrey/totalVotes*100)
percentLi = "%.3f" % (totalLi/totalVotes*100)
percentOTooley = "%.3f" % (totalOTooley/totalVotes*100)

#Print results

print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(totalVotes)}")
print(f"----------------------------")
print(f"Khan: {str(percentKhan)}% ({str(totalKhan)})")
print(f"Correy: {str(percentCorrey)}% ({str(totalCorrey)})")
print(f"Li: {str(percentLi)}% ({str(totalLi)})")
print(f"O'Tooley: {str(percentOTooley)}% ({str(totalOTooley)})")
print(f"----------------------------")
print(f"Winner: {str(winner)}")
print(f"----------------------------")

#Create and write ouputs into a text file

output_txt = os.path.join('pypoll_results.txt')
with open(output_txt, 'w') as writefile:
    writefile.write(f"Election Results\n")
    writefile.write(f"----------------------------\n")
    writefile.write(f"Total Votes: {str(totalVotes)}\n")
    writefile.write(f"----------------------------\n")
    writefile.write(f"Khan: {str(percentKhan)}% ({str(totalKhan)})\n")
    writefile.write(f"Correy: {str(percentCorrey)}% ({str(totalCorrey)})\n")
    writefile.write(f"Li: {str(percentLi)}% ({str(totalLi)})\n")
    writefile.write(f"O'Tooley: {str(percentOTooley)}% ({str(totalOTooley)})\n")
    writefile.write(f"----------------------------\n")
    writefile.write(f"Winner: {str(winner)}\n")
    writefile.write(f"----------------------------\n")