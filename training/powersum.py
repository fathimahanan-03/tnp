
import math
import os
import random
import re
import sys

def powerSum(X, N, num=1):
    val = num ** N
    if val == X:
        return 1
    if val > X:
        return 0
    return powerSum(X - val, N, num + 1) + powerSum(X, N, num + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
