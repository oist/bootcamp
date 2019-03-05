import math

"""
Ask for user input. If the input contains "ni" print "NI!"
"""
#x = input("Tell me something about knights: ")


"""
Ask for user input. If the input contains "cat" print "I like cats too!"
otherwise print "I don't like cats either!"
"""
#x = input("Tell me something about felines: ")


"""
Ask the age of the user via input. If the user is below 20. praise them
about their youth, otherwise if they are below 30, praise them about their
maturity, otherwise praise them about their wisdom.
Hint: don;t forget to converts the string input to int
"""


"""
Set x to 1. Keep doubling it until it becomes bigger than 1000. print x
"""


"""
Same as exercise, but this time also print the number of times x doubled.
"""


"""
Create a list that contains the first 100 square numbers and print it
"""



"""
Create a list that contains all pairs (i, j) for i, j between 1 and 5
"""


"""
Create a list with all the positive values of sin(i), for i between 1 and 100.
How many values are there?
Hint: use math.sin()
"""


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


"""
Cut the string s in a list of chuncks of 3 characters:
    ['Wha', 't a ', 're ' ... ]
"""
s = "What are you doing with this knife? Stay away!"



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




"""
Save in a list the characters that are the same on the same index between
s1 and s2. Print the string of conjoined characters.
Hint: lookup the function zip
"""
s1 = "I think < minus 3 stop until tsar do happening"
s2 = "I lost :<> pop :3 see murderous thoughts trip inside"


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
