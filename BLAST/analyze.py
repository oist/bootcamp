result = "out.txt"

# Reading the data
with open(result) as f:
    lines = f.readlines()

# Dictionnary of {sequence title: frequency}
seq = {}

for line in lines:
    if line[0] == "#": # Skipping comments
        continue

    name = line.split("\t")[0] # We only care about the sequence name 

    if name in seq:
        seq[name] = seq[name] + 1
    else:
        seq[name] = 1

for name in sorted(seq):
    print(f"sequence {name} had {seq[name]} hits")

