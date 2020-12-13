# https://leetcode.com/problems/group-anagrams/

# ATTEMPT 1 - dict with sorted string as key
# Time  = O(NKlogK) where N is array length and K is word length
# Space = NK

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            srtdStr = "".join(sorted(i))
            if srtdStr in res:
                res[srtdStr].append(i)
            else:
                res[srtdStr] = [i]
          
        return [i[1] for i in res.items()]

# ATTEMPT 2 - Refactor of ATTEMPT 1
# Using defaultdict(list) and res.values() for efficiency
# BEST SOLUTION IN LEETCODE BENCHMARKS

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for i in strs:
            srtdStr = "".join(sorted(i))
            res[srtdStr].append(i)
        return res.values()

# ATTEMPT 3 - dict with letter count as key
# Time  = O(NK) where N is array length and K is word length
# Space = NK

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for i in strs:
            cnt = [0]*26 # array of counts per letter
            for c in i:
                cnt[ord(c)-ord('a')] += 1
            res[tuple(cnt)].append(i)
        return res.values()