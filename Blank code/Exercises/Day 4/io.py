def print_exercise(n):
    print("-"*15, "exercise", n, "-"*15)

# Hint, exerx=cices 8, 9 and 10 are the easiest

def ex1a():
    print_exercise("1a")
    """
    Read the file simplemaps-worldcities-basic.csv.
    Write a script which prints the names of the first 10 cities in the file.
    """


def ex1b():
    print_exercise("1b")
    """
    Change your script so it prints the names of all cities which have a
    population larger than 10,000,000.
    """



def ex2():
    print_exercise(2)
    """
    Write a script which creates a new file called large_cities.txt.
    The file should contain one line for each of the cities identified in
    question 1, formatted as follows:
        Buenos Aires, Argentina: population 11862073
        Sao Paulo, Brazil: population 14433147.5
        ...
    """



def ex3():
    print_exercise(3)
    """
    Read the file en-US.dic.
    Create a list consisting of the words in the file:
    ['a', 'A', 'AA', 'AAA', 'Aachen', "Aachen's", 'aardvark', ...]
    Print a small sample
    """



def ex4():
    print_exercise(4)
    """
    Write a function check_spelling which returns True if a given string is in
    words.txt, and returns False otherwise. (Hint: copy/paste from question 3).
    Use it to identify the incorrectly spelt word:
        accommodate, playwrite, rhythm.
    """



def ex5():
    print_exercise(5)
    """
    Read the file edward_lear.txt and create a list
    containing the words in the file. (Hint: use string.split(); don’t worry
    about punctuation marks.)
        ['Edward', 'Lear', 'The', 'Owl', 'and', ...]
    Use the function check_spelling to print all the incorrectly spelt words
    in the file.
    """



def ex6():
    print_exercise(6)
    """
    Write a function check_spelling_file which prints all the incorrectly spelt
    words in a given file.
    """



def ex7():
    print_exercise(7)
    """
    (Bonus). Improve your spellchecker: It doesn’t handle uppercase or
    punctuation well. Fix it.
    """


def ex8():
    print_exercise(8)
    """
    Open the file 'edward_lear.txt'. Print every line preceded by its line number:
    """


def ex9():
    print_exercise(9)
    """
    Creates a file 'squares.txt' consisting of the first 5 square numbers
    """



def ex10():
    print_exercise(10)
    """
    Create a file edward_lear_shouted.txt where all words from edward_lear.txt
    are capitalized
    """


def ex11():
    print_exercise(11)
    """
    Read rubgy_world_cup_20151.csv
    Write rubgy_veterans.csv with only the rows with players over 30.
    """


def ex12():
    print_exercise(12)
    """
    Parse fasta.txt into a dictionary with identifier:sequence
        { "Desulfitobacterium...":"ACTTGA...", "Clostridium...":"AGAGTTTGA..." }
    """

