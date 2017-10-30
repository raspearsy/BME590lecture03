
# import random
# import sys
# import os
# import math

'''
name = 'HI'
print(name)
** = ^
quote = "\"Hi friends!\""
print('I like the quote: ', quote)

tuple has () around it, hard to change stuff in it though (have to convert to list [] then convert back)
first_tuple = (3,4,4)
second_tuple = list(first_tuple)
new_tuple = tuple(second_tuple) #how to convert back to tuple
'''

# Will ensure the inputs are not NaN (throw error if so) and then add them if their sum is >=0, if not return 0


def summer(num1, num2):
    if type(num1) is str or type(num2) is str or type(num1) is bool or type(num2) is bool:
        print('Error, not an int or float, NaN, throwing error -1')
        return -1
    else:
        sum_num = num1 + num2
        if isinstance(sum_num, complex):
            if sum_num.real < 0:
                return 0
            else:
                return sum_num
        elif sum_num < 0:
                return 0
        elif sum_num >= 0:
            return sum_num