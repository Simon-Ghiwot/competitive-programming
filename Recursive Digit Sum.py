#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def find_super_digit(n):
    if n < 10:
        return n
    total = 0
    for i in str(n):
        total += int(i)
    return find_super_digit(total)

def superDigit(n, k):
    total = 0
    for i in str(n):
        total += int(i) * k
    return find_super_digit(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
