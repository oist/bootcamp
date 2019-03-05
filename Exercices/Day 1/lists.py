"""
EX 1
Create a list x that contains all integers from 1 to 10
Print the list
"""
x = list(range(1,11))
print(x)


"""
EX 2
Create a list that contains the numbers from 1 to 100 and print it
Also print the sum of the numbers
"""
x = list(range(1,101))
print(x)
print(sum(x))


"""
EX 3
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

rev = friends[::-1]
print(rev)

classmates = friends[:2] + friends[4:6] + friends[-2:]
print(classmates)

friends.append('Kieran')
print(friends)

print('Kieran' in friends)

friends[2] = 'Zoe'
print(friends)


"""
EX 4
Get user input from the terminal and check if the input contains a "!"
Hint: treat the string as a list of characters
"""
x = input("Tell me something: ")
print("!" in x)

"""
EX 5
Get user input and print the length of the input
Hint: treat a string as a list of characters
"""
x = input("Tell me something: ")
print(len(x))


"""
EX 6
Get user input and sort the letters in alphabetical order using sorted()
Hint: treat a string as a list of characters
"""
x = input("Tell me something: ")
print(sorted(x))
