# Runtime: 64 ms, faster than 89.03% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Keys and Rooms.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms == [] or rooms == [[]]:
            return True

        visited = [False for i in range(len(rooms))]
        queue = [(0, rooms[0])]

        while queue:
            elem = queue.pop(0)
            room_num = elem[0]
            keys = elem[1]
            if visited[room_num] == False:
                visited[room_num] = True
                for key in keys:
                    queue.append((key, rooms[key]))

        for i in range(len(visited)):
            if visited[i] == False:
                return False
        return True