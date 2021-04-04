# https://www.hackerrank.com/challenges/encryption/problem

# ATTEMPT 1
# TIME = O(n) 
# SPACE = O(n)

import math

def encryption(s):
    if(not s): return ''
    
    cols = math.ceil(math.sqrt(len(s)))
    rows = math.floor(math.sqrt(len(s)))
    
    s_trim = s.replace(" ","")
    out_str = ''
    grid = []
    
    if(cols*rows < len(s)): rows += 1
    
    for i in range(rows):
        grid.append(s_trim[i*cols : (i+1)*cols])
        
    for i in range(cols):
        for j in grid:
            if len(j) <= i:
                out_str += ""
            else: 
                out_str += j[i]
        out_str += ' '

    return out_str