import pandas as pd

data = pd.read_csv(r'C:\Users\eddie\OneDrive\Desktop\Class_Requirements\UofM-VIRT-DATA-PT-09-2024-U-LOLC\03-Python\Homework\Starter_Code\PyPoll\Resources/election_data.csv')

print(data.columns)

total_votes = len(data['Ballot ID'])

candidates = data['Candidate'].unique()

votes_per_candidate = data['Candidate'].value_counts()

vote_percentages = (votes_per_candidate / total_votes) * 100

winner = votes_per_candidate.idxmax()

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    percentage = vote_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, votes in votes_per_candidate.items():
        percentage = vote_percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")