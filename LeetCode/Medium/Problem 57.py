# https://leetcode.com/problems/insert-interval/

# ATTEMPT 1 - Iteratively merging overlaps
# TIME = O(n) where n is length of intervals
# SPACE = O(n) 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not newInterval: return intervals
        if not intervals: return [newInterval]
        out = []
        for i in range(len(intervals)):
            # Check newInt's start is bigger than i's end
            if intervals[i][1] < newInterval[0]:
                out.append(intervals[i])
                continue
            # Check newInt's end is smaller than i's start -> add all i's left and break
            elif intervals[i][0] > newInterval[1]:
                out = out + [newInterval] + intervals[i:]
                break
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        if(newInterval not in out): out.append(newInterval)
        return out