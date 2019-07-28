"""A simple coding problem based upon String, but could also be asked with numbers. You need to write a Java program to check if two given strings are anagrams of Each other. Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation, and capitalization. Each letter should have the same count in both strings. For example, the Army and Mary are an anagram of each other.

"""

str_1 = "Army"
str_2 = "Mary"
str_3 = "Mary Land"

def is_anagram(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")

    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    alphabet = "abcdefghijlmnopqrstuvwxyz"

    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1

    return dict_1 == dict_2


# True = is_anagram, False = not anagram
print(is_anagram(str_1, str_2))
print(is_anagram(str_1, str_3))