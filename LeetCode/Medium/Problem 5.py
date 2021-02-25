# https://leetcode.com/problems/longest-palindromic-substring/

# ATTEMPT 1 - Dynamic Programming + Middle-out.
# Works for most cases, just not some edge cases like 'ccd'
# TIME = O(N^2) -> nested loops and recursion with DP
# SPACE = O(N^2) -> inefficient dict usage

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if(not s or len(s)==1): return s
        memo = {}
        
        def isPal(sub):
            if(sub in memo): return memo[sub]
            if(len(sub) <= 1): memo[sub] = True
            else:
                memo[sub] = (sub[0] == sub[-1]) and isPal(sub[1:-1])
                
            return memo[sub]
        
        if(isPal(s)):
                   return s
            
        for center in range(len(s)):
            for offset in range(min(center+1, len(s)-center)):
                # Odd length palindromes
                subS = s[center-offset:center] + s[center] + s[center+1:center+offset+1]
                if(subS not in memo):
                    memo[subS] = isPal(subS)
                # Even length palindromes
                subS = s[center-offset+1:center+offset+1]
                if(subS not in memo):
                    memo[subS] = isPal(subS)
        
        return max([k for (k,v) in memo.items() if v], key=len)

# ATTEMPT 2 - Efficient n^2 optimized solution from comments
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
# Uses very clever proof by contradiction showing you can iterate through string once,
# storing start and length of best palindrome found so far.
# TIME = O(N^2) -> loop through s, + string slicing is O(n)
# SPACE = O(1) -> only stores maxLen and start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]