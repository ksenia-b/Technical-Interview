# recursion
# sample 0:

# def rec(x):
#     print(x)
#     rec(x + 1)
#
# rec(1)


# sample 1:
# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# print(factorial(3))
# print(factorial(5))
#
# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
#
# # Each function call represents an elf doing his work
# def deliver_presents_recursively(houses):
#     # Worker elf doing his work
#     if len(houses) == 1:
#         house = houses[0]
#         print("Delivering presents to", house)
#
#     # Manager elf doing his work
#     else:
#         mid = len(houses) // 2
#         first_half = houses[:mid]
#         second_half = houses[mid:]
#
#         # Divides his work among two elves
#         deliver_presents_recursively(first_half)
#         deliver_presents_recursively(second_half)


# sample 3
# import sys
# sys.setrecursionlimit(1000)
#
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print("factorial = ", fact(100))
# print(fact(5))


# sample 4, recursion in the list
# def sum(list):
#     sum = 0
#
#     # Add every number in the list.
#     for i in range(0, len(list)):
#         sum = sum + list[i]
#
#     # Return the sum.
#     return sum
#
#
# print(sum([5, 7, 3, 8, 10]))

# sample 4, recursively
# def sum(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] + sum(list[1:])
#
# print(sum([5,7,3,8,10]))


# recursion simplest example
# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x + 1)
#         print(x)
#
# rec(1)


# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x - 1) * x
#
#
# print(fact(4))


# #fibonacci
# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     #print( n)
#     # print(" 2 = ", fib(n - 2))
#
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(11))


# # Assume that remaining is a positive integer
# def hi_recursive(remaining):
#     # The base case
#     if remaining == 0:
#         return
#     print('hi')
#
#     # Call to function, with a reduced remaining count
#     hi_recursive(remaining - 1)
#
# hi_recursive(5)


def hi_recursive(remaining):
    if remaining == 0:
        return
    print("hi", remaining)
    hi_recursive(remaining - 1)
    print("finished", remaining)


hi_recursive(5)