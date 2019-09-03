# Run these in the console

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
Create a list x that contains all integers from 1 to 10
Print the list
"""
x = list(range(1,11))


"""
Create a list that contains the numbers from 1 to 100 and print it
Also print the sum of the numbers
"""
x = list(range(1,101))
print(x)
print(sum(x))

"""
Create a list that contains all even numbers from 2 to 100 and print it
"""
x = list(range(2,101,2))
print(x)

"""
After each step, print the newly created variable or boolean
1) print the list 'friends'
2) create a list 'half1' with the first 5 elements of friends into it
3) create a list 'half2' with the last 5 elements of friends into it
4) verify that half1 and half2 together are the same as friends
5) create a variable 'last' with the last element of friends in it
6) create a list 'other' with every other element of friends into it (first, third...)
7) create a list 'rev' with the elements of friends in reverse order into it
8) create a list 'classmates' with the fist two, fifth and 6th, and last 2 elements of
friends into it
9) add the 'Kieran' to friends
10) verify that 'Kieran' is inside of friends using the keyword 'in'
11) replace the third element of friends by 'Zoe'
"""

friends = ['Alice','Bob','Charly','Dave','Eve','Fiona','Gina','Hector','Isabel','Jeremie']
print(friends)

half1 = friends[:5]
print(half1)

half2 = friends[5:]
print(half2)

print(half1 + half2 == friends)

last = friends[-1]
print(last)

other = friends[::2]
print(other)

rev = reversed(friends)
print(rev)

classmates = friends[:2] + friends[4:6] + friends[-2:]
print(classmates)

friends.append('Kieran')
print(friends)

print('Kieran' in friends)

friends[2] = 'Zoe'
print(friends)


"""
Get user input from the terminal and check if the input contains a "!"
Hint: treat the string as a list of characters
"""
x = input("Tell me something: ")
print("!" in x)

"""
Get user input and print the length of the input
Hint: treat a string as a list of characters
"""
x = input("Tell me something: ")
print(len(x))


"""
Get user input and sort the letters in alphabetical order using sorted()
Hint: treat a string as a list of characters
"""
x = input("Tell me something: ")
print(sorted(x))


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
Which lists can be cast to False? True?
"""
bool([]) == False
bool([1, 2]) == True # Any non-empty list

"""
Reverse the list x by using slicing
"""
x = [1, 2, 3]
x[::-1]

"""
Create the matrix m (2 dimensional list)
1 2 3
4 5 6
7 8 9
"""
m = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]

"""
Print the center element (5) of m
"""
m[1][1]

"""
Create the submatrix s which contains only the last 2 rows of m using slicing
operations
"""
m[1:3]

"""
Name 3 lists methods that work on tuples
Name 3 list methods that don't wotk on tuples
"""
# Work: in, count, index, sorted, len, max, sum, +, *...
# Don't work: append, insert, remove, sort...

"""
Guess what the method x.pop() does.
Check the documentation for other interesting list methods.
"""
# It removes the last element of x and returns it



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
Create a list that contains itself
"""
x = [1, 2, "Hello"]
x.append(x)
print(x)
print(x[-1])
print(x[-1][-1])

"""
What is the link between parallel assignment of variables and tuples?
"""
# They are the same thing with parentheses dropped

"""
Create a tuple with the numbers 1 to 100
"""
t = tuple(range(1,101))

"""
Find the identity tuple e for the operation + (Meaning: e + e == e)
Find the identity tuple e for the operation * (Meaning: e * 3 == e)
"""
# The empty tuple () for both

"""
Guess what a 'set' does and experiement using 'set()' on lists and the notation
a = {1,2,3,3,2,1}
Browse the documentation about sets
"""
# It's a list without duplicates

"""
Using sets, check that a list has no duplicates
"""
x == list(set(x))
