"""
How to reverse String in Java using Iteration and Recursion?

"""

str = "I like jam."

def reverse_string(s):
    new_str = ""
    s = list(s)

    for i in range(len(s)):
        # This needed for the reverce loop.
        char = s[len(s)- 1 - i]
        new_str = new_str + char

    print(new_str)

reverse_string(str)