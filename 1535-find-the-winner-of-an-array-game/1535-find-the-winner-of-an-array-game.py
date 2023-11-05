class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(1, n - 1):
            arr[i] = max(arr[i], arr[i - 1])
            
        arr[0] = 0
        mx = 0
        past, count = 0, 0     
        for num in arr:
            if num == past:
                count += 1
            else:
                past = num
                count = 1
            
            if count >= k and num != 0:
                return num
            mx = max(mx, num)
            
        return mx