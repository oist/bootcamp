# -*- coding: utf-8 -*-

def print_exercise(n):
    print("-"*15, "exercise", n, "-"*15)


en_jp = {"cat":"neko", "cute":"kawaii", "great":"subarashii", "I":"watashi", }

def ex1():
    print_exercise(1)
    """
    Translate s into Japanese (as much as possible) using en_jp
    """
    s = "I saw this super cute cat yesterday, what a great day!"
    print(" ".join([ en_jp.get(word, word) for word in s.split()]))


def ex2():
    print_exercise(2)
    """
    Create a dictionnary that indexes the height of 3 friends of yours with
    their names. Add them one at a time.
    What is the average height of your friends?
    """
    friends = {}
    friends["Shinji"] = 74
    friends["Ami"] = 168
    friends["Yuuki"] = 174
    print(sum(friends.values())/3)


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

def ex3():
    print_exercise(6)
    """
    Count the frequency of each word in script.
    Print them in descending order of frequency
    """
    d = {}
    for word in script.split():
        freq = d.get(word, 0)
        d[word] = freq+1
    elems = [(d[word], word) for word in d]
    print(sorted(elems)[::-1])


def ex4():
    print_exercise(4)
    """
    Add the elements of d2 into d1

    """
    d1 = {"I":"Groot", "Me":"Tarzan"}
    d2 = {"You":"Jane", "We":"World"}
    d1.update(d2)
    print(d1)


def ex5():
    print_exercise(5)
    """
    Get input from the user 5 times using a loop, add each input to a list
    indexed by "input" in d. Result should be something like:
        {'input': ['x', 'y', 'z', 'w', 's']}
    """
    d = {}
    for _ in range(5):
        x = input()
        lst = d.get("input", [])
        lst.append(x)
        d["input"] = lst
    print(d)



def ex6():
    print_exercise(6)
    """
    Using list comprehensions, filter out the values of en_jp where the English
    words are longer than 3 characters
    """
    print({ word:en_jp[word] for word in en_jp if len(word) <= 3})

