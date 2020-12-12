# https://leetcode.com/problems/search-a-2d-matrix/

# ATTEMPT 1 - Searching using row ends as checkpoints
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or target is None: return False
        for row in matrix:
            if target >= row[0]:
                if target <= row[-1]:
                    for n in row:
                        if target < n:
                            return False
                        if target == n:
                            return True

# ATTEMPT 2 - Binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None: return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols-1
        
        while low <= high:
            mid = (low+high)//2
            num = matrix[mid//cols][mid%cols]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
                  
        return False