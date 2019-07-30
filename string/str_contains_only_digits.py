"""
You need to write a program to check a String contains only numbers by using Regular expression.

"""
str = "Akula21"

def is_digit(str):
    for char in str:
        if not char.isdigit():
            print("The string do not connect only digits.")
