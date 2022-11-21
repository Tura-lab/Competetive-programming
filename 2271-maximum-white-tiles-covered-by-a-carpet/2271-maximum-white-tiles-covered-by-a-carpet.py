class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        p_sum = [0]
        for a,b in tiles:
            p_sum.append(p_sum[-1] + b - a + 1)
            
        maximum = 0
        for i in range(len(tiles)):
            l, r = i, len(tiles)-1
            ans = l
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if tiles[mid][0] - tiles[i][0] + 1 <= carpetLen:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            if ans == i:
                maximum = max(maximum, min(carpetLen, tiles[i][1]-tiles[i][0]+1))
            else:
                val = p_sum[ans+1] - p_sum[i]
                if carpetLen < tiles[ans][1] - tiles[i][0] + 1:
                    val -= abs(carpetLen - (tiles[ans][1] - tiles[i][0] + 1))
                    
                maximum = max(maximum, val)

        
        return maximum