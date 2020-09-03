# Many of the following functions are re-implemetations of built-in functions,
# for example "my_sum" is the same as "sum". Do not use the built-in versions.

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


def my_phrase():
    """Prints a phrase."""

    print("I love mango!!!")



def my_line(my_number):
    """Prints a line consisting of my_number times "-".

    Keyword arguments:
        my_number (int) -- Number of "-"

    Example: my_line(20) returns "--------------------"
    """

    print(my_number * "-")

def my_triangle(my_a, my_b):
    """Calculates the area of a right triangle given the length of the two
    shorter sides of the triangle.

    Keyword arguments:
        my_a (float) -- Length of side a.
        my_b (float) -- Length of side b.

    Returns:
        Float -- Area of the triangle.
    """

    return my_a * my_b / 2



def my_circle(my_radius):
    """Calculates the area of a circle given its radius.

    Keyword arguments:
        my_radius (float) -- Radius of the circle.

    Returns:
        Float -- Area of the circle.
    """

    return (3.14 * my_radius * my_radius)


def my_sum(my_list):

    """Calculates the sum of a given list.

    Keyword arguments:
        my_list (list) -- Given list.

    Returns:
        Float -- Sum of given list.
    """

    my_total = 0
    for i in my_list:
        my_total += i

    return my_total

def my_mean(my_list):
    """Calculates the mean of a given list.

    Keyword arguments:
    my_list (list) -- Given list.

    return (float) -- Mean of given list.
    """

    return my_sum(my_list)/len(my_list)



def my_percentage(my_list):
    """Calculates the percentage each element of a list is of the total given list.

    Keyword arguments:
        my_list (list) -- Given list.

    Returns:
        List -- Percentage of each element of the total given list."""

    my_percentage = []
    s = my_sum(my_list)

    for i in my_list:
        my_percentage.append(i/s)

    return my_percentage
    # or return [x / s  for x in my_list]





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


def my_even(my_number):
    """Checks if a number is even

    Keyword arguments:
        my_number (int) -- integer

    Returns:
        Bool -- Whether my_number is even
    """
    if my_number % 2 == 0:
        return True
    else:
        return False
    #or return my_number % 2 == 0


def my_reverse(my_string):
    """Reverses a given string.

    Keyword arguments:
    my_string (string) -- Given string.

    return (string) -- Reversed string."""

    lst = [my_string[i] for i in range(len(my_string)-1, -1, -1)]
    my_reversed_string = "".join(lst)

    return my_reversed_string
    #or retun my_string[::-1]
    #or return "".join(reversed(x))

def my_count(my_string, my_letter):
    """Counts the number of instances of a given letter in a given string.

    Keyword arguments:
        my_string (string) -- Given string.
        my_letter (char) -- Given letter.

    Returns:
        String -- Number of instances of given letter in given string.
    """

    my_counter = 0

    for i in range(0, len(my_string)):
        if my_string[i] == my_letter:
            my_counter += 1

    return my_counter

def my_replace(my_string, my_old_letter, my_new_letter):
    """Replaces in a given string all instances of a given letter with another
    given letter.

    Keyword arguments:
        my_string (string) -- Given string.
        my_old_letter (char) -- Given letter to be replaced.
        my_new_letter (char) -- Given letter to replace the first given letter.

    Returns:
        String -- String with replaced letters."""

    for i in range(0, len(my_string)):
        if my_string[i] == my_old_letter:
            my_string = my_string[:i] + my_new_letter + my_string[i+1:]

    return my_string

#Ex: Guess what the one-star function my_phrase returns
# None

def defaults(x = "No argument"):
    """Modify the function so that when it is called with one argument it
    returns that argument and the string "No argument" if there is none.

    Keyword arguments:
        x (any type) -- Any input.

    Returns:
        Either x or the string "No argument" """
    return x


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

def zipf(text):
    """Calculates the frequency of every word in a text.
    Extra credit: verify Zipf's law https://simple.wikipedia.org/wiki/Zipf%27s_law

    Keyword arguments:
        text (string) -- A large string.

    Returns:
        Dictionary (string: int) -- Dictionary of (word: frequency) pairs."""

    from collections import Counter
    return Counter(text.split())

def adds_args(*args):
    """Adds an arbitrary number of arguments
    Keyword argument:
        args (iterable of numbers) -- an iterable containing numbers

    Returns
        number -- Sum of all the numbers in args

    Ways to use the function:
        1) With hand-written arguments: adds_args(10), adds_args(10, 20), adds_args(1,2,3)...
        2) By using an iterable: add_args(?????) --Figure out the syntax--
        3) Mixing both: add_args(?????) --Figure out the syntax--
    """
    s = 0
    for num in args:
        s += num
    return s

def print_kwargs(**kwargs):
    """Prints an arbitrary number of key/value pairs
    Keyword argument:
        kwargs (dict) -- an dictionary

    Returns
        None

    Ways to use the function:
        1) With hand-written arguments: print_kwargs(name = "John", age = 12)
        2) By using an dictionnary: print_kwargs(?????) --Figure out the syntax--
        3) Mixing both: print_kwargs(?????) --Figure out the syntax--
    """
    for key in kwargs:
        print("The value of {} is {}".format(key, kwargs[key]))

def flexible_function(*args, **kwargs):
    """ A flexible function.
    - With no argument, the function should print "No argument" and return None
    - With number arguments, it prints "Numbers" and returns the product of the numbers
    - With named arguments, it prints "Named" and returns the value of the last named value
    - With both number and names, it prints "Combo" and returns the sum and the first named value
    """
    if args and kwargs:
        print("Combo")
        return(sum(args), list(kwargs.values())[0])

    elif args:
        print("Numbers")
        p = 1
        for arg in args:
            p *= arg
        return p

    elif kwargs:
        print("Named")
        return kwargs.popitem()[-1]

    else:
        print("No argument")
