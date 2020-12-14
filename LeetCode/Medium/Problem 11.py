# https://leetcode.com/problems/container-with-most-water/

# ATTEMPT 1 - Brute force
# Time: O(n^2) approx = [n*(n-1)]/2
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for start in range(len(height)):
            for end in range(start, len(height)):
                new = min(height[start],height[end]) * (end-start)
                if new > res: res = new
        return res


# ATTEMPT 2 - 2 pivots closing in from each end
# Time: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, start, end = 0, 0, len(height)-1 
        while start < end:
            new = (end-start) * min(height[start],height[end])
            if new > res: res = new
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res