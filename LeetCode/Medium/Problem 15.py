# https://leetcode.com/problems/3sum/

# ATTEMPT 1 - 2 pointers simultaneously closing in on 0
# RESULT = Wrong answer when nums is symmetrical e.g. [-2,-1,0,1,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        sort_nums = sorted(nums)
        if sort_nums[0] > 0 or sort_nums[-1] < 0: return []
        
        temp, start, end = 0, 0, len(nums)-1
        res = set()
        
        while start < end:
            # if both on same side of 0, can't sum to make 0
            if sort_nums[start]*sort_nums[end] > 0: break
            set_sum = sort_nums[start] + sort_nums[end]
            
            # shift the pivot thats needed to bring closer to 0
            if set_sum > 0:
                temp = sort_nums[start+1]
                set_sum += temp
            else:
                temp = sort_nums[end-1]
                set_sum += temp

            if set_sum == 0:
                res.add((sort_nums[start], sort_nums[end], temp))
            
            if temp > 0:
                start += 1
            else:
                end -= 1
                
        return list(res)


# ATTEMPT 2 - 3 pointers (anchor, p1, p2), anchor as all negatives then all positives.
# RESULT = Wrong answer on later tests 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3: return []
        sort_nums = sorted(nums)
        if sort_nums[0] > 0 or sort_nums[-1] < 0: return []
        
        anchor, p1, p2 = 0, nums_len-1, nums_len-2
        res = set()
        
        # Anchor on left
        while anchor < nums_len and sort_nums[anchor] <= 0:
            while sort_nums[p1] >= 0 and sort_nums[p2] >= 0 and p2 > anchor:
                if sort_nums[anchor] + sort_nums[p2] + sort_nums[p1] == 0:
                    res.add((sort_nums[anchor], sort_nums[p2], sort_nums[p1]))
                if sort_nums[anchor] + sort_nums[p1] < sort_nums[p2] and sort_nums[p2] > 0:
                    p2 -= 1
                else:
                    p1 -= 1
                    p2 = p1 - 1
                    
            anchor += 1
            p1, p2 = nums_len-1, nums_len-2
            
        # Anchor on right
        anchor, p1, p2 = nums_len-1, 0, 1
        while anchor > 0 and sort_nums[anchor] > 0:
            while sort_nums[p1] <= 0 and sort_nums[p2] <= 0 and p2 < anchor:
                if sort_nums[anchor] + sort_nums[p2] + sort_nums[p1] == 0:
                    res.add((sort_nums[p1], sort_nums[p2], sort_nums[anchor]))
                if sort_nums[anchor] + sort_nums[p1] > sort_nums[p2] and sort_nums[p2] < 0:
                    p2 += 1
                else:
                    p1 += 1
                    p2 = p1 + 1
            
            anchor -= 1
            p1, p2 = 0, 1
            
        return list(res)

# ATTEMPT 3 - Removed p2 pointer - calc it instead with anchor - p1
# RESULT = Seems to pass all tests but hits TIME LIMIT EXCEEDED

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3: return []
        sort_nums = sorted(nums)
        if sort_nums[0] > 0 or sort_nums[-1] < 0: return []
        
        anchor, p1 = 0, nums_len-1
        res = set()
        
        # Anchor on left
        while anchor < nums_len and sort_nums[anchor] <= 0:
            while sort_nums[p1] >= 0 and p1 > anchor:
                if sort_nums[p1] < -0.5*sort_nums[anchor]: break
                
                third_num = -(sort_nums[anchor] + sort_nums[p1])
                if third_num >= 0 and third_num <= sort_nums[p1] and third_num in sort_nums:
                    if third_num != sort_nums[p1]:
                        res.add((sort_nums[anchor], third_num, sort_nums[p1]))
                    else:
                        if third_num != sort_nums[anchor] and third_num == sort_nums[p1] and sort_nums.count(third_num) > 1:
                            res.add((sort_nums[anchor], third_num, sort_nums[p1]))
                        elif third_num == sort_nums[anchor] and third_num == sort_nums[p1] and sort_nums.count(third_num) > 2:
                            res.add((sort_nums[anchor], third_num, sort_nums[p1]))                        
                p1 -= 1
                    
            anchor += 1
            p1 = nums_len-1
            
        # Anchor on right
        anchor, p1 = nums_len-1, 0
        while anchor > 0 and sort_nums[anchor] > 0:
            while sort_nums[p1] <= 0 and p1 < anchor:
                if sort_nums[p1] > -0.5*sort_nums[anchor]: break
                
                third_num = -(sort_nums[anchor] + sort_nums[p1])
                if third_num < 0 and third_num >= sort_nums[p1] and third_num in sort_nums:
                    if third_num != sort_nums[p1]:
                        res.add((sort_nums[p1], third_num, sort_nums[anchor]))
                    else:
                        if third_num == sort_nums[p1] and sort_nums.count(third_num) > 1:
                            res.add((sort_nums[p1], third_num, sort_nums[anchor]))
                        
                p1 += 1
                    
            anchor -= 1
            p1 = 0
            
        return list(res)



