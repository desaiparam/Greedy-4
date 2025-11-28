# Time Complexity : O(MlogN) where M is the length of the target string and N is the length of the source string
# Space Complexity : O(N) for the hashmap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using a hashmap to store the indices of each character in the source string.
# I then iterate through the target string and for each character, I perform a binary search
# on the list of indices from the hashmap to find the smallest index that is greater than or
# equal to the current index in the source string.
# If such an index is found, I update the current index to that index + 1
# and move to the next character in the target string.
# If no such index is found, it means we need to start a new subsequence from
# the beginning of the source string, so I reset the current index to 0
# and increment the count of subsequences used.
# If at any point a character in the target string is not found in the source string,
# I return -1 as it is impossible to form the target string.


from collections import defaultdict
from typing import List
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        mapy = defaultdict(list)
        for i,c in enumerate(source):
            mapy[c].append(i)
        def bs(lis,target):
            low = 0
            high = len(lis)-1
            while low <= high:
                mid = low + (high - low)//2
                if lis[mid] == target:
                    return mid
                elif lis[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        i = 0
        j = 0
        count = 0
        while j < len(target):
            tchar = target[j]
            if tchar not in mapy:
                return -1
            lis = mapy[tchar]
            idx = bs(lis,i)
            if idx == len(lis):
                i = lis[0]
                count += 1
            else:
                i = lis[idx]
                i += 1
                j += 1
                if j == len(target):
                    return count + 1
            if i == len(source):
                i = 0
                count += 1
        return -1
