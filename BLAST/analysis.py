"""
How many species had a hit?
How many hits per species?
What is the average alignment percentage per species?
"""

species = {}
result = "data/results.out"

with open(result) as f:
    for line in f:
        if line[0] == "#":
            continue
            
        row = line.strip().split("\t") # Getting each row and spliting it by tabulations

        alignments = species.get(row[0], []) # Retrieve existing values, or an empty list
        alignments.append(float(row[2])) # Third column is the alignment percentage
        species[row[0]] = alignments # Updating the ist of alignments


print("Number of species: {}".format(len(species)))

for sp in species:
    hits = len(species[sp])
    av = sum(species[sp])/hits
    print("Species: {}, number of hits: {}, average alignment percentage: {}"
          .format(sp, hits, av))
