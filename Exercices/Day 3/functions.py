def my_phrase():
    """Prints a phrase."""

    print("I love mango!!!")



def my_line(my_number):
    """Prints a line consisting of my_number times "-".

    Keyword arguments:
        my_number (int) -- Number of "-"
    """

    print(my_number * "-")



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
    #or return sum(my_list)/len(my_list)



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



def my_triangle(my_a, my_b):
    """Calculates the area of a triangle given the length of the two shorter sides
    of the triangle.

    Keyword arguments:
        my_a (float) -- Length of side a.
        my_b (float) -- Length of side b.

    Returns:
        Float -- Area of the triangle.
    """

    return (my_a * my_b / 2)



def my_circle(my_radius):
    """Calculates the area of a circle given its radius.

    Keyword arguments:
        my_radius (float) -- Radius of the circle.

    Returns:
        Float -- Area of the circle.
    """

    return (3.14 * my_radius * my_radius)



def my_reverse(my_string):
    """Reverses a given string.

    Keyword arguments:
    my_string (string) -- Given string.

    return (string) -- Reversed string."""

    my_reversed_string = ""

    lst = [my_string[i] for i in range(len(my_string)-1, -1, -1)]
    my_reversed_string = "".join(lst)

    return my_reversed_string
    #or retun my_string[::-1]



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


