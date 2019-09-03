# -*- coding: utf-8 -*-

"""     .
       ,O,
      ,OOO,
'oooooOOOOOooooo'
  `OOOOOOOOOOO`
    `OOOOOOO`
    OOOO'OOOO
   OOO'   'OOO
  O'         'O
"""

"""
Create a dictionnary that indexes the height of 3 friends of yours with
their names. Add them one at a time.
What is the average height of your friends?
"""
friends = {}
friends["Shinji"] = 74
friends["Ami"] = 168
friends["Rei"] = 53
print(sum(friends.values())/len(friends))

"""
Add the elements of d2 into d1
"""
d1 = {"I":"Groot", "Me":"Tarzan"}
d2 = {"You":"Jane", "We":"World"}
d1.update(d2)
print(d1)


"""     .                 .
       ,O,               ,O,
      ,OOO,             ,OOO,
'oooooOOOOOooooo' 'oooooOOOOOooooo'
  `OOOOOOOOOOO`     `OOOOOOOOOOO`
    `OOOOOOO`         `OOOOOOO`
    OOOO'OOOO         OOOO'OOOO
   OOO'   'OOO       OOO'   'OOO
  O'         'O     O'         'O
"""

"""
Translate s into Japanese (as much as possible) using en_jp
"""
en_jp = {"cat":"neko", "cute":"kawaii", "great":"subarashii", "I":"watashi", }
s = "I saw this super cute cat yesterday, what a great day!"
print(" ".join([ en_jp.get(word, word) for word in s.split()]))

"""
Using list comprehensions, filter out the values of en_jp where the English
words are longer than 3 characters
"""
print({ word:en_jp[word] for word in en_jp if len(word) <= 3})


"""
Get input from the user 5 times using a loop, add each input to a list
indexed by "input" in d. Result should be something like:
    {'input': ['x', 'y', 'z', 'w', 's']}
"""
d = {}
for _ in range(5):
    x = input("Please write something: ")
    lst = d.get("input", [])
    lst.append(x)
    d["input"] = lst
print(d)


"""     .                 .                 .
       ,O,               ,O,               ,O,
      ,OOO,             ,OOO,             ,OOO,
'oooooOOOOOooooo' 'oooooOOOOOooooo' 'oooooOOOOOooooo'
  `OOOOOOOOOOO`     `OOOOOOOOOOO`     `OOOOOOOOOOO`
    `OOOOOOO`         `OOOOOOO`         `OOOOOOO`
    OOOO'OOOO         OOOO'OOOO         OOOO'OOOO
   OOO'   'OOO       OOO'   'OOO       OOO'   'OOO
  O'         'O     O'         'O     O'         'O
"""

"""
Get input from the user 5 times using a loop, add each input to a list
indexed by "input" in d. Result should be something like:
    {'input': ['x', 'y', 'z', 'w', 's']}
Do this in a single line using list comprehensions
"""
d = {}
d["input"] = [input("Please write something: ") for _ in range(5)]

"""
Count the frequency of each word in script.
Print them in descending order of frequency
"""
script = """
BABY BRIAN COHEN: [crying]
WISE MAN #1: Ahem.
MANDY COHEN: Ohhh! [whump] Who are you?
WISE MAN #1: We are three wise men.
MANDY: What?!
WISE MAN #1: We are three wise men.
MANDY: Well, what are you doing creeping around a cow shed at two o'clock in the morning? That doesn't sound very wise to me.
WISE MAN #3: We are astrologers.
WISE MAN #1: We have come from the East.
MANDY: Is this some kind of joke?
WISE MAN #2: We wish to praise the infant.
WISE MAN #1: We must pay homage to him.
"""
d = {}
for word in script.split():
    freq = d.get(word, 0)
    d[word] = freq + 1
print(sorted(d.items(), key = lambda x : x[1], reverse = True))

"""
Find the most unlikely objects/data structures that can be used as a key
"""
# Keys must be hashable, may not contain mutable ojects. Most things in Python.
# Unlikely: ranges (range(10)), functions (math.sin, lambda), module (math),
# IO objects (open("file")), types (dict, _), ellipsis (...), ...

"""BLAST result analysis
Write a script that calculates the mean value of the values in the `% identity`
field for each species ('Bacterium', 'Aspergillus'...) from 'results'.
Save those values in a dictionary.
"""

results = """
# BLASTN 2.2.30+
# Query: Bacterium_levoglucosan-1(Bacillus)
# Database: data/database/My16sAmplicon
# Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# 513 hits found
Bacterium_levoglucosan-1(Bacillus)\tgi|295702242:9181-10722\t97.42\t1396\t32\t4\t1\t1394\t62\t1455\t0.0\t2375
Bacterium_levoglucosan-1(Bacillus)\tgi|294496875:9180-10721\t97.35\t1396\t33\t4\t1\t1394\t62\t1455\t0.0\t2370
Bacterium_levoglucosan-1(Bacillus)\tgi|384044176:356446-357987\t97.35\t1396\t33\t4\t1394\t62\t1455\t0.0\t2370
Bacterium_levoglucosan-1(Bacillus)\tgi|488570484:10449-11988\t94.73\t1386\t62\t1014\t1394\t74\t1453\t0.0\t2145
# BLASTN 2.2.30+
# Query: Aspergillus_sp._HX-2006f(fungi)
# Database: data/database/My16sAmplicon
# Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# 1 hits found
Aspergillus_sp._HX-2006f(fungi)	gi|367036261:601304-603099	90.99	866	71	7	3	867	780	1639	0.0	 1164
# BLASTN 2.2.30+
# Query: Uncultured_fungus_isolate_DGGE_gel_band_1 (fungi)
# Database: data/database/My16sAmplicon
# Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# 1 hits found
Uncultured_fungus_isolate_DGGE_gel_band_1	gi|367036261:601304-603099	95.01	341	17341	20	360	1e-153	  536
"""

species = {}
for line in results.strip().split("\n"):
    if line[0] == "#":
        continue
    row = line.split("\t") # Getting each row and spliting it by tabulations

    alignments = species.get(row[0], []) # Retrieve existing values, or an empty list
    alignments.append(float(row[2])) # Third column is the alignment percentage
    species[row[0]] = alignments # Updating the ist of alignments

for sp in species:
    av = sum(species[sp]) / len(species[sp])
    species[sp] = av

print(species)
