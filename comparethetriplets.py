import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    tri_a = 0
    tri_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            tri_a += 1
        elif a[i] < b[i]:
            tri_b += 1
    return(tri_a, tri_b)