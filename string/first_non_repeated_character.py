"""
How to program to print first non repeated character from String?

Read more: https://javarevisited.blogspot.com/2015/01/top-20-string-coding-interview-question-programming-interview.html#ixzz5uzeFObjn

"""

str = "Meeting"


def find_first_non_repeated_character(s):
    dict_1 = dict.fromkeys(list(str), 0)

    print(dict_1)

    for i in range(len(s)):
        count = dict_1[s[i]] + 1
        dict_1[s[i]] = count

        if count > 1:
            # The second key 'e' will have count == 2 once we loop throung the first two characters.
            # First loop: m=1, e=0
            # Second loop: m=1, e=1
            # Third loop: m=1, e=2
            # !!! So we should substract 2

            first_non_repeated = s[i - 2]

            print("First non repeated character is: ", first_non_repeated)



find_first_non_repeated_character(str)