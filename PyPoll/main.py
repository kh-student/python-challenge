import csv

# constants
CSV_PATH = "./Resources/election_data.csv"
OUTPUT_PATH = "./analysis/pypoll.txt"

# read file
with open(CSV_PATH) as file:
    csv_reader = csv.reader(file, delimiter=',')

    # header
    # Ballot ID,County,Candidate
    csv_header = next(csv_reader)

    # data
    total_votes = 0
    votes_dict = {}

    for row in csv_reader:
        # total votes
        total_votes+=1
        # votes
        # new candidate
        if not row[2] in votes_dict:
            votes_dict[row[2]] = 1
        # existing candidate
        else:
            votes_dict[row[2]]+=1

# results
# console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for k, v in votes_dict.items():
    print(f"{k}: {round(v/total_votes*100, 3)}% ({v})")
print("-------------------------")
print(f"Winner: {max(votes_dict, key=votes_dict.get)}")
print("-------------------------")

# file
with open(OUTPUT_PATH, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for k, v in votes_dict.items():
        file.write(f"{k}: {round(v/total_votes*100, 3)}% ({v})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {max(votes_dict, key=votes_dict.get)}\n")
    file.write("-------------------------\n")
