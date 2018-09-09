import math

def print_exercise(n):
    print("-"*15, "exercise", n, "-"*15)


def ex1():
    print_exercise(1)
    """
    Create a list x that contains all integers from 1 to 10
    Print the list
    """
    x = list(range(1,11))
    print(x)


def ex2():
    print_exercise(2)
    """
    After each step, print the newly created variable or boolean
    1) create a list 'full' that has the first 10 letters of the alphabet
    2) create a list 'half1' with the first 5 elements of full into it
    3) create a list 'half2' with the last 5 elements of full into it
    4) verify that half1 and half2 together are the same as full
    5) create a variable 'last' with the last element of full in it
    6) create a list 'other' with every other element of full into it
    7) create a list 'rev' with the elements of full in reverse order into it
    8) create a list 'frank' with the fist two, middle 2 and last 2 elements of
       full into it
    9) add the character 'k' to full
    10) verify that 'k' is inside of full using the keyword 'in'
    11) replace the third letter of full by 'z
    """

    full = ['a','b','c','d','e','f','g','h','i','j']
    print(full)

    half1 = full[:5]
    print(half1)

    half2 = full[5:]
    print(half2)

    print(half1 + half2 == full)

    last = full[-1]
    print(last)

    other = full[::2]
    print(other)

    rev = full[::-1]
    print(rev)

    frank = full[:2] + full[4:6] + full[-2:]
    print(frank)

    full.append('k')
    print(full)

    print('k' in full)

    full[2] = 'z'
    print(full)



def ex3():
    print_exercise(3)
    """
    Create a list that contains the numbers from 1 to 100 and print it
    Also print the sum of the numbers
    """
    x = list(range(1,101))
    print(x)
    print(sum(x))


def ex4():
    print_exercise(4)
    """
    Get user input from the terminal and check if the input contains a "!"
    Hint: treat the string as a list of characters
    """
    x = input()
    print("!" in x)

def ex5():
    print_exercise(5)
    """
    Get user input and print the length of the input
    Hint: treat a string as a list of characters
    """
    x = input()
    print(len(x))


def ex6():
    print_exercise(6)
    """
    Get user input and sort the letters in alphabetical order using sorted()
    Hint: treat a string as a list of characters
    """
    x = input()
    print(sorted(x))