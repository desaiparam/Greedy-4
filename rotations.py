# Time Complexity : O(N) where N is the length of the tops/bottoms list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using a helper function that takes a target value (either from tops[0] or bottoms[0])
# and calculates the minimum rotations needed to make all values in tops or bottoms equal to that target.
# The helper function iterates through the tops and bottoms lists, counting the rotations needed for each
# If at any point neither tops[i] nor bottoms[i] matches the target, it returns -1 indicating it's not possible.
# Finally, I call the helper function twice, once with tops[0] and once with bottoms[0],
# and return the minimum rotations needed from either call

from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(target):
            tr = 0
            br = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1 
                if tops[i] == target and bottoms[i] == target:
                    continue
                if tops[i] != target:
                    tr += 1
                if bottoms[i] != target:
                    br += 1
            return min(tr,br)
        res = helper(tops[0])
        if res != -1:
            return res
        return helper(bottoms[0])
        