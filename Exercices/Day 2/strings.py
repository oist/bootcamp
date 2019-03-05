"""
How many ni are there in s?
"""
s = "We are the knight who say ni!"
print(s.count("ni"))


"""
get rid of the trailing characters in s
"""
s = "Stop walking in such a silly way!  \t  \n"
print(s.strip())


"""
Change this list of characters into a string
"""
lst = ['I', ' ', 'a', 'm', ' ', 'n', 'o', 't', ' ', 'a', ' ', 'l', 'i', 's', 't']
print("".join(lst))


"""
replace {one} by a, {two} by b and {three} by c in s using format
"""
s = "I am agent {one}, my phone number ends in {two} and I have {three} cats."
a, b, c = str(1).zfill(3), "02", 3
print(s.format(one=a, two=b, three=c))


"""
Initialize the following variable:
    s = "When SPAMming is the SPAMmote of mental SPAMmed."

Save and print the string without SPAMs.
"""
s1 = "When SPAMming is the SPAMmote of mental SPAMmed."
s2 = s1.replace("SPAM", "")
print(s2)


"""
Initialize the following variable:
    s1 = "Beware of HABU snakes"

Print the uppercase version of the string made of the first 2 and last 2
characters of s1, then find the word HABU and replace it with the newly
found word. Print the result.
"""
s1 = "Beware of HABU snakes"
s2 = (s1[:2] + s1[-2:]).upper()
s3 = s1.replace("HABU", s2)
print(s3)


""" Initialize a sting that will print as:
Symbol meaning
\n    new-line
\t    tab
\'    single quote
\"    double quote
"""
s = "\\n\tnew-line\n\\t\ttab\n\\\'\tsingle quote\n\\\"\tdouble quote"
print(s)


"""
change the commas in s into tabs by using split and join.
Also replace the word comma by tab
"""
s = "comma,divided,text,lol"
print("\t".join(s.split(",")).replace("comma", "tab"))


"""
Get user input, print the input without the white spaces
"""
x = input("Tell me something with spaces: ")
print("".join(x.split()))
