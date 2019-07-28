"""
To start with, we have a simple String related coding question frequently asked in programming interviews. You need to write a program in Java, C, C++, Python, Perl, or Ruby to print duplicate characters from a given String.

For example, if String is "Java" then the program should print "a". Bonus points if your program is robust and handles different kinds of input e.g. String without duplicate, null or empty String etc. Bonus points if you also write unit tests for normal and edge cases.


Read more: https://javarevisited.blogspot.com/2015/01/top-20-string-coding-interview-question-programming-interview.html#ixzz5uzGDUx00
"""

"""
Implement an algorithm to determine if the string has all unique characters.
"""
s1 = 'unique'
s2 = 'bear'

def is_unique(s):
    return len(s) == len(set(s))

print(is_unique(s1))
print(is_unique(s2))


"""
How to print the unique values from the string.
"""
print(set(s1))


#============= 1 solution =============

s = "Java"
result = {}

if s == None or s == '':
    print("The string is empty or null.")
if is_unique(s):
    print("The string is unique.")
else:
    for character in s:
        if character not in result.keys():
            result[character] = 0

        count = result[character]
        result[character] = count + 1

    for k, value in result.items():
        if value > 1:
            print(k)

