# https://leetcode.com/problems/number-of-islands/
# https://en.wikipedia.org/wiki/Depth-first_search

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: return 0
        
        score = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    score += 1
                    self.dfs(grid, i, j)
        
        return score
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = "#"
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)