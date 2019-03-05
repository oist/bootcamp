import math

"""
Ask for user input. If the input contains "ni" print "NI!"
"""
x = input("Tell me something about knights: ")
if 'ni' in x:
    print("NI!")


"""
Ask for user input. If the input contains "cat" print "I like cats too!"
otherwise print "I don't like cats either!"
"""
x = input("Tell me something about felines: ")
if 'cat' in x:
    print("I like cats too!")
else:
    print("I don't like cats either!")

"""
Ask the age of the user via input. If the user is below 20. praise them
about their youth, otherwise if they are below 30, praise them about their
maturity, otherwise praise them about their wisdom.
Hint: don;t forget to converts the string input to int
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
# x = [i**2 for i in range(1,101)]
x = []
for i in range(1,101):
    x.append(i**2)
print(x)



"""
Create a list that contains all pairs (i, j) for i, j between 1 and 5
"""
#x = [(i, j) for i in range(1,6) for j in range(1,6)]
x = []
for i in range(1,6):
    for j in range(1,6):
        x.append((i, j))
print(x)


"""
Create a list with all the positive values of sin(i), for i between 1 and 100.
How many values are there?
Hint: use math.sin()
"""
#x = [ math.sin(i) for i in range(1,101) if math.sin(i) > 0]
# print("There are {} positive values".format(len(x)))
c = 0
for i in range(1,101):
    if math.sin(i) > 0:
        c += 1
print("There are {} positive values".format(c))


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
