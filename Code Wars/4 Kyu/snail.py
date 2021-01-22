# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

# ATTEMPT 1 - Using a True/False mirror grid to keep track of explored blocks
# TIME = O(n) where n is the number of blocks in the grid
# SPACE = O(n) 

def snail(snail_map):
    if(not snail_map or len(snail_map[0]) == 0): return []

    width = len(snail_map)
    openGrid = [[True for j in range(width)] for i in range(width)]
    
    out = []
    x,y = 0,0
    lastMove = ""
    
    # starting point
    out.append(snail_map[y][x])
    openGrid[y][x] = False
                
    while len(out) < width*width:
        # check if in top left corner -> move right
        if (x == 0 or not openGrid[y][x-1]) and (y == 0 or not openGrid[y-1][x]) and (lastMove is not "RIGHT"):
            lastMove="RIGHT"
            while (x < width - 1 and openGrid[y][x+1]):
                x += 1
                out.append(snail_map[y][x])
                openGrid[y][x] = False
                
        # check if in top right corner -> move down        
        elif (x == width - 1 or not openGrid[y][x+1]) and (y == 0 or not openGrid[y-1][x]) and (lastMove is not "DOWN"):
            lastMove="DOWN"
            while (y < width - 1 and openGrid[y+1][x]):
                y += 1
                out.append(snail_map[y][x])
                openGrid[y][x] = False
                
        # check if in bottom right corner -> move left
        elif (x == width - 1 or not openGrid[y][x+1]) and (y == width - 1 or not openGrid[y+1][x]) and (lastMove is not "LEFT"):
            lastMove="LEFT"
            while (x > 0 and openGrid[y][x-1]):
                x -= 1
                out.append(snail_map[y][x])
                openGrid[y][x] = False
                
        # check if in bottom left corner -> move up        
        elif (x == 0 or not openGrid[y][x-1]) and (y == width - 1 or not openGrid[y+1][x]) and (lastMove is not "UP"):
            lastMove="UP"
            while (y > 0 and openGrid[y-1][x]):
                y -= 1
                out.append(snail_map[y][x])
                openGrid[y][x] = False
            
    return out