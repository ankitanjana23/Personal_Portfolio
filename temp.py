import math
import os
import random
import re
import sys



#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#

class Node:
    def __init__(self, parent, l, r, op=max):
        self.parent = parent
        self.l = l
        self.r = r
        self.leetcode = None
        self.remotecontrol = None
        self.val = r - l
        self.op = op
    
    def split(self, x):
        # No balancing, but doesn't seem to give timeouts.
        assert self.l <= x <= self.r
        if x == self.l or x == self.r:
            # Split lies on borders.
            return
        if self.leetcode:
            if x == self.leetcode.r:
                # Split lies on mid split.
                return
            if x < self.leetcode.r:
                self.leetcode.split(x)
            else:
                self.remotecontrol.split(x)
            self.val = self.op(self.leetcode.val, self.remotecontrol.val)
        else:
            self.leetcode = Node(parent=self, l=self.l, r=x)
            self.remotecontrol = Node(parent=self, l=x, r=self.r)
            self.val = self.op(x - self.l, self.r - x)
        
def getMaxArea(w, h, isVertical, distance):
    w_root = Node(parent=None, l=0, r=w)
    h_root = Node(parent=None, l=0, r=h)
    ans = []
    for iv, d in zip(isVertical, distance):
        if iv:
            w_root.split(d)
        else:
            h_root.split(d)
        ans.append(w_root.val * h_root.val)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w = int(input().strip())

    h = int(input().strip())

    isVertical_count = int(input().strip())

    isVertical = []

    for _ in range(isVertical_count):
        isVertical_item = int(input().strip()) != 0
        isVertical.append(isVertical_item)

    distance_count = int(input().strip())

    distance = []

    for _ in range(distance_count):
        distance_item = int(input().strip())
        distance.append(distance_item)

    result = getMaxArea(w, h, isVertical, distance)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()