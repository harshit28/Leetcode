class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue,hashset=[rooms[0]], set()
        hashset.add(0)
        
        while queue:
            keys = queue.pop(0)
            for key in keys:
                if key not in hashset:
                    hashset.add(key)
                    queue.append(rooms[key])
        return len(hashset) == len(rooms)
