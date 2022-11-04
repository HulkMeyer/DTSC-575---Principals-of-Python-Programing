# Create a program, palindrome.py that has a function that takes one string
# argument and prints a sentence indicating if the text is a palindrome.
# The function should consider only the alphanumeric characters in the string,
# and not depend on capitalization, punctuation, or whitespace.

import sys

def palindrome(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
        string == reverse
    if True:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

string = str(sys.argv[1])

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
res=" "
for ele in string:
    if ele not in punc:
        res += ele
string = res.lower()

palindrome(string)
