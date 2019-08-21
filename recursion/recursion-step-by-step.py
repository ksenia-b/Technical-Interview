# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))


# calc_factorial(4)              # 1st call with 4
# 4 * calc_factorial(3)          # 2nd call with 3
# 4 * 3 * calc_factorial(2)      # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1                  # return from 4th call as number=1
# 4 * 3 * 2                      # return from 3rd call
# 4 * 6                          # return from 2nd call
# 24                             # return from 1st call

def getTotal(n):
    total = 0

    for number in list(range(n+1)):
        print(number)
        total = total + number

    return total #print getTotal(5)


getTotal(5)

# factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# factorial example 2
# Example of recursion in Python to
# find the factorial of a given number

def factorial(num):
    """This function calls itself to find
    the factorial of a number"""

    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))


num = 5
print("Factorial of", num, "is: ", factorial(num))


#
def sum_recursive(nums):
    if len(nums) == 0:
        return 0

    last_num = nums.pop()
    return last_num + sum_recursive(nums)

#vdef factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)