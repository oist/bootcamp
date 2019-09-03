# Run these in the console
# Warning, a few questions are trick questions

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

#Ex: give the value 3 to a, 5 to b and 0 to c
a, b, c = 3, 5, 0

#Ex: give the value 3 to a, 5 to b and 0 to c in a single line
a, b, c = 3, 5, 0

#Ex: divide a by b and b by a
a/b
b/a

#Ex: same, with integer division
a//b
b//a

#Ex: divide a by c, with float and integer division
#a/c
#a//c

#Ex: calculate b modulo a and b modulo c
b%a
#b%c

#Ex: calculate b to the power a
b**a

#Ex: set a to 7
a = 7

#Ex: add 10 to a using +=
a += 10

#Ex: check the type of a
type(a)

#Ex: without touching the "7" key on your keyboard, set b to the float value of 7
b = a - 10.

#Ex: check that b is a float
type(b)

#Ex: guess what the type of a+b should be
type(a+b)

#Ex: use the function input() to save a string entered by the user in the console
x = input()

#Ex: cast the string "12" into an int
int("12")

#Ex: set c to "hello goodbye" using a and b
a = "hello"
b = "goodbye"
c = a + " " + b

#Ex: set a to "I like the Bootcamp! " repeated 100 times
a = 100 * "I like the Bootcamp! "

#Ex: set b to True using only the variable a
a = False
b = not a


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


#Ex: set a,b,c,d to 1,2,4,12 and find 1 or 2 ways to combine all 4 variables with +-*// to make 24
#example: a*(c-b)*d
a,b,c,d = 1,2,4,12
a*(c-b)*d
(d-c)*(a+b)
(a+b)*c+d
a*c*d//b

#Ex: which strings can be cast to False? Which strings are cast to True?
bool("")
bool("anything else") # Any non-empty string

#Ex: which ints can be cast to False? Which ints are cast to True?
bool(0)
bool(42) # Or any non-zero value

#Ex: which floats can be cast to False? Which floats are cast to True?
bool(0.)
bool(3.14) # Or any non-zero value

#Ex: guess the values of int(t), float(t), str(t) for t True or False
[int(True), int(False), float(True), float(False), str(True), str(False)]

#Ex: Find 3 illegal ways to name a variable
# 0a = 1
# *a = 1
# @a = 0

#Ex: which is larger, True or False?
True > False

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

#Ex: guess the value of bool('False')
bool('False')

#Ex: find the built-in function f such that f('False') == False
eval('False')

#Ex: Guess the type of type(())
type(())

#Ex: Guess the type of type(None)
type(None)

#Ex: Guess the type of type(type(None))
type(type(None))

#Ex: what is the largest int you can define?
#Ans: something big enough to use all your computer's memory

#Ex: what is the difference between a multi-line comment and a multi-line string?
# None, they are just a string that doesn't do anything in the code
# You would have the same effect by typing numbers

#Ex: place the parentheses in the expression: a and b or c
# (a and b) or c

#Ex: place the parentheses in the expression: a and b or c and d
# (a and b) or (c and d)
