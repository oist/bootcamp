import math

def print_exercise(n):
    print("-"*15, "exercise", n, "-"*15)

def ex1():
    print_exercise(1)
    """
    Ask for user input. If the input contains "ni" print "NI!"
    """
    x = input()


def ex2():
    print_exercise(2)
    """
    Ask for user input. If the input contains "cat" print "I like cats too!"
    otherwise print "I don't like cats either!"
    """



def ex3():
    print_exercise(3)
    """
    Set x to 1. Keep doubling it until it becomes bigger than 1000. print x
    """



def ex4():
    print_exercise(4)
    """
    Same as exercise for, but this time also print the number of times x
    doubled.
    """



def ex5():
    print_exercise(5)
    """
    Create a list that contains the first 100 square numbers and print it
    """



def ex6():
    print_exercise(6)
    """
    Create a list that contains all pairs (i, j) for i, j between 1 and 5
    """



def ex7():
    print_exercise(7)
    """
    Create a list with all the positive values of sin(i), for i between 1 and 100.
    How many values are there?
    Hint: use math.sin()
    """



def ex8():
    print_exercise(8)
    """
    Save in a list the characters that are the same on the same index between
    s1 and s2. Print the string of conjoined characters.
    """
    s1 = "I think < minus 3 stop until tsar do happening"
    s2 = "I lost :<> pop :3 see murderous thoughts trip inside"



tsv = """# this is a comment line
# this is another comment line
header1\theader2\theader3
nameA\tsampleA\texperimentA
nameB\tsampleB\texperimentB"""


def ex9():
    print_exercise(9)
    """
    Write a script that reads the table in tsv, and prints the content of
    each column, in the following way:
        header1:		nameA, nameB
        header2:		sampleA, sampleB
        header3:		experimentA, experimentB
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

def ex10():
    print_exercise(10)
    """
    Write a script that prints the identifier of fasta (after the “>”),
    prints the length of the AA sequence, and prints the number of tryptophan
    AAs (W) in the sequence.
    """

csv = """name,age,height
John,22,176.1
Jake,50,180.2
Jimmy,12,150"""

def ex11():
    print_exercise(11)
    """
    Parse csv and save the values of the columns into three lists:
        - names (list of strings)
        - ages (list of ints)
        - heights (list of floats)
    """
    names, ages, heights = [], [], []


def ex12():
    print_exercise(12)
    """
    Cut the string s in a list of chuncks of 3 characters:
        ['Don', "'t ", 'you' ... ]
    """
    s = "What are you doing with this knife? Stay away!"

