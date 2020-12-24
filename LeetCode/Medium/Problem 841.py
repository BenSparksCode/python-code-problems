# https://leetcode.com/problems/keys-and-rooms/

# ATTEMPT 1 - BFS with deque and dict to track visited rooms
# TIME = O(n + e) = O(n) where n = num of rooms and e = num of keys
# SPACE = O(n) to store key queue and room dict

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited = {i: False for i in range(len(rooms))}
        key_queue = collections.deque()
        
        # starting in room 0
        for key in rooms[0]:
            key_queue.append(key)
        rooms_visited[0] = True
        
        while len(key_queue) > 0:
            key = key_queue.popleft()
            rooms_visited[key] = True
            for i in rooms[key]:
                if not rooms_visited[i]:
                    key_queue.append(i)

        return not (False in rooms_visited.values())

# ATTEMPT 2 - Minor refactor to start with 0 in queue, avoiding first loop
# TIME = O(n + e) = O(n) where n = num of rooms and e = num of keys
# SPACE = O(n) to store key queue and room dict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited = {i: False for i in range(len(rooms))}
        key_queue = collections.deque()
        key_queue.append(0)

        while len(key_queue) > 0:
            key = key_queue.popleft()
            rooms_visited[key] = True
            for i in rooms[key]:
                if not rooms_visited[i]:
                    key_queue.append(i)

        return not (False in rooms_visited.values())