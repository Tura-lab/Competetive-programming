class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        q.append(start)
        n = len(arr)
        seen = set()
        seen.add(start)
        
        print(len(arr))
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if arr[i] == 0:
                    return True
                if -1< i - arr[i]<n and (i - arr[i]) not in seen:
                    seen.add(i - arr[i])
                    q.append(i - arr[i])
                if -1< i + arr[i]<n and (i + arr[i]) not in seen:
                    seen.add(i + arr[i])
                    q.append(i + arr[i])
        return False