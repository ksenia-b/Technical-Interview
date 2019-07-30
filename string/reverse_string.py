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


# solution 2: recursion

def reverse(str):
    if str == "":
        return str
    else:
        return str[-1] + reverse(str[:-1])

print(reverse(str))


# solution3: ???
backward = lambda str: str[-1] + backward(str[:-1]) if str else str

print(backward)