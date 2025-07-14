#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    freq = defaultdict(int)

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substring = s[i:j]
            sig = ''.join(sorted(substring))
            freq[sig] += 1

    count = 0
    for val in freq.values():
        count+=(val*(val-1))//2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
