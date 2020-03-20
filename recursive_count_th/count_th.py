"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

"""
str.find(substring) returns the first occurance of a substring, so we need to continue to search until we reach len(str) == 0. This is our base case.  
If we find the substring in the first two characters, we need to call the function recursively starting from index 1 and increment.
If we do not find the substring, the call the function without incrementing 
"""


def count_th(word):
    if len(word) == 0 or len(word) == 1:
        return 0
    else:
        if word[0:2] == "th":
            return count_th(word[1:]) + 1
        else:
            return count_th(word[1:])


print(count_th("abcthefthghith"))
