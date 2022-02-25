from heapq import heappush, heappop

class Solution:
    '''
    4   2   7   6   9   14   12
    0   0   5   0   3    5    0    
    '''
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(1,len(heights)):
            # print(heap)
            val = heights[i]-heights[i-1]
            if val<0:
                continue
            if ladders:
                heappush(heap, val)
                ladders-=1
            else:
                if not heap or heap[0]>=val:
                    if bricks-val<0:
                        return i-1
                    bricks-=val
                else:
                    heappush(heap, val)
                    val = heappop(heap)
                    if bricks-val<0:
                        return i-1
                    bricks-=val
                            
        return i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans = 0
#         def isPossible(idx,ladders,bricks):
#             heap = []
            
#             for i in range(1,idx+1):
#                 val = heights[i]-heights[i-1]
#                 if val>0:
#                     heappush(heap, -val)
#             print(idx, heap)
#             while heap:
#                 if ladders:
#                     ladders -= 1
#                     heappop(heap)
#                 elif bricks >= -heap[0]:
#                     bricks-=-heap[0]
#                     heappop(heap)
#                 else:
#                     return False
#             return True
        
#         i=1
#         while i<len(heights) and isPossible(i,ladders,bricks):
#             i+=1
                
#         return i-1