# https://www.hackerrank.com/challenges/kangaroo/problem

# ATTEMPT 1 - Represent jumping data as straight lines, find intersection
# TIME = O(1) 
# SPACE = O(1)

def kangaroo(x1, v1, x2, v2):
    if(v1 != v2):
        j = (x1 - x2) / (v2 - v1) - 1
        if j % 1 == 0 and j >= 0: return "YES"
    elif (x1 == x2): return "YES"
    return "NO"