# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = collections.Counter(nums1)
        res = []
        
        for num in nums2:
            if(count[num] > 0):
                res.append(num)
                count[num] -= 1
        return res