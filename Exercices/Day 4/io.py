"""
Creates a file 'squares.txt' consisting of the first 5 square numbers
"""
with open("squares.txt", "w") as f:
    for i in range(1,6):
        f.write("{}\n".format(i*i))
print("see squares.txt")

"""
Open the file 'edward_lear.txt'. Print every line preceded by its line number.
Hint: use enumerate
"""
with open("edward_lear.txt") as f:
    for i, line in enumerate(f):
        print("{} {}".format(i+1, line.strip()))

"""
Create a file edward_lear_shouted.txt where all words from edward_lear.txt
are capitalized
"""
with open("edward_lear.txt") as f:
    lear = f.read()

with open("edward_lear_shouted.txt", "w") as f:
    f.write(lear.upper())
print("see edward_lear_shouted.txt")


"""
Read the file simplemaps-worldcities-basic.csv.
Write a script which prints the names of the first 10 cities in the file.
"""
with open("simplemaps-worldcities-basic.csv") as f: # Reading the file
    f.readline() # Skipping the header line
    for _ in range(10):
        line = f.readline() # Read line
        data = line.strip().split(",") # split the line
        city = data[1]
        print(city) # Select and print city name


"""
Change your script so it prints the names of all cities which have a
population larger than 10,000,000.
"""
with open("simplemaps-worldcities-basic.csv") as f: # Reading the file
    f.readline() # Skipping the header line
    for line in f:
        data = line.strip().split(",") # split the line
        city = data[1]
        pop = float(data[4])
        if pop > 10**7:
            print("{} ({})".format(city,pop))


"""
Write a script which creates a new file called large_cities.txt.
The file should contain one line for each of the cities identified in
question 1, formatted as follows:
    Buenos Aires, Argentina: population 11862073
    Sao Paulo, Brazil: population 14433147.5
    ...
"""
with open("large_cities.txt", "w") as out:
    with open("simplemaps-worldcities-basic.csv") as f: # Reading the file
        f.readline() # Skipping the header line
        for line in f:
            data = line.strip().split(",") # split the line
            city = data[1]
            pop = float(data[4])
            country = data[5]
            if pop > 10**7:
                out.write("{}, {}: population {}\n".format(city,country,pop))
print("See large_cities.txt")


"""
Read the file en-US.dic.
Create a list consisting of the words in the file:
['a', 'A', 'AA', 'AAA', 'Aachen', "Aachen's", 'aardvark', ...]
Print a small sample
"""
with open("en-US.dic") as f:
    dic = [word.strip() for word in f]

print(dic[:10]) # Printing just a sample


"""
Write a function check_spelling which returns True if a given string is in
words.txt, and returns False otherwise. Use the list from the previous question.
Use it to identify the incorrectly spelt word:
    accommodate, playwrite, rhythm.
"""
def check_spelling(word):
    return word in dic

for word in ["accommodate", "playwrite", "rhythm"]:
    print("{} is an English word: {}".format(word, check_spelling(word)))


"""
Read the file edward_lear.txt and create a list
containing the words in the file. (Hint: use string.split(); don’t worry
about punctuation marks.)
    ['Edward', 'Lear', 'The', 'Owl', 'and', ...]
Use the function check_spelling to print all the incorrectly spelt words
in the file.
"""
with open("edward_lear.txt") as f:
    words = f.read().split()

incorrect = [word for word in words if not check_spelling(word)]
print(incorrect)


"""
Write a function check_spelling_file which prints all the incorrectly spelt
words in a given file.
"""
def check_spelling_file(filename):
    with open(filename) as f:
        words = f.read().split()

    return [word for word in words if not check_spelling(word)]

print(check_spelling_file("edward_lear.txt"))


"""
(Bonus). Improve your spellchecker: It doesn’t handle uppercase or
punctuation well. Fix it.
"""
dic2 = [word.lower() for word in dic]

def clean(word):
    return word.lower().strip(".,;!?<>[]\{\}\"\'-")

def check_spelling2(word):
    return clean(word) in dic2

def check_spelling_file2(filename):
    with open(filename) as f:
        words = f.read().split()

    return [word for word in words if not check_spelling2(word)]

print(check_spelling_file2("edward_lear.txt"))


"""
Read rubgy_world_cup_20151.csv
Write rubgy_veterans.csv with only the rows with players over 30.
"""
with open('rugby_world_cup_20151.csv') as file:
    with open('rubgy_veterans.csv', 'w') as out:
        header = file.readline()
        out.write(header)

        for line in file:
            data = line.strip().split(',')
            age = int(data[4])
            name = data[1]
            if age > 30:
                print('{} ({})'.format(name, age))
                out.write(line)


"""
Parse fasta.txt into a dictionary with identifier:sequence
    { "Desulfitobacterium...":"ACTTGA...", "Clostridium...":"AGAGTTTGA..." }
"""
fasta = {}
with open("fasta.txt") as f:
    identifier = ""
    seq = ""
    for line in f:
        if line[0] == ">":
            if identifier != "":
                fasta[identifier] = seq
                seq =""
            identifier = line.strip()[1:]
        else:
            seq += line.strip()
    print(fasta)
