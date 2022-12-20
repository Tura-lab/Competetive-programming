class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = collections.deque()
        n = len(rooms)
        
        s = set()
        q.append(0)
        s.add(0)
        n-=1
        
        while q:
            room = q.popleft()
            for v in rooms[room]:
                if v not in s:
                    n-=1
                    s.add(v)
                    q.append(v)
                    
        return n==0