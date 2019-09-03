import math

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
Ask for user input. If the input contains "ni" print "NI!"
"""
x = input("Tell me something about knights: ")
if 'ni' in x:
    print("NI!")


"""
Ask for user input. If the input is "cat" print "I like cats too!"
otherwise print "I don't like cats amyway!"
"""
x = input("Tell me something about felines: ")
if x == 'cat':
    print("I like cats too!")
else:
    print("I don't like cats either!")

"""
Ask the age of the user via input. If the user is below 20. praise them
about their youth, otherwise if they are below 30, praise them about their
maturity, otherwise praise them about their wisdom.
"""
age = int(input("How old are you?" ))
if age < 20:
    print("You are so young!")
elif age < 30:
    print("You are so mature!")
else:
    print("You are so wise!")

"""
Set x to 1. Keep doubling it until it becomes bigger than 1000. print x
"""
x = 1
while x <= 1000:
    x *= 2
print(x)


"""
Same as exercise, but this time also print the number of times x doubled.
"""
x = 1
n = 0
while x <= 1000:
    x *= 2
    n += 1
print(x, n)

"""
Create a list that contains the first 100 square numbers and print it
"""
x = []
for i in range(1,101):
    x.append(i**2)
print(x)

"""
Create a list that contains all pairs (i, j) for i, j between 1 and 5
"""
x = []
for i in range(1,6):
    for j in range(1,6):
        x.append((i, j))
print(x)

"""
How many values of sin(i) are positive, for all 'i' between 1 and 100?
Hint: use math.sin()
"""
c = 0
for i in range(1,101):
    if math.sin(i) > 0:
        c += 1
print("There are {} positive values".format(c))

"""
You’re a cop, and you know what that means: you love doughnuts. I mean, you
really, really love doughnuts. Throughout your day, you stop by every doughnut
shop in town and you pick up one doughnut more than you picked up in the previous
shop. For example: at the first shop, you pick up one doughnut. At the second
shop, you pick up two. At the third shop you pick up three, and so on.
How many donuts will you eat in a single day?
Hint: use enumerate
"""
shops = ["Krispy Kreme", "dunkin’ donuts", "Nuts of Dough", \
         "Dough-natto", "Doug’s Donuts", "Dough"]
donuts = 0
for n, _ in enumerate(shops):
    donuts += n + 1
print(donuts)


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
Create a list that contains the first 100 square numbers using list comprehensions
"""
x = [i**2 for i in range(1,101)]
print(x)


"""
Create a list that contains all pairs (i, j) for i, j between 1 and 5 using
list comprehensions
"""
x = [(i, j) for i in range(1,6) for j in range(1,6)]
print(x)

"""
How many values of sin(i) are positive, for all 'i' between 1 and 100?
Use list comprehensions.
Hint: use math.sin()
"""
x = [ math.sin(i) for i in range(1,101) if math.sin(i) > 0]
print("There are {} positive values".format(len(x)))

"""
Cut the string s in a list of chuncks of 3 characters:
    ['Wha', 't a ', 're ' ... ]
"""
s = "What are you doing with this knife? Stay away!"

chunks = []
while len(s) > 0:
    chunks.append(s[:3])
    s = s[3:]
print(chunks)

"""
Parse csv and save the values of the columns into three lists:
    - names (list of strings)
    - ages (list of ints)
    - heights (list of floats)
"""
csv = """name,age,height
John,22,176.1
Jake,50,180.2
Jimmy,12,150"""

names, ages, heights = [], [], []
rows = csv.split("\n")
del rows[0] # headers

for row in rows:
    name, age, height = row.strip().split(",")
    names.append(name)
    ages.append(int(age))
    heights.append(float(height))

print(names, ages, heights)


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
Save in a list the characters that are the same on the same index between
s1 and s2. Print the string of conjoined characters.
Hint: lookup the function zip
"""
s1 = "I think < minus 3 stop until tsar do happening"
s2 = "I lost :<> pop :3 see murderous thoughts trip inside"
s3 = "".join([ a for a,b in zip(s1,s2) if a==b])
print(s3)


"""
Write a script that reads the table in tsv, and prints the content of
each column, in the following way:
    header1:		nameA, nameB
    header2:		sampleA, sampleB
    header3:		experimentA, experimentB
"""
tsv = """# this is a comment line
# this is another comment line
header1\theader2\theader3
nameA\tsampleA\texperimentA
nameB\tsampleB\texperimentB"""

splits = [line.split("\t") for line in tsv.split("\n") if line[0]!="#"]
for x in zip(*splits):
    print(x[0], ":\t",", ".join(x[1:]))


"""fasta parsing
Write a script that prints the identifier of fasta (after the “>”),
prints the length of the AA sequence, and prints the number of tryptophan
AAs (W) in the sequence.
"""
fasta = """>sp|Q4VBE4|EGFLA_MOUSE Pikachurin OS=Mus musculus OX=10090 GN=Egflam PE=1 SV=1
MDLISTFSLHFLLLACSLPPGAVSLRTALRKSGKVGPPLDIKLGALNCTAFSIQWKTPKR
SGSSIIGYTVFYSEVGSDKSLRERSHNVPVGQDTLITEEVIGDLKPGTEYQVSVAAYSQT
GKGRLSFPRHVTTLSQDSCLPPAAPQQPHVLVVSDSEVALSWRPGENEGSAPIQSYSVEF
IRPDFDKSWTIIQERLQMDSMVIKGLDPDTNYQFAVKAMNAHGFSPRSWPSNTVRTLGPG
EAGSGHYGPGYITNPGVSEDDDGSEDELDLDVSFEEVKPLPATKVGNKKFSVESKKTSVS
NSVMGSRLAQPTSASLHETTVAIPPTPAQRKGKNSVAMMSRLFDMSCDETLCSADSFCVN
DYAWGGSRCHCNLGKGGEACSEDIFIQYPQFFGHSYVTFEPLKNSYQAFQVTLEFRAEAE
DGLLLYCGESEHGRGDFMSLALIRRSLHFRFNCGTGIAIIISETKIKLGAWHTVTLYRDG
LNGMLQLNNGTPVTGQSQGQYSKITFRTPLYLGGAPSAYWLVRATGTNRGFQGCVQSLSV
NGKKIDMRPWPLGKALNGADVGECSSGICDEASCIHGGTCAAIKADSYICLCPLGFRGRH
CEDAFALTIPQFRESLRSYAATPWPLEPQHYLSFTEFEITFRPDSGDGVLLYSYDTGSKD
FLSINMAAGHVEFRFDCGSGTGVLRSEAPLTLGQWHDLRVSRTAKNGILQVDKQKVVEGM
AEGGFTQIKCNTDIFIGGVPNYDDVKKNSGILHPFSGSIQKIILNDRTIHVKHDFTSGVN
VENAAHPCVGAPCAHGGSCRPRKEGYECDCPLGFEGLNCQKECGNHCLNTIIEAIEIPQF
IGRSYLTYDNPNILKRVSGSRSNAFMRFKTTAKDGLLLWRGDSPMRPNSDFISLGLRDGA
LIFSYNLGSGVASIMVNGSFSDGRWHRVKAVRDGQSGKITVDDYGARTGKSPGLMRQLNI
NGALYVGGMKEIALHTNRQYLRGLVGCISHFTLSTDYHISLVEDAVDGKNINTCGAK"""

seq = ""
for line in fasta.split("\n"):
    if line[0] == ">":
        identifier = line.strip()[1:]
        print(identifier)
    else:
        seq += line.strip()

print("Length of sequence:", len(seq))
print("Number of W:", seq.count("W"))
